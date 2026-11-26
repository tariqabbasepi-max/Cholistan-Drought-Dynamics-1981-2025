# Data dictionary

## data/regional/

| File | Content |
|---|---|
| `CHIRPS_pentad_area_mean_1981_2025_RAW_CACHE.csv` | Area-weighted CHIRPS v2 pentad rainfall (mm) over the study boundary, 1981–2025, as extracted from Earth Engine for the original submission; columns `date`, `pentad_property`, `rainfall_mm` (3,240 pentads). |
| `spi_gamma_primary.csv` | SPI series archived with the original submission; used only to check reproduction (Table S1). |

## data/spatial_cache/

| File | Content |
|---|---|
| `chirps_native_grid.json` | Native 0.05° grid definition: CRS, origin (`x0`, `y0`), cell size (`sx`, `sy`), 43 × 65 cells. |
| `chirps_v2_cube_1981_2025.npz` | CHIRPS v2 pentad rainfall (mm) on the native grid: array `cube` (45 years × 72 pentads × 43 rows × 65 columns) with `years`, `lat` and `lon`. Coverage fractions and cell areas are computed in the notebook from the boundary. |
| `chirps_v3_cube_1981_2025.npz` | As above for CHIRPS v3. |
| `interproduct_<product>_monthly.csv` | Area-weighted monthly rainfall (mm) for PERSIANN-CDR, ERA5-Land and IMERG V07; columns `year`, `month`, `rainfall_mm`. |

## data/gis/Cholistan_Boundary/

Study-area polygon (EPSG:4326), area 24,790 km². Source and licence to be confirmed by the authors.

## outputs/

Main and supplementary figures and tables. Table numbering follows the notebook (`Table_1`–`Table_4`,
`Table_S01`–`Table_S31`); in the article the main tables are renumbered (notebook Table 1 → article Table 2,
Table 3 → 3, Table 4 → 4, Table 2 → 5; article Table 1 lists the datasets). Each table's columns are
described in `outputs/Captions.md`.

Key conventions: rainfall in mm; Sen slopes per year unless the column says per decade; `p_hr` is the
Hamed–Rao modified Mann–Kendall p-value; `q_*` are Benjamini–Hochberg adjusted values; years in change-point
tables are the last year of the first segment.
