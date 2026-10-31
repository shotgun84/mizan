# CFD — static mixer run (SIMULATED, team run Sep 2026, host ImranAsus)

## Setup (extracted verbatim from case files 2026-10-30 — no invention)
- OpenFOAM 14, `foamRun -solver incompressibleFluid` (`Allrun`: blockMesh → snappyHexMesh -overwrite → checkMesh), single process.
- `system/controlDict`: endTime 1500, deltaT 1, writeInterval 500, purgeWrite 0.
- `system/fvSolution`: p = GAMG (tol 1e-6, relTol 0.1); U/k/omega/C = smoothSolver symGaussSeidel (tol 1e-5, relTol 0.1).
- Turbulence: RAS kOmegaSST. Viscosity model: constant (`log.foamRun` header).
- Mesh: snappyHexMesh (`cellLevel`/`pointLevel` in `0/`, triSurface STL in `constant/`, `snappyHexMeshDict` + `blockMeshDict` in `system/`). Cell count + checkMesh log: MISSING — add before claiming mesh quality.
- Inlet (`0/C`, verbatim): `internalField uniform 51.67`; `seaInlet` = codedFixedValue 42.5 with inline code setting 70 where `r<0.002` (2 mm core) else 42.5; `outlet` + `mixer` walls = zeroGradient. Meaning of the 2 mm core vs the physical inlet: TEAM TO CONFIRM (do not assert geometry).
- Sampling: `system/sampleDict` + `functions` present; sets land in `postProcessing/sample/1500/p0..p6.xy` (7 planes).
- Run completed: `End` at Time = 1500 s, ~4460 s CPU. Final residuals U ~4–9e-4, p ~2e-4, C ~1.1e-3, k/omega ~1e-9/1e-6 (0 iterations at end), continuity global ~0.0035. Full log: `mizan02/log.foamRun` (local only).

## Results (`mizan02/cov.txt`, target CT = 51.67 per `post_cov.py`)
| plane | Cbar (ppt) | CoV | MI=1-CoV | mean err vs 51.67 |
|---|---|---|---|---|
| x=0D | 52.48 | 0.2069 | 0.7931 | +1.58% |
| x=1D | 52.41 | 0.2063 | 0.7937 | +1.43% |
| x=2D | 52.34 | 0.2059 | 0.7941 | +1.29% |
| x=3D | 52.27 | 0.2055 | 0.7945 | +1.17% |
| x=5D | 52.17 | 0.2046 | 0.7954 | +0.96% |
| x=10D | 45.82 | 0.0342 | 0.9658 | −11.32% |
| x=15D | 46.68 | 0.0084 | 0.9916 | −9.66% |
| dP = 8.5 Pa, K = 0.01 (as recorded in file) | | | | |

Reading (careful, literal): uniformity target CoV < 0.05 is met at x=10D (0.034) and x=15D (0.0084). Plane means at 10D/15D sit ~10% below the 51.67 target while 0–5D planes sit ~+1–1.5% above it. Do NOT explain this shift in the report without confirmed plane locations, sampled geometry and inlet conditions — record the team-confirmed interpretation in Section 6.5/Appendix B first.

## TODO (blocks Fig 5 + Appendix B)
1. checkMesh log + mesh cell count + mesh-independence evidence (2× refinement or documented rationale).
2. Contour PNGs for Report Fig 5 (ParaView from `case.foam`; label SIMULATED + setup ref).
3. Confirm: meaning of "D", plane positions, inlet split modelled, why means shift at 10D/15D.
4. Eductor CFD: not started (throat CAD exists in repo root).
