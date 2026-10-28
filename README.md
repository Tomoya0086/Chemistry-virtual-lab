# 🧪 Cheminformatics Virtual Laboratory & 3D Molecular Workstation
### SRM Institute of Science and Technology, Tiruchirappalli
**Faculty of Engineering and Technology | School of Sciences | Division of Chemistry**

[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://chemistry-virtual-lab-xi.vercel.app)
[![Python Engine](https://img.shields.io/badge/Engine-Python%203.14%20Serverless-38BDF8?style=for-the-badge&logo=python&logoColor=white)](api/index.py)
[![License: Academic](https://img.shields.io/badge/License-Academic%20Fair--Use-00FF9D?style=for-the-badge)](index.html)
[![Zero Build Pipeline](https://img.shields.io/badge/Build-Zero%20Bundler%20Static-00F0FF?style=for-the-badge)](index.html)

A production-grade, interactive Cheminformatics Virtual Laboratory and 3D molecular workstation developed for the Division of Chemistry at **SRM Institute of Science and Technology, Tiruchirappalli**.

---

## 🏛️ Academic Leadership & Curriculum Governance

* **Curriculum Design & Academic Supervision:**  
  **Dr. R. Subramanian**, Assistant Professor  
  Division of Chemistry, School of Sciences, Faculty of Engineering and Technology  
  SRM Institute of Science and Technology, Tiruchirappalli  
  📧 Email: [rsmani84@gmail.com](mailto:rsmani84@gmail.com)

* **Student Developer & Research Implementation:**  
  **velmurgan** (Register No: `RA2611030050019`)  
  Cohort: `SRM-CHEM-101`

---

## 🚀 The 8 Interactive Laboratory Chapters

The workstation is organized into 8 synchronized curriculum chapters (numbered 01 to 08):

| Chapter | Module | Description |
|---|---|---|
| **01** | **Overview** | Institutional orientation, course objectives, and interactive lab tour. |
| **02** | **Theory** | SMILES grammar specifications, molecular graphing principles, valence rules, and spectral physics. |
| **03** | **2D & 3D Lab** | SMILES parser, JSME 2D molecular drawing canvas, and 3D WebGL renderers (Ball & Stick, Stick, Space Filling CPK, Wireframe, Cartoon Ribbon). |
| **04** | **Descriptors** | 18-descriptor analytical engine with kinetic counter animations ($0 \rightarrow 46.07\text{ g/mol}$). |
| **05** | **Matrix** | Topological atom-neighborhood circular fingerprints (ECFP4-equivalent) and Tanimoto structural similarity matrix with SAR pedagogical guidance. |
| **06** | **Assessment** | Instant evaluative quiz with zero-flash static DOM hydration, automated scoring, and cohort leaderboard registration. |
| **07** | **Reactions** | Chemical transformation engine featuring left-to-right typewriter kinetics and stoichiometry balances. |
| **08** | **Report** | Inspection queue, active molecule-to-lab loading workflow, and certified institutional PDF export with cryptographic QR verification. |

---

## ⚡ Core Engineering & Architectural Features

### 1. Pure Python 3.14 Serverless Engine (`api/index.py`)
* Fully self-contained, standard-library cheminformatics engine executing on Python 3.14 edge runtime.
* Zero heavy binary dependencies (no C-compilation failures on serverless edge).
* Strict institutional CORS whitelist restricting origins to authorized domains:
  * `http://localhost:*` & `http://127.0.0.1:*`
  * `https://*.vercel.app`
  * `https://*.srmist.edu.in`

### 2. Multi-Tier Resilient Leaderboard Persistence
* **Cloud Tier:** PostgREST integration with Supabase for permanent multi-session storage.
* **Local Disk Tier:** Automated fallback to local disk storage (`leaderboard.json` / `/tmp`).
* **Client Self-Healing:** Browser `localStorage` cache automatically synchronizes past submissions to `/api/leaderboard/sync` if a serverless cold restart occurs.
* **Faculty Cohort Guidance:** In-UI instructions guiding students: *"Get your class code from Dr. R. Subramanian (Default cohort: SRM-CHEM-101)"*.

### 3. Pedagogical Error Feedback ("Errors That Teach")
* Intelligent SMILES error parser providing diagnostic root causes (e.g., unclosed ring pairs, nitrogen valence saturation errors) with recommended corrections (e.g., *"Try CC(=O)O for acetic acid"*).

### 4. Topological Structural Similarity (ECFP4-Equivalent)
* Replaces naive string matching with radius-2 circular atom-neighborhood topological connectivity fingerprints.
* Clear visual disclaimers for pedagogical Structure-Activity Relationship (SAR) studies.

### 5. Native 120fps Kinetic Motion
* Unlocked hardware-accelerated 120fps scrolling with 300ms viewport opacity reveals.
* Count-up descriptor animations and typewriter reaction dynamics.

---

## 💻 Running Locally

### Option 1: Python Engine (Recommended)
```bash
# Clone the repository
git clone git@github.com:Tomoya0086/Chemistry-virtual-lab.git
cd Chemistry-virtual-lab

# Run the standalone Python server
python3 app.py
```
Open [http://localhost:3000](http://localhost:3000) in your web browser.

### Option 2: Node.js Static Server
```bash
npx serve -l 3000
```

---

## ☁️ Deployment

The project is pre-configured for automated Vercel deployment:
1. Pushing commits to `main` automatically triggers Vercel CI/CD.
2. Edge static assets (`index.html`, assets) are served via Vercel Global CDN.
3. Cheminformatics API endpoints (`/api/*`) are handled serverlessly by `api/index.py`.

Live Production URL: [https://chemistry-virtual-lab-xi.vercel.app](https://chemistry-virtual-lab-xi.vercel.app)

---

## 📜 Academic License & Attribution
Developed for educational use by the Division of Chemistry, School of Sciences, SRM Institute of Science and Technology, Tiruchirappalli. All rights reserved under academic fair-use licensing.
