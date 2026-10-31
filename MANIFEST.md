# MANIFEST — measured inventory (2026-10-30, local inspection, no invention)

## CAD exports (repo root, KEEP — do not overwrite; repaired copies get new names)
- `Static mixer.stl` — 0.2 MB, binary, 3416 facets, bbox X[-27,27] Y[0,250] Z[-27,27] (~54 dia × 250 long; axis = Y). Edge audit: 0 bad edges → **watertight manifold ✓ print-ready**. Units implicit (confirm mm in slicer).
- `Venturi throat.stl` — 2.8 MB, binary, 59518 facets, bbox X[-0.1,0.1] Y[-0.1,0.1] Z[-0.1,0.0] (0.2 × 0.2 × 0.1 file units → likely metres = 200 dia × 100 long; axis = Z). Edge audit: 96 boundary + 15799 non-manifold edges → **NOT watertight as-exported** (internal intersecting shells + small open ring). Action: repair in Blender (3D-Print Toolbox), save as `Venturi throat_repaired.stl`, keep original untouched. NOTE: unit convention differs between the two STLs — confirm scale before printing/slicing together.

## CFD raw (`mizan02/`, upload complete for setup + results; raw fields local/Drive only)
- 869 time directories (transient fields) + `Allrun` (blockMesh → snappyHexMesh -overwrite → checkMesh → `foamRun -solver incompressibleFluid`).
- `system/` PRESENT: controlDict (endTime 1500, deltaT 1, writeInterval 500), controlDict.full, functions, fvSchemes, fvSolution (GAMG p tol 1e-6; smoothSolver U/k/omega/C tol 1e-5), sample, sampleDict, snappyHexMeshDict, blockMeshDict.
- `constant/` PRESENT except `polyMesh/` (147 MB — excluded from git as regenerable): triSurface STL (3.3 MB, tracked), momentumTransport/transport/turbulenceProperties, `0/` fields (C, U, p, k, omega, nut + cellLevel/pointLevel — snappy evidence), `dynamicCode/cInlet` (coded inlet BC build).
- `0/C`: internalField uniform 51.67; seaInlet = codedFixedValue (core 70 ppt within r<2 mm, 42.5 outside — VERBATIM from file, interpretation open); outlet + mixer walls zeroGradient.
- `postProcessing/` PRESENT + tracked (small): `residuals/0/residuals.dat` (155 KB) + `sample/1500/p0..p6.xy` (7 planes × 8.2 KB — the sets behind `cov.txt`). `log.foamRun` (1.3 MB): run completed `End` at Time=1500 s, ~4460 s CPU; final residuals U~5–9e-4, p~2e-4, C~1.1e-3, k/omega ~1e-9/1e-6; continuity global ~0.0035. Root sampling logs (`log.sample*`) are 0 bytes — the real sets are the postProcessing files above.
- `VTK/` PRESENT (153 MB: mizan02_1500 + mixer/outlet/seaInlet surfaces) — excluded from git (regenerable); export Fig 5 contour PNGs from ParaView (`case.foam`) into `figures/`.
- MISSING (needed for Appendix B + Fig 5): checkMesh log + mesh cell count, mesh-independence evidence, contour PNGs, eductor CFD (not started), tank data.

## Generator scripts (Blender, in `F:\PythonScripts\scienetist\`, NOT copied here to avoid divergence)
- Provenance of the two STLs is UNCONFIRMED — team: record which script+commit/export settings produced each STL in `cad/README.md`.
