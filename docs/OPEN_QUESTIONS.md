# Open questions (answer in order; each blocks the item noted)

1. [CFD] What are the plane locations behind x=0D…15D in cov.txt, and what geometry/inlets did the run model? (Blocks Sec 6 results text + Fig 5 caption.)
2. [CFD — PARTLY ANSWERED 30 Oct] Setup dicts recovered (`system/`, `constant/` minus regenerable `polyMesh/`). Still open: mesh cell count + checkMesh log, mesh-independence evidence, contour PNGs (Fig 5), interpretation of x=0D…15D stations and the 10D/15D mean shift. Eductor CFD: not started.
3. [CFD] Why do plane means shift 52.4 → ~46 at 10D/15D while target is 51.67? Confirm expected physics before writing the interpretation sentence.
4. [CFD] Mesh-independence evidence (2x refinement or documented rationale)? (Blocks "validated" language.)
5. [PLANT] Real outfall: flow, salinity, pressure after ERD, bathymetry, currents, STP distance? (Blocks site-specific claims, intake design, TRL 5+.)
6. [VENTURI] Throat CFD + diffuser CAD still pending — schedule before pilot. (Blocks Sec 5.4/6.4 completion.)
7. [RIG] Tank, pumps, EC probes, budget decided? Fill TEST_MATRIX + calibration sheet, then build.
8. [REPORT] Contour PNGs for Fig 5 (ParaView from case.foam) + render PNG for Fig 4 (Blender F12) — export, don't screenshot viewports.
9. [ADMIN] Repo public link; advisor signature; industry mentor row (or "none appointed"); video link + subtitles.
