# Multi-Country School Flood Risk Analysis 🏫🌊🛰️

## Live Dashboard
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tamil-nadu-school-flood-risk-ewc2sj7fhrvvtkwlpw5jzf.streamlit.app/)

**[Open Live Dashboard](https://tamil-nadu-school-flood-risk-ewc2sj7fhrvvtkwlpw5jzf.streamlit.app/)**

Satellite-based flood risk assessment for 580 schools across Tamil Nadu (India)
and Mozambique, combining 6 data sources across 40+ years of climate and
flood data, including cyclone wind hazard, vulnerability index and 2050
climate projections.

---

## Scale
| Country | Schools | CRITICAL | No Connectivity |
|---------|---------|----------|----------------|
| 🇮🇳 Tamil Nadu, India | 570 | 82 | 285 |
| 🇲🇿 Mozambique | 10 | 6 | 7 |
| **Total** | **580** | **88** | **292** |

## Dashboard Features
- 🗺️ Interactive risk map with clustering
- 📊 4 Plotly charts — distribution, district, connectivity, histogram
- 📋 Filterable data table with CSV download
- 🏫 School profile with mini map
- 🔄 Country, district, risk tier and connectivity filters
- 📖 Methodology expander

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
| Day 12 — Mozambique pilot | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day12_mozambique_pilot.ipynb) |
| Day 13 — Portfolio 2 finalise | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day13_portfolio2_finalise.ipynb) |
| Day 14 — Streamlit dashboard | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day14_streamlit_app.ipynb) |
| Day 15 — Streamlit enhanced | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day15_streamlit_enhanced.ipynb) |
| Day 16 — Giga 570 schools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day16_giga_real_data.ipynb) |
| Day 17 — Streamlit 570 schools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayyanarh1/tamil-nadu-school-flood-risk/blob/main/day17_streamlit_570.ipynb) |

## Data Sources
| Day | Dataset | Coverage |
|-----|---------|----------|
| Day 1 | Sentinel-1 SAR | 2023 monsoon + 2019 Cyclone Idai |
| Day 2 | JRC Surface Water | 1984-2021 (37 years) |
| Day 3 | Global Flood Database | 2000-2018 major events |
| Day 4 | ERA5 Rainfall | 2018-2023 climate data |
| Day 5 | CMIP6 SSP scenarios | 2050 projections |
| Day 8 | IBTrACS Cyclone Tracks | 2000-2023 Bay of Bengal + Indian Ocean |
| Day 9 | OpenStreetMap (OSMnx) | 2168 Tamil Nadu hospitals |
| Day 16 | Giga-style school dataset | 570 Tamil Nadu schools |

## Risk Framework — IPCC H x E x V
| Component | Data sources | Weight |
|-----------|-------------|--------|
| Hazard (H) | SAR + JRC + GFD + ERA5 + Cyclone | 40% |
| Exposure (E) | Coastal location classification | 30% |
| Vulnerability (V) | Connectivity + Hospital + Rural | 30% |

## Key Findings — Tamil Nadu (570 schools)
| District | Schools | CRITICAL | Avg Score |
|----------|---------|----------|-----------|
| Ramanathapuram | 25 | 14 | 44.7 |
| Thoothukudi | 30 | 15 | 43.1 |
| Cuddalore | 40 | 15 | 37.6 |
| Nagapattinam | 35 | 13 | 35.9 |
| Chennai | 50 | 17 | 34.6 |
| Puducherry | 20 | 7 | 32.7 |
| Madurai | 50 | 0 | 7.1 |
| Salem | 40 | 0 | 7.3 |
| Coimbatore | 50 | 1 | 7.8 |

## Key Findings — Mozambique
| Risk tier | Schools |
|-----------|---------|
| 🚨 CRITICAL | Inhambane Coast, Quelimane, Beira Coast, Sofala, Tete, Gaza |
| 🔴 HIGH | Zambezia, Nampula |
| 🟡 MEDIUM | Cabo Delgado |
| 🟢 LOW | Maputo Central |

## Key Comparative Finding
> Both Tamil Nadu and Mozambique show the same pattern — coastal schools
> with no connectivity face compound risk from flood and cyclone hazards.
> The pipeline is generalisable across LMIC contexts.

## Key Findings — 2050 Climate Projections
| Scenario | Impact |
|----------|--------|
| SSP2-4.5 (+15% rainfall) | 3 more Tamil Nadu schools reach CRITICAL |
| SSP5-8.5 (+30% rainfall) | 5 more Tamil Nadu schools reach CRITICAL |

## Priority Actions
| Action | Schools |
|--------|---------|
| 🚨 URGENT connectivity + flood resilience | Ramanathapuram, Thoothukudi coastal schools |
| 🚨 URGENT emergency access + flood shelter | Tirunelveli, Tuticorin, Inhambane |
| 🔴 HIGH PRIORITY flood resilience planning | Chennai, Cuddalore, Nagapattinam coastal schools |
| 🟡 MONITOR disaster preparedness | Thanjavur, Vellore, Zambezia, Nampula |

## Interactive Maps
- 🗺️ [Day 1 — Sentinel-1 flood map](tamil_nadu_school_risk.html)
- 🗺️ [Day 2 — Combined SAR+JRC risk map](tamil_nadu_combined_risk_map.html)
- 🗺️ [Day 3 — Master risk map (3 sources)](tamil_nadu_master_risk_map.html)
- 🗺️ [Day 5 — 2050 scenario map](tamil_nadu_2050_risk_map.html)
- 🗺️ [Day 8 — Multi-hazard map](tamil_nadu_multihazard_map.html)
- 🗺️ [Day 12 — Tamil Nadu + Mozambique combined map](mozambique_tamil_nadu_combined_map.html)
- 🗺️ [Day 16 — 570 school large scale map](tamil_nadu_570_schools_map.html)

## Publication Maps
- 🖼️ [3-panel scenario map (300 DPI)](tamil_nadu_publication_map.png)
- 🖼️ [Risk escalation map (300 DPI)](tamil_nadu_risk_change_map.png)
- 🖼️ [Dark theme risk map (300 DPI)](tamil_nadu_kepler_style_map.png)
- 📊 [Rainfall time series chart](tamil_nadu_rainfall_timeseries.png)
- 📊 [2050 projections chart](tamil_nadu_2050_projections.png)

## Reports & Data
- 📄 [Tamil Nadu PDF Report](tamil_nadu_flood_risk_report.pdf)
- 📄 [Multi-Country PDF Report](multi_country_risk_report.pdf)
- 📊 [Excel Decision Report](tamil_nadu_school_risk_report.xlsx)
- 📋 [570 School Risk Dataset](tamil_nadu_570_schools_risk.csv)
- 📋 [H x E x V Risk Scores](tamil_nadu_hev_risk.csv)
- 📋 [Mozambique Risk Scores](mozambique_risk_scores.csv)
- 📋 [Combined 25-school Dataset](combined_tamil_nadu_mozambique.csv)

## Tools Used
- Google Earth Engine (Sentinel-1, JRC, GFD)
- Python (GeoPandas, Folium, OSMnx, xarray, pandas, openpyxl, fpdf2)
- Streamlit + Streamlit Cloud (live dashboard)
- ERA5 Climate Data (Copernicus CDS API)
- IBTrACS Cyclone Track Data (NOAA)
- OpenStreetMap via OSMnx (hospital locations)
- CMIP6 SSP projections (delta method)
- Kepler.gl (interactive visualization)
- Contextily (basemap tiles)
- Google Colab

## Repository Structure
