<!-- Profile content reviewed against lsimg's public repository READMEs and source files. -->
<div align="center">
  <img src="./assets/header.svg" width="100%" alt="GULSIM — AI · Computer Vision · Robotics. Building ideas into reality." />
  <br /><br />
  <a href="#about-me">about</a> &nbsp; · &nbsp;
  <a href="#featured-projects">featured</a> &nbsp; · &nbsp;
  <a href="#project-constellation">projects</a> &nbsp; · &nbsp;
  <a href="#tech-stack">toolbox</a> &nbsp; · &nbsp;
  <a href="#github-signals">activity</a>
  <br /><br />
  <samp>curiosity → experiments → things you can interact with</samp>
</div>

<br />

<a id="about-me"></a>
<img src="./assets/about.svg" width="100%" alt="About me" />

I'm **Gulsim**, a student developer at **NIS Taldykorgan**. I build gesture-controlled interfaces, educational 3D tools, machine learning experiments, and web prototypes.

My projects explore how machines **see**, how software **responds to people**, and how data can support practical decisions — from satellite telemetry to agriculture in Kazakhstan.

I'm also the **head of software engineering for Team TDKwarriors**, working on an autonomous vehicle for **WRO Future Engineers 2026**.

<p>
  <a href="https://github.com/lsimg/Lumen"><img src="https://img.shields.io/badge/currently_building-LUMEN-b9a6ff?style=flat-square&amp;labelColor=1b1930" alt="Currently building Lumen" /></a>
  &nbsp;
  <a href="https://github.com/lsimg/TDKwarriors"><img src="https://img.shields.io/badge/robotics-TDKwarriors-8ef0d0?style=flat-square&amp;labelColor=1b1930" alt="Robotics: Team TDKwarriors" /></a>
</p>

<br />

<a id="featured-projects"></a>
<img src="./assets/project.svg" width="100%" alt="Featured projects" />

<a href="https://github.com/lsimg/Lumen">
  <img src="./assets/lumen.svg" width="100%" alt="Lumen — gesture-controlled educational 3D platform with Jeremy, an optional contextual voice assistant" />
</a>

**[Lumen](https://github.com/lsimg/Lumen)** brings four learning paths into one interactive 3D application: **robotics**, **computer components**, **human anatomy**, and **interactive learning for children**.

- **Explore with your hands:** point at parts, pinch to select, move with an open palm, rotate with a V gesture, and scale with two hands.
- **Learn by interacting:** inspect component descriptions, manipulate robot joints, and play fruit-matching and size-matching activities.
- **Ask Jeremy:** an optional voice assistant uses the current model, selected part, and application state as context. Wake-word detection, speech recognition, and speech synthesis run locally; generated answers use OpenRouter.

<samp>Python · OpenCV · MediaPipe · ModernGL · Trimesh · Vosk · PyTorch/Silero</samp>

<br /><br />

<p align="center">
  <a href="https://github.com/lsimg/Astroguard.v2"><img src="./assets/astroguard.svg" width="49%" alt="AstroGuard v2 — adaptive autoencoders, telemetry anomaly detection, FFT analysis and remaining-life estimation" /></a>
  <a href="https://github.com/lsimg/TDKwarriors"><img src="./assets/tdkwarriors.svg" width="49%" alt="TDKwarriors — autonomous robot vehicle software for WRO Future Engineers 2026" /></a>
</p>

**[AstroGuard v2](https://github.com/lsimg/Astroguard.v2)** — a telemetry research application with a PyTorch autoencoder, automated architecture search, FFT analysis, and remaining useful life estimation. Its loader supports NASA IMS, SMAP/MSL, CSV, and NumPy data, with a Streamlit monitoring interface.

**[TDKwarriors](https://github.com/lsimg/TDKwarriors)** — a team robotics project for WRO Future Engineers 2026. My role focuses on software: Pybricks control, sensor-based navigation, odometry, and steering. The repository also documents the OpenMV–Arduino–Technic Hub architecture and the vehicle's mechanical evolution.

<br />

<a id="project-constellation"></a>
<img src="./assets/projects.svg" width="100%" alt="Project constellation" />

<p align="center"><samp>more experiments from my public repositories</samp></p>

### Vision & gesture interfaces

| Project | What it does | Built with |
| :--- | :--- | :--- |
| **[Mediapipe_Draw](https://github.com/lsimg/Mediapipe_Draw)** | An air-drawing app: draw with an index finger, choose colors with two fingers, erase with a fist, and save drawings as PNG. Includes asynchronous tracking and adaptive smoothing. | Python · OpenCV · MediaPipe · NumPy |
| **[Mouse_Move](https://github.com/lsimg/Mouse_Move)** | A webcam-controlled virtual mouse for Windows. Hand gestures move the pointer, click, double-click, scroll, and pause control, with cursor smoothing and gesture debouncing. | Python · MediaPipe · OpenCV · PyAutoGUI |
| **[two-hand-image-zoom](https://github.com/lsimg/two-hand-image-zoom)** | Resize an image by moving two raised index fingers apart or together. Includes smooth scaling, scale limits, and transparent PNG support. | Python · OpenCV · MediaPipe |

### Data & applied AI

| Project | What it does | Built with |
| :--- | :--- | :--- |
| **[AstroGuard](https://github.com/lsimg/AstroGuard)** | The earlier vibration-monitoring prototype: MLP-based anomaly scoring, FFT plots, health trends, and a Streamlit dashboard. Includes a Dockerfile. | Python · scikit-learn · SciPy · Streamlit · Docker |
| **[AyaraiBI](https://github.com/lsimg/AyaraiBI)** | An agricultural risk assistant for Kazakhstan. Combines Open-Meteo forecasts and NASA POWER climate data with rule-based risk scoring and optional AI explanations for field decisions. | Python · FastAPI · Pydantic · HTTPX · Groq/Gemini APIs |

### Web prototypes for people

| Project | What it does | Built with |
| :--- | :--- | :--- |
| **[BalaQoldau](https://github.com/lsimg/Bala-Qolda)** | A bilingual family-and-specialist support prototype: specialist discovery, child profiles, development plans, home activities, and Russian/Kazakh AAC communication cards. Includes a Groq-powered AI module with plan review and approval states. | HTML · CSS · JavaScript · Groq API · SQL/D1 |
| **[SanaTynys](https://github.com/lsimg/SANA-TYNYS)** | A browser-based prototype for tracking nicotine habits: onboarding, a progress dashboard, a journal, a calendar, short exercises, and Sana Coach. Data is stored locally; the two interface variants connect to Groq or Gemini. | HTML · CSS · JavaScript · localStorage · AI APIs |

<br />

<a id="current-focus"></a>
<img src="./assets/focus.svg" width="100%" alt="Current focus" />

| Focus | Where I'm exploring it |
| :--- | :--- |
| **Computer Vision & HCI** | Hand tracking, gesture recognition, and interaction in Lumen and my webcam experiments. |
| **Interactive education** | Exploring 3D models, robotics, anatomy, and learning through play in Lumen. |
| **Machine Learning & signals** | Telemetry anomaly detection, autoencoders, and spectral analysis in AstroGuard. |
| **Autonomous robotics** | Navigation, localization, and motor control with Team TDKwarriors. |
| **Useful AI interfaces** | Agricultural decision support, contextual voice assistance, and human-reviewed AI workflows. |

<br />

<a id="tech-stack"></a>
<img src="./assets/stack.svg" width="100%" alt="My toolbox" />

<p align="center"><samp>tools used across my repositories</samp></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-19182b?style=for-the-badge&amp;logo=python&amp;logoColor=b9a6ff" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-19182b?style=for-the-badge&amp;logo=pytorch&amp;logoColor=8ef0d0" alt="PyTorch" />
  <img src="https://img.shields.io/badge/scikit--learn-19182b?style=for-the-badge&amp;logo=scikitlearn&amp;logoColor=b9a6ff" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/NumPy-19182b?style=for-the-badge&amp;logo=numpy&amp;logoColor=8ef0d0" alt="NumPy" />
  <img src="https://img.shields.io/badge/SciPy-19182b?style=for-the-badge&amp;logo=scipy&amp;logoColor=b9a6ff" alt="SciPy" />
  <br />
  <img src="https://img.shields.io/badge/OpenCV-19182b?style=for-the-badge&amp;logo=opencv&amp;logoColor=b9a6ff" alt="OpenCV" />
  <img src="https://img.shields.io/badge/MediaPipe-19182b?style=for-the-badge&amp;logo=mediapipe&amp;logoColor=8ef0d0" alt="MediaPipe" />
  <img src="https://img.shields.io/badge/ModernGL-19182b?style=for-the-badge&amp;logo=opengl&amp;logoColor=b9a6ff" alt="ModernGL" />
  <img src="https://img.shields.io/badge/Vosk-19182b?style=for-the-badge&amp;logo=&amp;logoColor=8ef0d0" alt="Vosk" />
  <img src="https://img.shields.io/badge/Pybricks-19182b?style=for-the-badge&amp;logo=&amp;logoColor=b9a6ff" alt="Pybricks" />
  <br />
  <img src="https://img.shields.io/badge/FastAPI-19182b?style=for-the-badge&amp;logo=fastapi&amp;logoColor=b9a6ff" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Streamlit-19182b?style=for-the-badge&amp;logo=streamlit&amp;logoColor=8ef0d0" alt="Streamlit" />
  <img src="https://img.shields.io/badge/JavaScript-19182b?style=for-the-badge&amp;logo=javascript&amp;logoColor=b9a6ff" alt="JavaScript" />
  <img src="https://img.shields.io/badge/HTML5-19182b?style=for-the-badge&amp;logo=html5&amp;logoColor=8ef0d0" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS-19182b?style=for-the-badge&amp;logo=css&amp;logoColor=b9a6ff" alt="CSS" />
  <br />
  <img src="https://img.shields.io/badge/Git-19182b?style=for-the-badge&amp;logo=git&amp;logoColor=b9a6ff" alt="Git" />
  <img src="https://img.shields.io/badge/Docker-19182b?style=for-the-badge&amp;logo=docker&amp;logoColor=8ef0d0" alt="Docker" />
  <img src="https://img.shields.io/badge/Groq%20API-19182b?style=for-the-badge&amp;logo=&amp;logoColor=b9a6ff" alt="Groq API" />
  <img src="https://img.shields.io/badge/OpenRouter-19182b?style=for-the-badge&amp;logo=&amp;logoColor=8ef0d0" alt="OpenRouter" />
</p>

<br />

<a id="github-signals"></a>
<img src="./assets/stats.svg" width="100%" alt="GitHub signals" />

<p align="center">
  <a href="https://github.com/lsimg?tab=repositories">
    <img width="49%" src="./assets/github-stats.svg" alt="Gulsim's public GitHub statistics" />
  </a>
  <a href="https://github.com/lsimg?tab=repositories">
    <img width="49%" src="./assets/top-languages.svg" alt="Languages in Gulsim's public repositories" />
  </a>
</p>

<div align="center">
  <img src="./assets/robot.svg" width="180" alt="A little floating robot with mint eyes and lavender sparkles" />
  <br />
  <samp>a little bot, a lot of curiosity.</samp>
</div>

<br /><br />

<img src="./assets/activity.svg" width="100%" alt="A little progress, every day" />

<!-- GitHub Actions refreshes these visuals daily using public GitHub data. -->
<p align="center">
  <img src="./assets/github-snake.svg" width="100%" alt="Animated contribution snake for lsimg" />
</p>

<img src="./assets/footer.svg" width="100%" alt="Stay curious. Build something that matters." />
