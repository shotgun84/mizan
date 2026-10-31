# figures/ — report visuals (small PNGs tracked; raw Blender/.blend NOT tracked)

- `figures_Figure3_system.png` — Figure 3 system diagram (team-made).
- `Figure5_MIZAN_CFD_validation.png` — Figure 5 (SIMULATED, main text, 2 big panels):
  (a) salinity traverse profiles per station; (b) CoV vs x/D with 0.05 threshold.
  From REAL OpenFOAM sample sets (no ParaView: plotted from
  `mizan02/postProcessing/sample/1500/p0..p6.xy` via Python). Generator:
  `scienetist/fig5_validation.py`. Planes are y-traverses (−5…+5 mm, 101 pts)
  at x = 0/1/2/3/5/10/15D (see `mizan02/system/sampleDict`), NOT full planes.
- `FigureB1_CFD_audit.png` — Figure B1 (Appendix B audit trail): (a) mass-consistency
  check, area- vs flux-averaged means vs 51.67 theory (uniform ~−10% offset at
  10D/15D — open verification item, not a mixing defect); (b) residuals vs
  iteration (settled ~1e-2). Same generator as Fig 5.
- `Figure6_bench_rig.png` — Figure 6 (PROPOSED): bench validation rig schematic
  (tanks, pumps, flowmeters, Y + needle inlet, DN10 6-fin mixer, EC probe,
  controls + pass criteria). Generator: `scienetist/fig6_rig.py`.
- `Figure4_CAD_geometry.png` — Figure 4 (team CAD geometry): (a) MIZAN-02 mixer
  section from `mizan02/constant/triSurface/mizan_02.stl` (wall ghosted, 6 fins
  solid); (b) Venturi eductor from `Venturi throat.stl` (cutaway, translucent).
  Rendered with matplotlib 3D (no Blender on build machine — replace with F12
  Cycles renders if available). Generator: `scienetist/fig4_cad.py`.
  Caption: team CAD geometry; mixer CFD setup Sec 6 / results Fig 5;
  Venturi CFD PENDING.
- Figure rules: numbered, captioned, legible in print/B&W, cited if not ours.
  No clipped content, no missing-glyph boxes. SIMULATED / ESTIMATED / PROPOSED
  labels mandatory.
