# Tamil Nadu School Flood Risk Analysis 🏫🌊🛰️

Satellite-based flood risk assessment for schools in Tamil Nadu, India
combining 6 data sources across 40+ years of climate and flood data,
including cyclone wind hazard, vulnerability index and 2050 climate projections.

## Run in Google Colab
| Notebook | Open |
|----------|------|
| Day 1 — Sentinel-1 SAR flood mapping | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day1_tamil_nadu_flood_risk.ipynb) |
| Day 2 — JRC historical flood data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day2_jrc_historical_flood.ipynb) |
| Day 3 — GFD flood frequency | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day3_aqueduct_hazard.ipynb) |
| Day 4 — ERA5 rainfall analysis | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day4_era5_climate.ipynb) |
| Day 5 — SSP 2050 projections | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day5_ssp_projections.ipynb) |
| Day 6 — Publication maps | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day6_publication_maps.ipynb) |
| Day 7 — Portfolio finalise | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day7_portfolio_finalise.ipynb) |
| Day 8 — Cyclone wind hazard | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day8_cyclone_wind_hazard.ipynb) |
| Day 9 — Vulnerability index | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day9_vulnerability_index.ipynb) |
| Day 10 — Decision report | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day10_decision_report.ipynb) |
| Day 11 — Kepler visualization | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day11_kepler_visualization.ipynb) |

## Data Sources
| Day | Dataset | Coverage |
|-----|---------|----------|
| Day 1 | Sentinel-1 SAR | 2023 monsoon season |
| Day 2 | JRC Surface Water | 1984-2021 (37 years) |
| Day 3 | Global Flood Database | 2000-2018 major events |
| Day 4 | ERA5 Rainfall | 2018-2023 climate data |
| Day 5 | CMIP6 SSP scenarios | 2050 projections |
| Day 8 | IBTrACS Cyclone Tracks | 2000-2023 Bay of Bengal |
| Day 9 | OpenStreetMap (OSMnx) | 2168 Tamil Nadu hospitals |

## Risk Framework — IPCC H x E x V
| Component | Data sources | Weight |
|-----------|-------------|--------|
| Hazard (H) | SAR + JRC + GFD + ERA5 + Cyclone | 40% |
| Exposure (E) | Coastal location classification | 30% |
| Vulnerability (V) | Connectivity + Hospital + Rural | 30% |

## Key Findings — H x E x V Final Rankings
| Risk tier | Schools |
|-----------|---------|
| 🚨 CRITICAL | Puducherry Border, Nagapattinam, Ramanathapuram, Kanchipuram, Tirunelveli, Cuddalore, Villupuram, Tuticorin, Chennai, Tiruchirappalli |
| 🔴 HIGH | Thanjavur, Vellore, Salem, Madurai |
| 🟡 MEDIUM | Coimbatore |

## Key Findings — 2050 Climate Projections
| Scenario | New CRITICAL schools |
|----------|---------------------|
| SSP2-4.5 (+15% rainfall) | Ramanathapuram added |
| SSP5-8.5 (+30% rainfall) | Ramanathapuram, Cuddalore, Tuticorin added |

## Priority Actions
| Action | Schools |
|--------|---------|
| 🚨 URGENT connectivity + flood resilience | Nagapattinam, Ramanathapuram, Cuddalore, Kanchipuram, Tirunelveli, Villupuram |
| 🚨 URGENT emergency access + flood shelter | Tirunelveli, Tuticorin |
| 🔴 HIGH PRIORITY flood resilience planning | Puducherry Border, Chennai, Tiruchirappalli |
| 🟡 MONITOR disaster preparedness | Thanjavur, Vellore, Salem, Madurai |

## Interactive Maps
- 🗺️ [Day 1 — Sentinel-1 flood map](tamil_nadu_school_risk.html)
- 🗺️ [Day 2 — Combined SAR+JRC risk map](tamil_nadu_combined_risk_map.html)
- 🗺️ [Day 3 — Master risk map (3 sources)](tamil_nadu_master_risk_map.html)
- 🗺️ [Day 5 — 2050 scenario map](tamil_nadu_2050_risk_map.html)
- 🗺️ [Day 8 — Multi-hazard map](tamil_nadu_multihazard_map.html)

## Publication Maps
- 🖼️ [3-panel scenario map (300 DPI)](tamil_nadu_publication_map.png)
- 🖼️ [Risk escalation map (300 DPI)](tamil_nadu_risk_change_map.png)
- 🖼️ [Dark theme risk map (300 DPI)](tamil_nadu_kepler_style_map.png)
- 📊 [Rainfall time series chart](tamil_nadu_rainfall_timeseries.png)
- 📊 [2050 projections chart](tamil_nadu_2050_projections.png)

## Reports & Data
- 📄 [Full PDF Report](tamil_nadu_flood_risk_report.pdf)
- 📊 [Excel Decision Report](tamil_nadu_school_risk_report.xlsx)
- 📋 [H x E x V Risk Scores CSV](tamil_nadu_hev_risk.csv)
- 📋 [Multi-hazard Scores CSV](tamil_nadu_multihazard_scores.csv)

## Tools Used
- Google Earth Engine (Sentinel-1, JRC, GFD)
- Python (GeoPandas, Folium, OSMnx, xarray, pandas, openpyxl, fpdf2)
- ERA5 Climate Data (Copernicus CDS API)
- IBTrACS Cyclone Track Data (NOAA)
- OpenStreetMap via OSMnx (hospital locations)
- CMIP6 SSP projections (delta method)
- Kepler.gl (interactive visualization)
- Contextily (basemap tiles)
- Google Colab

## Repository Structure
```
day1_tamil_nadu_flood_risk.ipynb     — SAR flood mapping
day2_jrc_historical_flood.ipynb      — 37-year flood history
day3_aqueduct_hazard.ipynb           — GFD major flood events
day4_era5_climate.ipynb              — ERA5 rainfall analysis
day5_ssp_projections.ipynb           — 2050 climate projections
day6_publication_maps.ipynb          — Publication quality maps
day7_portfolio_finalise.ipynb        — PDF report + portfolio
day8_cyclone_wind_hazard.ipynb       — Cyclone hazard analysis
day9_vulnerability_index.ipynb       — H x E x V framework
day10_decision_report.ipynb          — Excel decision report
day11_kepler_visualization.ipynb     — Kepler.gl dark theme map
tamil_nadu_multihazard_map.html      — Multi-hazard interactive map
tamil_nadu_kepler_style_map.png      — Dark theme 300 DPI map
tamil_nadu_publication_map.png       — 3-panel scenario map
tamil_nadu_risk_change_map.png       — Risk escalation map
tamil_nadu_hev_risk.csv              — Full H x E x V risk scores
tamil_nadu_school_risk_report.xlsx   — Excel decision report
tamil_nadu_flood_risk_report.pdf     — Full analysis report
TamilNadu_School_FloodRisk.pptx      — Presentation deck
