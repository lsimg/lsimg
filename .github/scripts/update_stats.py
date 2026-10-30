"""Render profile cards from public GitHub data using the Python standard library."""

from collections import Counter
from datetime import datetime, timedelta, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "lsimg")
if not re.fullmatch(r"[A-Za-z0-9-]+", OWNER):
    raise ValueError("Unexpected GitHub owner")
USE_CLI = "--gh-cli" in sys.argv


def api(path):
    if USE_CLI:
        result = subprocess.run(
            ["gh", "api", path], check=True, capture_output=True, encoding="utf-8"
        )
        return json.loads(result.stdout)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-stats-generator",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request("https://api.github.com/" + path, headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def text(x, y, value, size=13, color="#d8d4eb", extra=""):
    return (
        f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" '
        f'font-size="{size}" fill="{color}" {extra}>{escape(str(value))}</text>'
    )


def card(title, content, subtitle, date):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="440" height="230" '
        f'viewBox="0 0 440 230" role="img" aria-label="{escape(title)}">'
        f'<title>{escape(title)}</title>'
        '<rect x="1" y="1" width="438" height="228" rx="14" '
        'fill="#111321" stroke="#302d48"/>'
        + text(24, 35, title, 18, "#b9a6ff", 'font-weight="600"')
        + text(24, 56, subtitle, 10, "#a99bbd")
        + content
        + '<path d="M24 197h392" stroke="#302d48"/>'
        + text(24, 216, f"UPDATED {date} / PUBLIC GITHUB DATA", 9, "#827b9d")
        + "</svg>\n"
    )


def main():
    user = api(f"users/{OWNER}")
    repos = []
    page = 1
    while True:
        batch = api(f"users/{OWNER}/repos?type=owner&per_page=100&page={page}")
        if not isinstance(batch, list):
            raise TypeError("Expected a repository list")
        repos.extend(
            repo for repo in batch
            if not repo.get("private") and not repo.get("fork")
            and repo["owner"]["login"].lower() == OWNER.lower()
        )
        if len(batch) < 100:
            break
        page += 1
    languages = Counter()
    for repo in repos:
        for language, byte_count in api(f"repos/{repo['full_name']}/languages").items():
            languages[language] += byte_count

    date = datetime.now(timezone(timedelta(hours=5))).strftime("%Y-%m-%d")
    metrics = [
        ("PUBLIC SOURCE REPOS", len(repos)),
        ("STARS EARNED", sum(r["stargazers_count"] for r in repos)),
        ("REPOSITORY FORKS", sum(r["forks_count"] for r in repos)),
        ("FOLLOWERS", user["followers"]),
    ]
    stats = ""
    for i, (label, value) in enumerate(metrics):
        x, y = (24 if i % 2 == 0 else 234), (97 if i < 2 else 155)
        stats += text(x, y, value, 29, "#8ef0d0", 'font-weight="650"')
        stats += text(x, y + 19, label, 9, "#a99bbd", 'letter-spacing=".5"')

    rows = languages.most_common(5)
    total = sum(languages.values())
    language_body = ""
    palette = ["#b9a6ff", "#8ef0d0", "#86c7ec", "#dfafd7", "#e2cd96"]
    for i, (language, count) in enumerate(rows):
        y = 82 + i * 23
        percent = count / total * 100
        language_body += text(24, y, language, 11)
        language_body += text(410, y, f"{percent:.1f}%", 10, palette[i], 'text-anchor="end"')
        language_body += f'<rect x="145" y="{y-7}" width="200" height="6" rx="3" fill="#242239"/>'
        language_body += f'<rect x="145" y="{y-7}" width="{200*count/total:.2f}" height="6" rx="3" fill="{palette[i]}"/>'
    if not rows:
        language_body = text(24, 115, "No language data yet.", 14)

    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    (assets / "github-stats.svg").write_text(
        card("My GitHub signals", stats, f"@{OWNER} / owned public repositories, excluding forks", date),
        encoding="utf-8",
    )
    (assets / "top-languages.svg").write_text(
        card("Languages in my repos", language_body, "Share of code bytes / top 5 languages / excludes forks", date),
        encoding="utf-8",
    )
    print(f"Updated cards: {len(repos)} public source repositories; {len(languages)} languages.")


if __name__ == "__main__":
    main()
