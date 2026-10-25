# ChemSpace: Interactive 3D Chemistry Workstation & Quantum Lab

[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-00F0FF?style=for-the-badge)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20Build-00FF9D?style=for-the-badge)](index.html)
[![Web Audio API](https://img.shields.io/badge/Sound-Web%20Audio%20Synth-38BDF8?style=for-the-badge)](index.html)

A next-generation interactive chemistry workstation and quantum simulation environment: dynamic 3D subatomic particle reactor, real-time periodic table telemetry, Slater's rules effective nuclear charge calculations, Aufbau anomalous electron configurations, quantum wavefunctions, molecular orbitals, SMILES-to-3D distance-geometry virtual lab, cheminformatics descriptors, interactive quizzes, and instant client-side PDF report exports.

Built with pure vanilla web technologies: single self-contained `index.html` with **zero build step, zero bundlers, and zero server-side tracking**.

---

## Highlights & Features

### 1. 3D Subatomic Scroll Reactor Canvas
- **Perspective 3D Engine:** Real-time 3D rotation math projecting a central nuclear cluster of protons and neutrons connected by dynamic covalent springs.
- **Precessing Quantum Orbitals:** 4 interlocking 3D orbital rings with high-velocity wave-packet electrons racing across tilted coordinate planes.
- **Relativistic Scroll Warp:** High scroll velocity stretches the surrounding celestial starfield into relativistic warp streaks.
- **Quantum Shockwaves & Laser HUD:** Expanding shockwave wavefronts trigger on section crossings, synchronized with a real-time top laser progress beam and telemetry module HUD.

### 2. Synthesized Web Audio API Acoustic Engine
- **Element Resonant Frequencies:** Every single one of the 118 elements synthesizes an acoustic harmonic tone derived from its atomic number $Z$:
  $$f(Z) = 160 + (Z \times 7.5)\text{ Hz}$$
- **Interactive Audio Feedback:** Acoustic click pulses and quantum warp frequency ramps accompany module navigation and chemical analyses. Can be toggled on/off instantly via the navigation bar.

### 3. Comprehensive Chemistry Intelligence Modules

| Module | Features & Capabilities |
|---|---|
| **Periodic Table** | Complete 118-element dynamic grid; color-coded by chemical family, electronegativity, atomic radius, first ionization energy, or valence block. |
| **Periodic Trends** | Real-time SVG gradient trend curves tracking $r$, $IE$, $\chi$, and Slater $Z_{\text{eff}}$ across periods and groups. |
| **$Z_{\text{eff}}$ Calculator** | Automated Slater's shielding rules calculation worked out step by step for any element and occupied orbital. |
| **Electron Config** | Aufbau filling, Pauli exclusion principle, and Hund's rule orbital diagrams with all 20 real-world anomalous exceptions detailed. |
| **3D Molecular Lab** | SMILES parser $\rightarrow$ implicit hydrogen assignment $\rightarrow$ VSEPR distance-geometry relaxation $\rightarrow$ interactive 3D viewer. |
| **Quantum Wavefunctions** | Particle-in-a-1D-box eigenstates and hydrogen atom radial distribution $r^2 R^2(r)$ with angular spherical harmonic cross-sections. |
| **MO & Hückel Theory** | Diatomic LCAO molecular orbital diagrams (bond order, magnetism, Hund filling) and cyclic/linear Hückel $\pi$-electron systems (Frost circle). |
| **Cheminformatics** | SMILES grammar reference, Lipinski Rule of 5 drug-likeness evaluation, topological polar surface area (TPSA), and an in-browser logistic-regression toxicity classifier. |
| **Practical Calculations** | EDTA complexometric water hardness and Mohr's argentometric chloride determination with burette volume inputs. |
| **Quiz & Report Export** | 15-question chemistry evaluation that stamps your session results into a downloadable PDF report with verification metadata. |

---

## Architecture & Design Principles

- **Zero-Vibe Coding Aesthetics:** Engineered strictly adhering to modern UI craftsmanship—eliminated generic purple/pink gradients, discarded pill buttons in favor of sleek industrial 6px/8px radii, and replaced placeholder copy with rigorous scientific equations.
- **100% Client-Side Ephemeral Security:** No external telemetry, tracking cookies, or remote databases. All Slater matrices, SMILES relaxations, and PDF documents are generated in browser memory.
- **Instant Deployment:** Zero node modules, zero build pipelines. Served as a pure static site on Vercel or any static file host.

---

## Running Locally

Clone the repository and serve with any local HTTP server:

```bash
# Clone the repository
git clone git@github.com:Tomoya0086/Chemistry-virtual-lab.git
cd Chemistry-virtual-lab

# Option 1: Python 3
python3 -m http.server 3000

# Option 2: Node.js (npx serve)
npx serve -l 3000
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## Deploy to Vercel

### Option 1: GitHub Integration (Recommended)
1. Push your changes to GitHub (`git push origin main`).
2. Go to [vercel.com/new](https://vercel.com/new), select **Chemistry-virtual-lab**, and click **Deploy**.
3. Vercel automatically deploys `index.html` as a high-speed Edge static site.

### Option 2: Vercel CLI
```bash
npm i -g vercel
vercel --prod
```

---

## Third-Party Libraries
- [3Dmol.js](https://3dmol.csb.pitt.edu/) — WebGL molecular visualization (loaded asynchronously from CDN with automatic 2D SVG fallback).
- [jsPDF](https://github.com/parallax/jsPDF) — Client-side vector PDF document generation.

---

## License
Open-source under the [MIT License](LICENSE).
