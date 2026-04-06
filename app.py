
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page config
st.set_page_config(
    page_title="School Flood Risk Dashboard",
    page_icon="🏫",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #021C3B, #065A82);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .metric-card {
        background: #f0f7ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #065A82;
    }
    .critical { color: #CC0000; font-weight: bold; }
    .high { color: #FF6600; font-weight: bold; }
    .medium { color: #FFAA00; font-weight: bold; }
    .low { color: #2D8A4E; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏫 School Flood Risk Dashboard</h1>
    <p>UN Giga Initiative — Multi-Country Climate Hazard Assessment</p>
    <p>Tamil Nadu, India + Mozambique | 25 Schools | 6 Data Sources</p>
</div>
""", unsafe_allow_html=True)

# Data
@st.cache_data
def load_data():
    return pd.DataFrame({
        "school_name": [
            "School Puducherry Border",
            "Panchayat School Nagapattinam",
            "School Ramanathapuram",
            "School Kanchipuram",
            "Panchayat School Tirunelveli",
            "Govt School Cuddalore",
            "School Villupuram",
            "School Tuticorin",
            "Govt High School Chennai",
            "Govt School Tiruchirappalli",
            "Govt School Thanjavur",
            "High School Vellore",
            "Govt School Salem",
            "Govt School Madurai",
            "High School Coimbatore",
            "School Inhambane Coast",
            "Primary School Quelimane",
            "Secondary School Beira Coast",
            "Primary School Sofala",
            "Primary School Tete",
            "Primary School Gaza",
            "Secondary School Zambezia",
            "Secondary School Nampula",
            "School Cabo Delgado",
            "Primary School Maputo Central"
        ],
        "country": ["Tamil Nadu"] * 15 + ["Mozambique"] * 10,
        "latitude": [
            11.93, 10.76, 9.37, 12.83, 8.71,
            11.75, 11.93, 8.80, 13.08, 10.79,
            10.78, 12.92, 11.65, 9.93, 11.01,
            -23.86, -17.88, -19.84, -19.52, -16.16,
            -24.05, -17.05, -15.12, -12.37, -25.96
        ],
        "longitude": [
            79.83, 79.84, 78.83, 79.70, 77.69,
            79.75, 79.49, 78.15, 80.27, 78.68,
            79.13, 79.13, 78.16, 78.12, 76.96,
            35.38, 36.89, 34.84, 34.56, 33.59,
            34.40, 36.98, 39.27, 40.52, 32.57
        ],
        "risk_tier": [
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "HIGH", "HIGH", "HIGH", "HIGH", "MEDIUM",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "HIGH", "HIGH", "MEDIUM", "LOW"
        ],
        "hev_score": [
            68.7, 68.3, 67.0, 66.6, 65.9,
            65.6, 62.3, 54.6, 44.8, 41.1,
            33.7, 29.5, 24.7, 23.3, 18.7,
            100.2, 86.2, 78.3, 73.3, 61.3,
            53.8, 47.3, 34.7, 25.7, 8.3
        ],
        "flood_score": [
            96.7, 56.8, 43.5, 33.3, 30.7,
            39.8, 22.9, 39.1, 13.8, 31.4,
            26.5, 22.1, 4.9, 13.0, 4.8,
            93.2, 56.4, 38.9, 34.9, 54.9,
            54.2, 0.5, 0.0, 0.0, 0.5
        ],
        "cyclone_score": [
            87.5, 79.2, 45.8, 79.2, 37.5,
            87.5, 83.3, 37.5, 100.0, 50.0,
            58.3, 66.7, 62.5, 41.7, 25.0,
            73.3, 93.3, 100.0, 93.3, 33.3,
            53.3, 80.0, 86.7, 26.7, 20.0
        ],
        "vulnerability": [
            19.9, 55.0, 79.2, 68.2, 90.0,
            55.0, 59.8, 45.7, 0.1, 40.2,
            15.0, 0.1, 0.1, 0.1, 0.0,
            75.0, 80.0, 85.0, 78.0, 70.0,
            30.0, 65.0, 20.0, 60.0, 10.0
        ],
        "connectivity": [
            "Connected", "No connectivity", "No connectivity",
            "No connectivity", "No connectivity", "No connectivity",
            "No connectivity", "Connected", "Connected",
            "No connectivity", "Connected", "Connected",
            "Connected", "Connected", "Connected",
            "No connectivity", "No connectivity", "No connectivity",
            "No connectivity", "No connectivity", "Connected",
            "No connectivity", "Connected", "No connectivity",
            "Connected"
        ],
        "risk_ssp245": [
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "HIGH", "HIGH", "HIGH", "CRITICAL", "CRITICAL",
            "HIGH", "HIGH", "HIGH", "MEDIUM", "LOW",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "HIGH", "HIGH", "MEDIUM", "LOW"
        ],
        "risk_ssp585": [
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "HIGH", "HIGH", "HIGH", "HIGH", "MEDIUM",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "CRITICAL", "HIGH", "HIGH", "LOW"
        ]
    })

df = load_data()

# ── Sidebar ──
st.sidebar.header("🔧 Filters")

country = st.sidebar.multiselect(
    "Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

risk_filter = st.sidebar.multiselect(
    "Risk tier",
    options=["CRITICAL", "HIGH", "MEDIUM", "LOW"],
    default=["CRITICAL", "HIGH", "MEDIUM", "LOW"]
)

connectivity = st.sidebar.multiselect(
    "Connectivity",
    options=df["connectivity"].unique(),
    default=df["connectivity"].unique()
)

scenario = st.sidebar.radio(
    "Climate scenario",
    options=["Current (2024)", "2050 SSP2-4.5", "2050 SSP5-8.5"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Data sources:** Sentinel-1, JRC, GFD, ERA5, IBTrACS"
)
st.sidebar.markdown(
    "[View on GitHub](https://github.com/ayyanarh1/tamil-nadu-school-flood-risk)"
)

# Map risk column based on scenario
scenario_col = {
    "Current (2024)":  "risk_tier",
    "2050 SSP2-4.5":   "risk_ssp245",
    "2050 SSP5-8.5":   "risk_ssp585"
}[scenario]

# Filter data
filtered = df[
    (df["country"].isin(country)) &
    (df[scenario_col].isin(risk_filter)) &
    (df["connectivity"].isin(connectivity))
].copy()

# ── Metrics ──
st.subheader(f"Summary — {scenario}")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total schools", len(filtered))
col2.metric("CRITICAL",
    len(filtered[filtered[scenario_col] == "CRITICAL"]),
    delta=None
)
col3.metric("HIGH",
    len(filtered[filtered[scenario_col] == "HIGH"])
)
col4.metric("No connectivity",
    len(filtered[filtered.connectivity == "No connectivity"])
)
col5.metric("Avg score",
    round(filtered.hev_score.mean(), 1) if len(filtered) > 0 else 0
)

st.markdown("---")

# ── Map + Table ──
map_col, table_col = st.columns([3, 2])

with map_col:
    st.subheader("🗺️ Risk Map")

    center_lat = filtered.latitude.mean() if len(filtered) > 0 else 0
    center_lon = filtered.longitude.mean() if len(filtered) > 0 else 60

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=3,
        tiles="CartoDB positron"
    )

    color_map = {
        "CRITICAL": "#CC0000",
        "HIGH":     "#FF6600",
        "MEDIUM":   "#FFAA00",
        "LOW":      "#2D8A4E"
    }

    for _, row in filtered.iterrows():
        risk_val = row[scenario_col]
        color = color_map.get(risk_val, "gray")

        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=max(8, row["hev_score"] / 8),
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.85,
            tooltip=row["school_name"],
            popup=folium.Popup(
                f"<b>{row['school_name']}</b><br>"
                f"Country: {row['country']}<br>"
                f"Scenario: {scenario}<br>"
                f"Risk: <b>{risk_val}</b><br>"
                f"Score: {row['hev_score']}<br>"
                f"Connectivity: {row['connectivity']}",
                max_width=260
            )
        ).add_to(m)

    st_folium(m, width=700, height=420)

with table_col:
    st.subheader("📋 Rankings")
    display_df = filtered[[
        "school_name", "country",
        scenario_col, "hev_score", "connectivity"
    ]].sort_values("hev_score", ascending=False)
    display_df.columns = [
        "School", "Country", "Risk", "Score", "Connectivity"
    ]
    st.dataframe(display_df, height=420, hide_index=True)

st.markdown("---")

# ── Charts ──
st.subheader("📊 Risk Analysis Charts")

chart1, chart2 = st.columns(2)

with chart1:
    # Risk tier distribution
    risk_counts = filtered[scenario_col].value_counts().reset_index()
    risk_counts.columns = ["Risk Tier", "Count"]
    risk_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
    risk_colors = {
        "CRITICAL": "#CC0000",
        "HIGH": "#FF6600",
        "MEDIUM": "#FFAA00",
        "LOW": "#2D8A4E"
    }
    fig1 = px.bar(
        risk_counts,
        x="Risk Tier", y="Count",
        color="Risk Tier",
        color_discrete_map=risk_colors,
        title=f"Risk Distribution — {scenario}",
        category_orders={"Risk Tier": risk_order}
    )
    fig1.update_layout(showlegend=False, height=300)
    st.plotly_chart(fig1, use_container_width=True)

with chart2:
    # Flood vs cyclone scatter
    fig2 = px.scatter(
        filtered,
        x="flood_score",
        y="cyclone_score",
        color=scenario_col,
        color_discrete_map=color_map,
        size="hev_score",
        hover_name="school_name",
        hover_data=["country", "connectivity"],
        title="Flood vs Cyclone Risk",
        labels={
            "flood_score": "Flood Score",
            "cyclone_score": "Cyclone Score"
        }
    )
    fig2.update_layout(height=300)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ── School Detail ──
st.subheader("🏫 School Profile")

selected = st.selectbox(
    "Select a school for detailed analysis",
    options=filtered["school_name"].tolist()
)

if selected:
    school = filtered[filtered.school_name == selected].iloc[0]

    info_col, chart_col = st.columns([2, 3])

    with info_col:
        st.markdown(f"### {school['school_name']}")
        st.markdown(f"**Country:** {school['country']}")
        st.markdown(f"**Connectivity:** {school['connectivity']}")
        st.markdown("---")

        c1, c2 = st.columns(2)
        c1.metric("HEV Score", school["hev_score"])
        c2.metric("Current Risk", school["risk_tier"])
        c1.metric("2050 SSP2-4.5", school["risk_ssp245"])
        c2.metric("2050 SSP5-8.5", school["risk_ssp585"])

    with chart_col:
        # Radar chart for school
        categories = [
            "Flood", "Cyclone",
            "Vulnerability", "Overall"
        ]
        values = [
            school["flood_score"],
            school["cyclone_score"],
            school["vulnerability"],
            school["hev_score"]
        ]

        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=categories,
            y=values,
            marker_color=[
                "#065A82", "#1C7293",
                "#FF6600", "#CC0000"
            ],
            text=[f"{v:.1f}" for v in values],
            textposition="outside"
        ))
        fig3.update_layout(
            title=f"Risk Profile — {selected[:30]}",
            yaxis_range=[0, 110],
            height=280,
            showlegend=False
        )
        st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ── Download ──
st.subheader("💾 Download Data")

dl1, dl2 = st.columns(2)
with dl1:
    csv = filtered.to_csv(index=False)
    st.download_button(
        label="Download filtered data (CSV)",
        data=csv,
        file_name="school_risk_filtered.csv",
        mime="text/csv"
    )
with dl2:
    all_csv = df.to_csv(index=False)
    st.download_button(
        label="Download full dataset (CSV)",
        data=all_csv,
        file_name="school_risk_all.csv",
        mime="text/csv"
    )

# ── Methodology ──
with st.expander("📖 Methodology & Data Sources"):
    st.markdown("""
    ### Risk Framework
    This dashboard uses the IPCC H x E x V framework:
    - **Hazard (40%):** Sentinel-1 SAR + JRC Surface Water +
      Global Flood Database + ERA5 Rainfall + IBTrACS Cyclones
    - **Exposure (30%):** Coastal location classification
    - **Vulnerability (30%):** Connectivity + Hospital distance + Rural

    ### Data Sources
    | Source | Coverage | Resolution |
    |--------|----------|------------|
    | Sentinel-1 SAR | 2023 monsoon / 2019 Cyclone Idai | 10m |
    | JRC Surface Water | 1984-2021 (37 years) | 30m |
    | Global Flood Database | 2000-2018 | 250m |
    | ERA5 Rainfall | 2018-2023 | ~30km |
    | IBTrACS Cyclones | 2000-2023 | Track points |

    ### 2050 Projections
    Based on IPCC AR6 delta method:
    - SSP2-4.5: +15% rainfall increase by 2050
    - SSP5-8.5: +30% rainfall increase by 2050

    ### Limitations
    - School locations are sample data
    - SSP projections use simplified delta method
    - Analysis covers 25 schools — expandable to full Giga dataset

    **Full code:** github.com/ayyanarh1/tamil-nadu-school-flood-risk
    """)

st.caption(
    "Built with Google Earth Engine, Python and Streamlit | "
    "UN Giga Initiative | "
    "github.com/ayyanarh1/tamil-nadu-school-flood-risk"
)
