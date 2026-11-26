# Cholistan Drought Dynamics, 1981–2025

Analysis code and derived data for the study *"Long-term rainfall change and meteorological drought in the
Cholistan Desert, Pakistan, 1981–2025: A multi-product Earth-observation assessment with locally identified
livestock resilience priorities"* (manuscript in preparation; citation to be added on publication).

One Jupyter notebook reproduces every figure and table of the meteorological analysis from cached
Google Earth Engine extracts. No Earth Engine account is needed to reproduce the published results.

## What the analysis does

- Area-weighted regional rainfall from native 0.05° CHIRPS v2 pentads (915 analysis cells, 24,790 km²).
- Standardized Precipitation Index (SPI-1, -3, -6, -12): gamma distribution fitted by L-moments for each ending
  calendar month, explicit zero mass, bootstrap goodness-of-fit tests and calibration sensitivity.
- Trends: Hamed–Rao modified Mann–Kendall, Sen slope with moving-block bootstrap CIs, trend-free
  pre-whitening, Benjamini–Hochberg FDR.
- Change points: Pettitt, Buishand Q/R and SNHT (permutation p), BIC comparison of step and trend models,
  bootstrap uncertainty of the change year, sub-period trends.
- Pentad-scale dry-spell definitions (eight variants), rainfall concentration and wet-pentad
  frequency–intensity decomposition.
- Pixel-level trends with field-significance control, global Moran's I and LISA, exploratory constrained
  clustering.
- Agreement with CHIRPS v3, PERSIANN-CDR, ERA5-Land and IMERG V07.

The participatory (herder consultation) component of the study is **not** part of this repository; its
qualitative records are confidential.

## Repository layout

```
notebooks/   Cholistan_Drought_Supplementary_Code.ipynb  (outputs stripped)
data/        regional/        archived regional CHIRPS v2 pentad series and SPI
             spatial_cache/   native-grid CHIRPS v2 and v3 cubes, grid definition, other products (monthly)
             gis/             study-area boundary (shapefile, EPSG:4326)
outputs/     figures and tables produced by the notebook (identical to the submitted versions)
docs/        Methodology.md, Data_dictionary.md, Reproduction_guide.md, Key_results.md
illustrations/ script that draws the workflow and conceptual-framework figures
```

## Quick start

```bash
conda env create -f environment.yml      # or: pip install -r requirements.txt
conda activate cholistan-drought
cd notebooks
jupyter lab Cholistan_Drought_Supplementary_Code.ipynb   # Run All (about 3 minutes)
```

Outputs are written to `outputs/`. The notebook stops if any built-in method self-test fails.
See `docs/Reproduction_guide.md` for details, including how to rebuild the caches from Earth Engine.

## Data sources

| Dataset | Earth Engine ID | Terms |
|---|---|---|
| CHIRPS v2.0 pentad | `UCSB-CHG/CHIRPS/PENTAD` | Public domain |
| CHIRPS v3 pentad | `UCSB-CHC/CHIRPS/V3/PENTAD` | Public domain |
| PERSIANN-CDR | `NOAA/PERSIANN-CDR` | NOAA CDR, no restrictions |
| ERA5-Land monthly | `ECMWF/ERA5_LAND/MONTHLY_AGGR` | Copernicus licence |
| IMERG V07 monthly | `NASA/GPM_L3/IMERG_MONTHLY_V07` | NASA open data |

## Licence

Not yet assigned; see `LICENSE_PENDING.md`.

## Citation

See `CITATION.cff`. Please also cite the data providers (Funk et al., 2015, 2026; Ashouri et al., 2015;
Muñoz-Sabater et al., 2021; Huffman et al., 2020).

## Contact

Tariq Abbas, Cholistan University of Veterinary and Animal Sciences, Bahawalpur, Pakistan —
tariqabbas@cuvas.edu.pk
