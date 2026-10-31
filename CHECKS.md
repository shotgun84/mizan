# CHECKS — dated validation log (append, never rewrite history)

## 2026-10-30 — repo foundation + verification (assistant-assisted, team to review)
- `calculations/reproduce.py` run from repo root AND from `calculations/` — SELF-CHECK PASS.
  Reproduced: S1 60.83; finals 56.25/53.5/51.67; 0.43 MW; 10,320 kWh/d; 3,766.8 MWh/yr;
  AED 1,657,392/yr (≈1.66M); 0.0190 kWh + AED 0.0084 per m³ brine;
  Taweelah ×2.31 → 0.99 MW, ≈AED 10,454/day (≈10,500 as reported). Matches report §7.
- STL edge audit (Python, exact counts): Static mixer.stl 3416 facets, 0 bad edges (watertight ✓).
  Venturi throat.stl 59518 facets, 96 boundary + 15799 non-manifold edges (NOT watertight — repair before print).
- CFD reading (`mizan02/`): OpenFOAM 14, `foamRun -solver incompressibleFluid`, RAS kOmegaSST,
  SIMPLE tol 1e-5, snappyHexMesh workflow (cellLevel/pointLevel present). `system/` + `constant/`
  + `postProcessing/` (residuals + 7 sample planes p0–p6 @1500) + `VTK/` all present after upload
  finished (polyMesh 147 MB + VTK 153 MB excluded from git as regenerable; triSurface STL kept).
- `0/C` (verbatim): internalField 51.67; seaInlet codedFixedValue (70 core r<2 mm, else 42.5);
  outlet/mixer zeroGradient. Interpretation of core + plane stations: OPEN (see docs/OPEN_QUESTIONS.md).
- Run completed `End` at Time=1500 s (~4460 s CPU); finals U~5–9e-4, p~2e-4, C~1.1e-3, k/omega ~1e-9/1e-6.
- cov.txt transcribed verbatim into `cfd/STATIC_MIXER.md` (CoV 0.0084 @15D beats <0.05 target;
  10D/15D means sit ~10% below CT=51.67 — interpretation OPEN).
- Missing confirmed: checkMesh log + mesh count, mesh-independence evidence, Fig 5 contour PNGs,
  Fig 4 renders, eductor CFD, tank data, advisor signature, industry mentor row, video link.
- Bytes kept out of git by `.gitignore`: 869 time dirs + polyMesh + VTK + dynamicCode (~8 GB raw).
  Tracked instead: system dicts, small constant files, triSurface STL, 0/ fields, postProcessing
  sets + residuals, logs excerpts, manifest, inputs + reproduce script.
