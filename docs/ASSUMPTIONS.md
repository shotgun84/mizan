# Assumptions register (every number in the report traces here; change here, rerun reproduce.py)

| # | Assumption | Value used | Status | If wrong, what breaks |
|---|---|---|---|---|
| A1 | Brine flow 6.283 m³/s (2 m pipe at 2 m/s) | Example, not a plant measurement | ASSUMED | All absolute MW/cost figures rescale linearly |
| A2 | Brine 70 ppt, ambient 42.5 ppt | Spec + Gulf example | ASSUMED | S_mix endpoints shift (salt balance is exact given inputs) |
| A3 | Pump efficiency 0.75 | Typical | ASSUMED | Power ±10–15% |
| A4 | Tariff AED 0.44/kWh | Industrial illustration | ASSUMED | Costs scale linearly; state tariff with every cost claim |
| A5 | Static lift 5 m, offshore pipe 800 m, roughness 0.05 mm | Example site | ASSUMED | Offshore friction share; confirm site data |
| A6 | Mixer loss = 6× empty pipe (range 4–8) | Literature-type value, fouling dependent | ESTIMATED ±30–50% | Stage-1 head 0.1–0.3 m band |
| A7 | Venturi head = 1.3×ideal + 0.5 m | 1D + margin | ESTIMATED ±30–50% | Stage-2 power 0.15–0.35 MW band |
| A8 | 42% recovery, Taweelah 909,200 m³/d product | Illustration only | ASSUMED | Scale factor 2.31 is illustrative, not plant data |
| A9 | Intake screens < 0.15 m/s, no fouling derate in headline numbers | Design target | PROPOSED | Real w falls if screens clog (carried as risk case) |

Dilution redistributes salt; it does not remove it. Discharge stays above ambient in all cases.
