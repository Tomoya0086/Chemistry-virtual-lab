# 🧪 Cheminformatics Virtual Laboratory & 3D Molecular Workstation
### SRM Institute of Science and Technology, Tiruchirappalli
**Faculty of Engineering and Technology | School of Sciences | Division of Chemistry**

[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://chemistry-virtual-lab-xi.vercel.app)
[![Python Engine](https://img.shields.io/badge/Engine-Python%203.14%20Serverless-38BDF8?style=for-the-badge&logo=python&logoColor=white)](api/index.py)
[![License: Academic](https://img.shields.io/badge/License-Academic%20Fair--Use-00FF9D?style=for-the-badge)](index.html)
[![Zero Build Pipeline](https://img.shields.io/badge/Build-Zero%20Bundler%20Static-00F0FF?style=for-the-badge)](index.html)

A next-generation interactive Cheminformatics Virtual Laboratory and 3D molecular simulation workstation developed for the Division of Chemistry at **SRM Institute of Science and Technology, Tiruchirappalli**, in technical collaboration with **Tomoya Okazaki**.

---

## 🏛️ Academic Leadership & Technical Credits

* **Curriculum Design & Academic Supervision:**  
  **Dr. R. Subramanian**, Assistant Professor  
  Division of Chemistry, School of Sciences, Faculty of Engineering and Technology  
  SRM Institute of Science and Technology, Tiruchirappalli  
  📧 Email: [rsmani84@gmail.com](mailto:rsmani84@gmail.com)

* **Systems Architecture & Kinetic Engineering:**  
  **Tomoya Okazaki**  
  Purple Team Cybersecurity & Interactive Simulation Architecture  
  📧 Email: [khalidnawaz7y@gmail.com](mailto:khalidnawaz7y@gmail.com)  
  🛡️ TryHackMe: [Tomoya.okazaki](https://tryhackme.com/p/Tomoya.okazaki) | HackTheBox: [01a0be6e](https://profile.hackthebox.com/profile/01a0be6e-b00a-7335-9ff0-5864ad467519) | LinkedIn: [khalidnawaz-sec](https://www.linkedin.com/in/khalidnawaz-sec)

---

## 🚀 Key Modules & Capabilities

### 1. Interactive 2D & 3D Molecular Simulation
* **SMILES Parser & Coordinate Embedder:** Real-time conversion of SMILES strings (`CCO`, `c1ccccc1`, `CC(=O)Oc1ccccc1C(=O)O`, etc.) into 2D chemical connectivity vectors and 3D WebGL geometries.
* **Hardware-Accelerated 3D Models:** Ball and Stick, Stick Model, Space Filling (CPK), Wireframe, and Cartoon Ribbon representations with van der Waals (vdW) surface mesh overlay.
* **Interactive Controls:** Mouse rotation, mouse wheel zoom, 3D panning, and automated gyroscopic spin.

### 2. Complete 18-Descriptor Analytical Suite
Evaluates comprehensive physicochemical and structural descriptors:
1. **Molecular Formula** (Standard Hill notation)
2. **Molecular Weight** (Average isotopic mass)
3. **Exact Molecular Weight** (Monoisotopic mass for high-res MS)
4. **LogP** (Wildman-Crippen lipophilicity octanol-water partition coefficient)
5. **TPSA** (Topological Polar Surface Area in Å²)
6. **Hydrogen Bond Donors** (Lipinski Rule of 5 donor sites)
7. **Hydrogen Bond Acceptors** (Electronegative N/O heteroatoms)
8. **Rotatable Bonds** (Conformational flexibility index)
9. **Total Ring Count**
10. **Aromatic Rings** (Hückel $4n+2$ planar conjugated systems)
11. **Aliphatic Rings**
12. **Number of Atoms**
13. **Heavy Atoms**
14. **Heavy Atom Bonds**
15. **Sigma ($\sigma$) Bonds** (Localized framework bonds including implicit H)
16. **Pi ($\pi$) Bonds** (Multiple bonds and aromatic delocalization)
17. **Fraction Csp3** (Ratio of sp³ carbons to total carbons)
18. **Molar Refractivity** (Steric volume and electronic polarizability)

### 3. Student Assessment & PDF Report Generation
* **Interactive 5-Question Evaluator:** Evaluates knowledge on SMILES grammar, Lipinski's Rule of 5, TPSA, and bonding theory with instant feedback.
* **Certified Laboratory Report:** One-click client-side export to downloadable PDF with student name, registration number, evaluation metrics, and institutional verification block.

### 4. Quantum Foundations & Periodic Intelligence
* **118-Element Dynamic Grid:** Complete periodic table with acoustic resonant tones synthesized via the Web Audio API.
* **Slater's Effective Nuclear Charge ($Z_{\text{eff}}$):** Step-by-step screening constant calculation for any element and subshell.

---

## ⚡ Kinetic Motion & Zero-Vibe Design Principles

1. **Momentum Inertial Scrolling:** Custom mathematical velocity scroller providing fluid, weighted scroll physics.
2. **Scroll-Driven 3D Perspective:** Cards and telemetry modules enter the viewport with kinetic tilt (`rotateX`, `skewY`, `scale`) and staggered child delays (0.08s - 0.25s).
3. **Button Hover Dynamics:** Micro-displacement (-3px), light sheen diagonal sweep, and neon electric cyan glow.
4. **Zero-Vibe Anti-Patterns:**
   * ❌ Zero purple/pink gradients
   * ❌ Zero 999px pill buttons (industrial 6px/8px radii)
   * ❌ Zero fake reviews or fake metrics
   * ❌ Zero emoji icons (crisp inline SVG vectors)
   * ❌ Zero em dashes
   * ✅ Favicon, meta descriptions, mobile responsive drawer, 404 recovery modal, privacy and terms compliance.

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
Open [http://localhost:3000](http://localhost:3000) in your browser.

### Option 2: Node.js (npx serve)
```bash
npx serve -l 3000
```

---

## ☁️ Deploying to Vercel

The repository is configured for instantaneous deployment to Vercel with zero build configuration:
1. Push changes to GitHub: `git push origin main`.
2. Connect the repository in the Vercel dashboard.
3. Vercel automatically deploys `index.html` at the edge and routes `/api/*` to the serverless Python handler `api/index.py`.

Live deployment: [chemistry-virtual-lab-xi.vercel.app](https://chemistry-virtual-lab-xi.vercel.app)

---

## 📜 License
Educational and academic fair-use license. Division of Chemistry, SRM Institute of Science and Technology.
