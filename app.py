import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import plotly.express as px

st.set_page_config(
    page_title="School Flood Risk Dashboard",
    page_icon="🏫",
    layout="wide"
)

st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #021C3B, #065A82);
    padding: 20px;
    border-radius: 10px;
    color: white;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🏫 School Flood Risk Dashboard</h1>
    <p>India (Tamil Nadu) + Mozambique | 580 Schools</p>
</div>
""", unsafe_allow_html=True)

# ── DATA ──
@st.cache_data
def load_data():
    tn_df = pd.read_csv(
        "https://raw.githubusercontent.com/ayyanarh1/"
        "tamil-nadu-school-flood-risk/main/"
        "tamil_nadu_570_schools_risk.csv"
    )

    tn_df["country"] = "India"
    tn_df["state"] = "Tamil Nadu"
    tn_df = tn_df.rename(columns={"connectivity": "connectivity_status"})

    moz_data = {
        "school_name": [
            "School Inhambane Coast", "Primary School Quelimane",
            "Secondary School Beira Coast", "Primary School Sofala",
            "Primary School Tete", "Primary School Gaza",
            "Secondary School Zambezia", "Secondary School Nampula",
            "School Cabo Delgado", "Primary School Maputo Central"
        ],
        "district": [
            "Inhambane", "Zambezia", "Sofala", "Sofala",
            "Tete", "Gaza", "Zambezia", "Nampula",
            "Cabo Delgado", "Maputo"
        ],
        "latitude": [
            -23.86, -17.88, -19.84, -19.52, -16.16,
            -24.05, -17.05, -15.12, -12.37, -25.96
        ],
        "longitude": [
            35.38, 36.89, 34.84, 34.56, 33.59,
            34.40, 36.98, 39.27, 40.52, 32.57
        ],
        "connectivity_status": [
            "not_connected", "not_connected", "not_connected",
            "not_connected", "not_connected", "connected",
            "not_connected", "connected", "not_connected", "connected"
        ],
        "flood_score": [93.2, 56.4, 38.9, 34.9, 54.9, 54.2, 0.5, 0.0, 0.0, 0.5],
        "final_score": [100.2, 86.2, 78.3, 73.3, 61.3, 53.8, 47.3, 34.7, 25.7, 8.3],
        "risk_tier": [
            "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL", "CRITICAL",
            "CRITICAL", "HIGH", "HIGH", "MEDIUM", "LOW"
        ],
        "school_type": ["Secondary"] * 10,
        "country": ["Mozambique"] * 10
    }

    moz_df = pd.DataFrame(moz_data)

    combined = pd.concat([tn_df, moz_df], ignore_index=True)
    combined["connectivity_status"] = combined["connectivity_status"].fillna("unknown")

    return combined

df = load_data()

# ── SIDEBAR ──
st.sidebar.header("🔧 Filters")

country = st.sidebar.multiselect(
    "Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

# Dynamic state filter (only India)
if "India" in country:
    state_options = df[df["country"] == "India"]["state"].dropna().unique()
else:
    state_options = []

state = st.sidebar.multiselect(
    "State",
    options=state_options,
    default=state_options
)

# Dynamic district filter
district_options = sorted(
    df[df["country"].isin(country)]["district"].unique()
)

district = st.sidebar.multiselect(
    "District",
    options=district_options,
    default=district_options
)

risk_filter = st.sidebar.multiselect(
    "Risk tier",
    options=["CRITICAL", "HIGH", "MEDIUM", "LOW"],
    default=["CRITICAL", "HIGH", "MEDIUM", "LOW"]
)

connectivity = st.sidebar.multiselect(
    "Connectivity",
    options=df["connectivity_status"].unique(),
    default=df["connectivity_status"].unique()
)

# ── FILTER LOGIC ──
filtered = df[
    (df["country"].isin(country)) &
    (df["district"].isin(district)) &
    (df["risk_tier"].isin(risk_filter)) &
    (df["connectivity_status"].isin(connectivity))
].copy()

# Apply state filter ONLY to India
if "India" in country and len(state) > 0:
    india_mask = filtered["country"] == "India"

    filtered = pd.concat([
        filtered[~india_mask],  # Mozambique untouched
        filtered[india_mask & filtered["state"].isin(state)]
    ])

# ── METRICS ──
st.subheader("Summary Statistics")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total schools", len(filtered))
c2.metric("CRITICAL", len(filtered[filtered.risk_tier == "CRITICAL"]))
c3.metric("HIGH", len(filtered[filtered.risk_tier == "HIGH"]))
c4.metric("No connectivity", len(filtered[filtered.connectivity_status == "not_connected"]))
c5.metric("Avg score", round(filtered.final_score.mean(), 1) if len(filtered) else 0)

st.markdown("---")

# ── MAP ──
st.subheader("Risk Map")

if len(filtered) > 0:
    center_lat = filtered.latitude.mean()
    center_lon = filtered.longitude.mean()
else:
    center_lat, center_lon = 10.5, 78.5

m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

color_map = {
    "CRITICAL": "#CC0000",
    "HIGH": "#FF6600",
    "MEDIUM": "#FFAA00",
    "LOW": "#2D8A4E"
}

cluster = MarkerCluster().add_to(m) if len(filtered) > 50 else m

for _, row in filtered.iterrows():
    state_value = row["state"] if "state" in row and pd.notna(row["state"]) else ""

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=7,
        color=color_map.get(row["risk_tier"], "gray"),
        fill=True,
        fill_opacity=0.8,
        tooltip=row["school_name"],
        popup=f"""
        <b>{row['school_name']}</b><br>
        District: {row['district']}<br>
        Country: {row['country']}<br>
        State: {state_value}<br>
        Connectivity: {row['connectivity_status']}<br>
        Score: {row['final_score']}<br>
        Risk: <b>{row['risk_tier']}</b>
        """
    ).add_to(cluster)

st_folium(m, width=1000, height=500)

# ── CHART ──
st.subheader("Risk Distribution")

risk_counts = filtered["risk_tier"].value_counts().reset_index()
risk_counts.columns = ["Risk Tier", "Count"]

fig = px.bar(
    risk_counts,
    x="Risk Tier",
    y="Count",
    color="Risk Tier",
    color_discrete_map=color_map
)

st.plotly_chart(fig, use_container_width=True)

# ── TABLE ──
st.subheader("Top Schools")

display_df = filtered.sort_values("final_score", ascending=False).head(50)

st.dataframe(
    display_df[[
        "school_name", "district", "country",
        "risk_tier", "final_score", "connectivity_status"
    ]],
    use_container_width=True
)
