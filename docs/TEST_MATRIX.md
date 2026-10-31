# Tank-test matrix (planned — fill IDs/dates as run; success criteria fixed in advance)

| ID | Objective | Controlled | Measured | Reps | Pass criterion | Fail action |
|---|---|---|---|---|---|---|
| T-MIX-01 | Mixer uniformity at 0.5:1 | Qp fixed, Qs sweep 0.25/0.5/0.75× | Outlet CoV (5-point EC), dp | 3 + blank (no mixer) | CoV < 0.05, head within 50% of 1D | Check injection position before adding elements |
| T-MIX-02 | TWE vs seawater feed | Same, feed swapped | Same + scaling notes | 3 | Same + no excess fouling in run | Fall back to seawater baseline |
| T-VENT-01 | Entrainment curve | Primary Q fixed, w sweep via valve | Qs, suction kPa, head, outlet S | 3 per w | w within 30% of 1D, head within 50%, no cavitation noise | Redesign throat/intake per data |
| T-VENT-02 | Fouling sensitivity | Half-blocked screens | w, head | 2 | Quantify w drop (expect ~55 ppt fallback) | Resize screens, update cleaning plan |
| T-FIELD-01 | Plume check (if site access) | Release rate | Salinity at 10/50/100/500 m, current | campaign | Compare vs UM3-type near-field estimate | Feed back to outfall orientation |

Controls for all runs: T = 25 °C, EC calibrated (see CALIBRATION_TEMPLATE), flowmeters ±3%, triplicate + blank. Stop rules: cavitation noise, leak, EC drift > 1 ppt between calibrations.
