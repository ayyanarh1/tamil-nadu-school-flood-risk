# Tamil Nadu School Flood Risk Analysis 🏫🌊🛰️

Satellite-based flood risk assessment for schools in Tamil Nadu, India
combining 4 data sources across 40+ years of climate and flood data.

## Data Sources
| Day | Dataset | Coverage |
|-----|---------|----------|
| Day 1 | Sentinel-1 SAR | 2023 monsoon season |
| Day 2 | JRC Surface Water | 1984–2021 (37 years) |
| Day 3 | Global Flood Database | 2000–2018 major events |
| Day 4 | ERA5 Rainfall | 2018–2023 climate data |

## Key Findings
- 2 CRITICAL risk schools — Puducherry Border, Nagapattinam
- 6 HIGH risk schools — all coastal locations
- Coastal schools with no connectivity = highest priority
- November = peak flood month (northeast monsoon)
- Coimbatore and Salem = zero flood risk confirmed

## Tools Used
- Google Earth Engine (Sentinel-1, JRC, GFD)
- Python (GeoPandas, Folium, xarray, pandas)
- ERA5 Climate Data (Copernicus CDS API)
- Google Colab

## Files
- 📓 4 Jupyter notebooks (Day 1–4)
- 🗺️ 3 interactive HTML risk maps
- 📊 3 CSV risk tables
- 📈 Rainfall time series chart
- 📑 PowerPoint presentation

## Next Steps
- SSP 2050 climate projections (Day 5)
- Streamlit dashboard deployment (Week 3)
- Giga Spatial library contribution (Week 4)
