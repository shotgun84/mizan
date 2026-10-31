# MIZAN-02 — Team OATSZ Engineering Repository (CMAT-00114)

Team repository for the Global Water Hackathon 2026 Final Report, Theme 1
(Water Security and Sustainable Desalination).
Use this link in Report §5.6 as the access link (repository). Make it public
(or anyone-with-link) before submission; keep available until ≥ 31 Dec 2026.

## Layout (what lives where)

| Path | Contents | Tracked in git? |
|---|---|---|
| `Static mixer.stl`, `Venturi throat.stl` | As-received CAD exports (DO NOT overwrite) | Yes (small) |
| `cad/` | STL documentation, print notes, generator provenance | Yes |
| `cfd/` | Setup + results notes for the static-mixer OpenFOAM run | Yes |
| `mizan02/` | Raw OpenFOAM case: 869 time dirs, logs, `cov.txt`, `post_cov.py` | **No — local/Drive only (see 8 GB policy below)** |
| `calculations/` | Inputs + reproduce script for every headline number | Yes |
| `docs/` | Assumptions, open questions, tank-test matrix, calibration sheet | Yes |
| `figures/` | Report figures (Fig 3 system diagram in repo; renders + CFD contour to be added) | Yes (small PNGs) |
| `references.bib` | Verified references only | Yes |
| `MANIFEST.md`, `CHECKS.md` | Inventory + dated validation log | Yes |

## Status (honest, 2026-10-30)

- Static mixer: CAD done (STL watertight ✓), CFD done (OpenFOAM 14, kOmegaSST, ran to 1500 s, CoV 0.0084 at x=15D — see `cfd/`) — SIMULATED. Setup dicts present; mesh-independence + contour PNGs still open.
- Venturi throat + mixing tube + diffuser: CAD done (STL needs repair, see `cad/`). Eductor CFD: NOT done.
- Offshore pipe: straight pipe — 1D friction only, no CFD needed (standard practice).
- Tank test / field data: NOT done. Overall TRL 3 (see docs).
- `system/` + `constant/` (minus regenerable `polyMesh/`) + `postProcessing/` sets ARE in `mizan2/` and tracked — small text/CSV only. Raw fields stay local.

## 8 GB raw-data policy (important)

`mizan02/` holds ~8 GB of time-step fields across 869 time directories.
Do NOT commit it to git (GitHub hard limit: 100 MB/file; practical repo limit far below 8 GB).
It is excluded in `.gitignore`. Keep ONE authoritative copy (this disk + a backup),
and put the public dataset link (Drive/OSF/Zenodo) here once uploaded:

- Full dataset link: [ADD link — must work without sign-in, keep until ≥ 31 Dec 2026]
- What is in the repo instead: solver setup notes, `cov.txt` results table, log excerpts,
  post-processing script reference, mesh-independence statement (once run), contour PNGs.

## Quickstart (reproduce every headline number)

```
python calculations/reproduce.py   # run from repo root OR from calculations/
```
Expected: S1 60.83 → 53.5/51.67; 0.43 MW; 10,320 kWh/d; 3,766.8 MWh/yr; AED 1,657,392 (≈1.66M);
0.0190 kWh + AED 0.0084 per m³ brine; Taweelah ×2.31 → 0.99 MW, ≈AED 10,454/day (≈10,500 as reported).
Full derivation: Appendix A of the report + `calculations/inputs.yaml`.
