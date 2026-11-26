# Methodology summary

Full methods, equations and references are given in Section 2 of the article and Section S2 of its
Supplementary Material. This summary maps each method to the notebook section that implements it.

| Step | Method | Key settings | Notebook |
|---|---|---|---|
| Spatial aggregation | Area-weighted mean, w = coverage × cell area | Native 0.05° grid; cells ≥ 50% inside for pixel analysis | §10 |
| SPI | Gamma by L-moments (Hosking 1990 approximation), per ending calendar month | Zero mass H(0) = q; full-record calibration; 1991–2020 and q/2 sensitivity | §2 `spi()`; §6 |
| SPI goodness of fit | KS and Anderson–Darling | 999 parametric-bootstrap replicates with re-fitting; BH across months | §2, §6 |
| Trend | Hamed–Rao modified Mann–Kendall; Sen slope | Moving-block bootstrap CI (block 4 years, 2,000 replicates); TFPW; BH-FDR within families | §2 `trend_row()`; §7 |
| Change point | Pettitt, Buishand Q/R, SNHT | 9,999 permutations | §2, §7 |
| Step vs trend | Constant, linear, step, step + trend, hinge | BIC/AICc; break year counted as a parameter | §2, §7 |
| Change-year uncertainty | Block bootstrap of step-model residuals; Pettitt under pure-trend null | 2,000 replicates | §2, §7 |
| Dry pentads | Mid-rank calendar-pentad percentile vs 1991–2020 | P25/P20/P10/P05; eligibility ≥ 1 or ≥ 2 mm; absolute < 1, < 2 mm | §2, §8 |
| Concentration | Top-10 share, max pentad, Gini, PCI, wet pentads ≥ 5 mm | Log frequency–intensity decomposition | §2, §9 |
| Pixel trends | As regional, per cell | BH-FDR across cells, q ≤ 0.10 | §11–12 |
| Spatial autocorrelation | Global Moran's I; LISA | Queen (rook sensitivity); 9,999 conditional permutations; BH q ≤ 0.05 | §11 `moran_global()`, `lisa()` |
| Zones | Spatially constrained Ward on standardised annual anomalies | k = 2–8, silhouette; year-resampling ARI (200) | §14 |
| Product agreement | r, bias, KGE, Sen trend, Pettitt, SPI-12 correlation | Each product's overlap with CHIRPS v2 | §13 `kge()` |

Section numbers refer to the notebook's numbered headings.
