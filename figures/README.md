# figures/ — report visuals (small PNGs tracked; raw Blender/.blend NOT tracked)

- `figures_Figure3_system.png` — Figure 3 system diagram (team-made).
- `Figure5_MIZAN_CFD_validation.png` — Figure 5 (SIMULATED): 4-panel CFD validation
  from REAL OpenFOAM sample sets (no ParaView: plotted from
  `mizan02/postProcessing/sample/1500/p0..p6.xy` via Python).
  (a) salinity traverse profiles per station; (b) CoV vs x/D with 0.05 threshold;
  (c) mass check area- vs flux-averaged means vs 51.67 theory;
  (d) residuals vs iteration. Generator: `scienetist/fig5_validation.py`.
  Note: planes are y-traverses (−5…+5 mm, 101 pts) at x = 0/1/2/3/5/10/15D
  (see `mizan02/system/sampleDict`), NOT full cross-sections.
- `Figure6_bench_rig.png` — Figure 6 (PROPOSED): bench validation rig schematic
  (tanks, pumps, flowmeters, Y + needle inlet, DN10 6-fin mixer, EC probe,
  controls + pass criteria). Generator: `scienetist/fig6_rig.py`.
- Figure 4 (missing — TEAM TODO): lab mixer + Venturi CAD renders. Export via
  Blender F12 (1920×1080, Cycles), never viewport screenshots. Caption: team CAD
  geometry; CFD setup Sec 6 / results Fig 5.
- Figure rules: numbered, captioned, legible in print/B&W, cited if not ours.
  No clipped content, no missing-glyph boxes. SIMULATED / ESTIMATED / PROPOSED
  labels mandatory.
