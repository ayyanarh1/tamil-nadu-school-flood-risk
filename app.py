
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import numpy as np

# Page config
st.set_page_config(
    page_title="School Flood Risk Dashboard",
    page_icon="🏫",
    layout="wide"
)

# Header
st.title("🏫 School Flood Risk Dashboard")
st.markdown("**UN Giga Initiative — Multi-Country Climate Hazard Assessment**")
st.markdown("---")

# Data
@st.cache_data
def load_data():
    data = {
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
        "connectivity": [
            "Connected", "No connectivity", "No connectivity",
            "No connectivity", "No connectivity", "No connectivity",
            "No connectivity", "Connected", "Connected",
            "No connectivity", "Connected", "Connected",
            "Connected", "Connected", "Connected",
            "No connectivity", "No connectivity", "No connectivity",
            "No connectivity", "No connectivity", "Connected",
            "No connectivity", "Connected", "No connectivity", "Connected"
        ],
        "risk_2050": [
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "HIGH", "HIGH", "HIGH", "HIGH", "MEDIUM",
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "HIGH", "HIGH", "MEDIUM", "LOW"
        ]
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

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

# Filter data
filtered = df[
    (df["country"].isin(country)) &
    (df["risk_tier"].isin(risk_filter)) &
    (df["connectivity"].isin(connectivity))
]

# Metrics row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total schools", len(filtered))
col2.metric("CRITICAL risk",
    len(filtered[filtered.risk_tier == "CRITICAL"]))
col3.metric("No connectivity",
    len(filtered[filtered.connectivity == "No connectivity"]))
col4.metric("Avg risk score",
    round(filtered.hev_score.mean(), 1) if len(filtered) > 0 else 0)

st.markdown("---")

# Map + table columns
map_col, table_col = st.columns([3, 2])

with map_col:
    st.subheader("Risk Map")

    # Build Folium map
    if len(filtered) > 0:
        center_lat = filtered.latitude.mean()
        center_lon = filtered.longitude.mean()
    else:
        center_lat, center_lon = 0, 60

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
        color = color_map.get(row["risk_tier"], "gray")
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
                f"Risk: {row['risk_tier']}<br>"
                f"Score: {row['hev_score']}<br>"
                f"Connectivity: {row['connectivity']}",
                max_width=250
            )
        ).add_to(m)

    st_folium(m, width=700, height=450)

with table_col:
    st.subheader("Risk Rankings")
    display_df = filtered[[
        "school_name", "country",
        "risk_tier", "hev_score", "connectivity"
    ]].sort_values("hev_score", ascending=False)
    display_df.columns = [
        "School", "Country",
        "Risk", "Score", "Connectivity"
    ]
    st.dataframe(display_df, height=450, hide_index=True)

st.markdown("---")

# School detail
st.subheader("School Detail")
selected = st.selectbox(
    "Select a school",
    options=filtered["school_name"].tolist()
)

if selected:
    school = filtered[filtered.school_name == selected].iloc[0]
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("HEV Score", school["hev_score"])
    c2.metric("Flood Score", school["flood_score"])
    c3.metric("Cyclone Score", school["cyclone_score"])
    c4.metric("Risk Tier", school["risk_tier"])
    c5.metric("2050 Risk", school["risk_2050"])

    st.info(
        f"**{school['school_name']}** | "
        f"{school['country']} | "
        f"Connectivity: {school['connectivity']}"
    )

# Download
st.markdown("---")
st.subheader("Download Data")
csv = filtered.to_csv(index=False)
st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="school_risk_data.csv",
    mime="text/csv"
)

st.caption(
    "Data sources: Sentinel-1 SAR, JRC Surface Water, "
    "Global Flood Database, ERA5, IBTrACS | "
    "github.com/ayyanarh1/tamil-nadu-school-flood-risk"
)
