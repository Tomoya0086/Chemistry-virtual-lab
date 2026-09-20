# ChemSpace

An interactive chemistry workstation: periodic table, effective nuclear charge with Slater's
rules, electron configurations, quantum wavefunctions, molecular orbitals, a SMILES-to-3D
virtual lab, cheminformatics descriptors, quizzes and a downloadable PDF report.

The front end is a single self-contained `index.html` — no build step, no bundler.
`api/chem.py` is an optional Python serverless function exposing the same chemistry
calculations as a JSON API.

## Modules

| Section | What it does |
|---|---|
| Periodic Table | All 118 elements, recolour by family / electronegativity / radius / ionisation energy / block |
| Trends | Interactive plots of radius, IE, electronegativity and Slater Z_eff across periods and groups |
| Z_eff | Slater's rules worked out step by step for any element and any occupied orbital |
| Configuration | Aufbau, Pauli and Hund with all 20 real anomalies explained |
| Virtual Lab | SMILES parser → implicit hydrogens → VSEPR distance-geometry embedding → 3D viewer |
| Quantum | Particle in a 1-D box; hydrogen radial and angular wavefunctions |
| MO & Hückel | Diatomic MO diagrams with bond order and magnetism; Hückel π systems (butadiene, benzene) |
| Cheminformatics | SMILES reference, molecular descriptors, Lipinski rule of five, a logistic-regression demo classifier |
| Practicals | EDTA complexometric hardness and Mohr's chloride determination |
| Quiz & Report | 15-question bank, and a PDF export stamped with your name and register number |

## Deploy to Vercel

### Option A — GitHub (recommended)

```bash
git init
git add .
git commit -m "ChemSpace"
git branch -M main
git remote add origin https://github.com/<you>/chemspace.git
git push -u origin main
```

Then go to [vercel.com/new](https://vercel.com/new), import the repository and press **Deploy**.
Leave every build setting empty — Vercel serves `index.html` as a static site and detects
`api/chem.py` as a Python function automatically. No environment variables are needed.

### Option B — Vercel CLI

```bash
npm i -g vercel
vercel          # preview deployment
vercel --prod   # production
```

## Run locally

```bash
python3 -m http.server 3000        # front end  → http://localhost:3000
python3 api/chem.py                # API        → http://localhost:8000/api/chem?op=zeff&z=11
```

## API

Once deployed, `https://<your-app>.vercel.app/api/chem` accepts:

| Query | Returns |
|---|---|
| `?op=elements` | Symbol, atomic number and block for all 118 elements |
| `?op=config&z=24` | Configuration, condensed form, orbital diagram, anomaly flag |
| `?op=zeff&z=11&orbital=3s` | Screening constant, Z_eff and the full Slater step table |
| `?op=huckel&kind=ring&n=6` | Hückel π energies, occupancies, delocalisation energy, aromaticity |
| `?op=pib&n=1&length=1.0` | Particle-in-a-box energy levels in eV |

Example:

```bash
curl "https://<your-app>.vercel.app/api/chem?op=zeff&z=11&orbital=3s"
```

```json
{ "screening_constant": 8.8, "zeff": 2.2, "...": "..." }
```

## Notes and limits

- 3D geometries come from covalent radii and VSEPR angles relaxed by distance geometry.
  They are correct for connectivity and shape, not for precise bond lengths or stereochemistry.
- The SMILES parser handles branches, ring closures, aromatic lowercase atoms, bracket atoms,
  charges and explicit hydrogen counts. It ignores stereo descriptors (`@`, `/`, `\`).
- cLogP and TPSA are simple additive estimates for teaching, not RDKit-quality values.
- The toxicity classifier is a demonstration of how a QSAR model is built from 18 labelled
  molecules. It is not validated and must not be used to assess any real chemical.
- Radii and ionisation energies for the superheavy elements are predicted values.

## Third-party libraries

Loaded from CDN at runtime: [3Dmol.js](https://3dmol.csb.pitt.edu/) for the molecular viewer
and [jsPDF](https://github.com/parallax/jsPDF) for the report. Both have graceful fallbacks.

## Licence

MIT.
