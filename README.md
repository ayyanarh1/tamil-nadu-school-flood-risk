# Tamil Nadu School Flood Risk Analysis 🏫🌊🛰️

Satellite-based flood risk assessment for schools in Tamil Nadu, India
combining 4 data sources across 40+ years of climate and flood data,
including 2050 climate change projections.

## Run in Google Colab
| Notebook | Open |
|----------|------|
| Day 1 — Sentinel-1 SAR flood mapping | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day1_tamil_nadu_flood_risk.ipynb) |
| Day 2 — JRC historical flood data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day2_jrc_historical_flood.ipynb) |
| Day 3 — GFD flood frequency | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day3_aqueduct_hazard.ipynb) |
| Day 4 — ERA5 rainfall analysis | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day4_era5_climate.ipynb) |
| Day 5 — SSP 2050 projections | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day5_ssp_projections.ipynb) |

## Data Sources
| Day | Dataset | Coverage |
|-----|---------|----------|
| Day 1 | Sentinel-1 SAR | 2023 monsoon season |
| Day 2 | JRC Surface Water | 1984–2021 (37 years) |
| Day 3 | Global Flood Database | 2000–2018 major events |
| Day 4 | ERA5 Rainfall | 2018–2023 climate data |
| Day 5 | CMIP6 SSP scenarios | 2050 projections |

## Key Findings — Current Risk
| Risk tier | Schools |
|-----------|---------|
| 🚨 CRITICAL | Puducherry Border, Nagapattinam |
| 🔴 HIGH | Ramanathapuram, Cuddalore, Tuticorin, Kanchipuram, Tiruchirappalli, Tirunelveli, Thanjavur |
| 🟡 MEDIUM | Vellore, Villupuram, Chennai, Madurai |
| 🟢 LOW | Coimbatore, Salem |

## Key Findings — 2050 Climate Projections
| Scenario | New CRITICAL schools |
|----------|---------------------|
| SSP2-4.5 (+15% rainfall) | Ramanathapuram added |
| SSP5-8.5 (+30% rainfall) | Ramanathapuram, Cuddalore, Tuticorin added |

## Interactive Maps
- 🗺️ [Day 1 — Sentinel-1 flood map](tamil_nadu_school_risk.html)
- 🗺️ [Day 2 — Combined SAR+JRC risk map](tamil_nadu_combined_risk_map.html)
- 🗺️ [Day 3 — Master risk map (3 sources)](tamil_nadu_master_risk_map.html)
- 🗺️ [Day 5 — 2050 scenario map](tamil_nadu_2050_risk_map.html)

## Tools Used
- Google Earth Engine (Sentinel-1, JRC, GFD)
- Python (GeoPandas, Folium, xarray, pandas)
- ERA5 Climate Data (Copernicus CDS API)
- CMIP6 SSP projections (delta method)
- Google Colab

## Repository Structure
```
day1_tamil_nadu_flood_risk.ipynb    — SAR flood mapping
day2_jrc_historical_flood.ipynb     — 37-year flood history
day3_aqueduct_hazard.ipynb          — GFD major flood events
day4_era5_climate.ipynb             — ERA5 rainfall analysis
day5_ssp_projections.ipynb          — 2050 climate projections
tamil_nadu_2050_risk_map.html       — Interactive scenario map
tamil_nadu_2050_projections.png     — Before/after chart
tamil_nadu_day4_final_risk.csv      — 4-source risk scores
tamil_nadu_2050_projections.csv     — 2050 projected scores
TamilNadu_School_FloodRisk.pptx     — Presentation deck
```

## Next Steps
- Streamlit dashboard deployment (Day 6–7)
- Giga Spatial library contribution (Week 4)
- Expand to real Giga school dataset (5,000+ schools)
