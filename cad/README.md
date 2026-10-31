# cad/ — CAD exports + print notes

## Files (repo root)
- `Static mixer.stl` — team Autodesk export, 4-element print-trial variant (measured 54 dia × 250 long, axis Y), 3416 facets, watertight ✓. NOTE: `mixer_A_kenics.py` in scienetist/ describes a similar but different 60 mm bore × 200 mm 4-element variant — do not cite its parameters for this file. This is NOT the 6-element MIZAN-02 rig/CFD geometry (`mizan02/.../mizan_02.stl`, DN10 N6). Do not present it as the validated mixer. Slice at 0.2 mm layers, 3 walls. Confirm mm units in slicer.
- `Venturi throat.stl` — measured 0.2 × 0.2 × 0.1 file units (probably metres → 200 dia × 100 long, axis Z), 59518 facets, NOT watertight (see MANIFEST). Repair first, save repaired copy under a new name, never overwrite the original. Confirm scale vs the mixer STL before printing them together (units differ).

## Generator provenance — TEAM TODO (required before calling these reproducible)
Record here, per STL: generator script + its parameters + export settings + date + author.
Candidate generators live in `F:\PythonScripts\scienetist\` (mixer_A/B/C, venturi_throat, open_blade, ross scripts). Do NOT copy them here until the exact revision is confirmed — one source of truth, no forks.

## Print notes (FDM, PETG/ASA)
- Static mixer: print elements flat, no supports; shells outer-side down. Keep the 2–3 mm wall clearance in mind; check manifold after any repair (`3D-Print Toolbox`).
- Venturi: halves outer-side down; plenum sleeve needs supports; drill barb bores d8 after print.
- After any repair or rescale, re-run the edge audit and log it in CHECKS.md.
