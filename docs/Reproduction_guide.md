# Reproduction guide

## 1 Reproduce the published results (no Earth Engine needed)

1. Install Python 3.11 or later and the packages in `requirements.txt` (or `environment.yml`).
2. Open `notebooks/Cholistan_Drought_Supplementary_Code.ipynb` from the `notebooks/` folder and run all
   cells. The project root is found automatically (the parent of `notebooks/`). To run from elsewhere, set
   the environment variable `CHOLISTAN_PROJECT_ROOT` to the repository folder.
3. The notebook reads `data/regional/` and `data/spatial_cache/`, runs self-tests of every statistical
   routine against known answers, and writes 12 TIFF figures (600 dpi, 174 mm wide) and 35 CSV tables to
   `outputs/`, together with `Captions.md`, `Key_results.md`, `Figure_quality_check.csv`,
   `Output_manifest.csv` and `Provenance.json`.
4. Random seeds are fixed (2026). A clean re-run reproduced every CSV table in `outputs/` byte for byte.

Run time is about 2–3 minutes on a laptop.

## 2 Rebuild the caches from Earth Engine (optional)

1. `pip install earthengine-api` and authenticate (`earthengine authenticate`).
2. Set `EE_PROJECT_ID` to a Google Cloud project with the Earth Engine API enabled. Optionally set
   `EE_BOUNDARY_ASSET` to an Earth Engine asset of the boundary.
3. In the configuration cell set `ALLOW_EARTH_ENGINE = True`, and delete or move the files in
   `data/spatial_cache/` that you want rebuilt.

Never commit credentials. `.gitignore` excludes common credential files.

## 3 Optional GeoTIFF export

If `rasterio` is installed, pixel trend fields are also written as GeoTIFFs to `outputs/GIS_rasters/`.
