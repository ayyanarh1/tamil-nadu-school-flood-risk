
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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
    <p>Multi-Country Climate Hazard Assessment — Tamil Nadu + Mozambique Climate Hazard Assessment</p>
    <p>580 Schools | 6 Satellite & Climate Data Sources | 40+ Years of Data</p>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    # Tamil Nadu 570 schools
    tn_df = pd.read_csv(
        'https://raw.githubusercontent.com/ayyanarh1/'
        'tamil-nadu-school-flood-risk/main/'
        'tamil_nadu_570_schools_risk.csv'
    )
    tn_df['country'] = 'Tamil Nadu'
    tn_df = tn_df.rename(columns={
        'connectivity': 'connectivity_status'
    })

    # Mozambique 10 schools
    moz_data = {
        'school_name': [
            'School Inhambane Coast',
            'Primary School Quelimane',
            'Secondary School Beira Coast',
            'Primary School Sofala',
            'Primary School Tete',
            'Primary School Gaza',
            'Secondary School Zambezia',
            'Secondary School Nampula',
            'School Cabo Delgado',
            'Primary School Maputo Central'
        ],
        'district': [
            'Inhambane', 'Zambezia', 'Sofala', 'Sofala',
            'Tete', 'Gaza', 'Zambezia', 'Nampula',
            'Cabo Delgado', 'Maputo'
        ],
        'latitude': [
            -23.86, -17.88, -19.84, -19.52, -16.16,
            -24.05, -17.05, -15.12, -12.37, -25.96
        ],
        'longitude': [
            35.38, 36.89, 34.84, 34.56, 33.59,
            34.40, 36.98, 39.27, 40.52, 32.57
        ],
        'connectivity_status': [
            'not_connected', 'not_connected', 'not_connected',
            'not_connected', 'not_connected', 'connected',
            'not_connected', 'connected', 'not_connected',
            'connected'
        ],
        'flood_score': [
            93.2, 56.4, 38.9, 34.9, 54.9,
            54.2, 0.5, 0.0, 0.0, 0.5
        ],
        'final_score': [
            100.2, 86.2, 78.3, 73.3, 61.3,
            53.8, 47.3, 34.7, 25.7, 8.3
        ],
        'risk_tier': [
            'CRITICAL', 'CRITICAL', 'CRITICAL', 'CRITICAL', 'CRITICAL',
            'CRITICAL', 'HIGH', 'HIGH', 'MEDIUM', 'LOW'
        ],
        'school_type': ['Secondary'] * 10,
        'country': ['Mozambique'] * 10
    }
    moz_df = pd.DataFrame(moz_data)

    # Combine
    combined = pd.concat([tn_df, moz_df], ignore_index=True)
    combined['connectivity_status'] = combined[
        'connectivity_status'
    ].fillna('unknown')
    return combined

df = load_data()

# ── Sidebar ──
st.sidebar.header("🔧 Filters")

country = st.sidebar.multiselect(
    "Country",
    options=df["country"].unique(),
    default=df["country"].unique()
)

district = st.sidebar.multiselect(
    "District",
    options=sorted(df["district"].unique()),
    default=sorted(df["district"].unique())
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

st.sidebar.markdown("---")
st.sidebar.markdown(
    "[View on GitHub](https://github.com/ayyanarh1/"
    "tamil-nadu-school-flood-risk)"
)
st.sidebar.markdown(
    "[Live App](https://tamil-nadu-school-flood-risk-"
    "ewc2sj7fhrvvtkwlpw5jzf.streamlit.app/)"
)

# Filter
filtered = df[
    (df["country"].isin(country)) &
    (df["district"].isin(district)) &
    (df["risk_tier"].isin(risk_filter)) &
    (df["connectivity_status"].isin(connectivity))
].copy()

# ── Metrics ──
st.subheader("Summary Statistics")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total schools", len(filtered))
c2.metric("CRITICAL",
    len(filtered[filtered.risk_tier == "CRITICAL"]))
c3.metric("HIGH",
    len(filtered[filtered.risk_tier == "HIGH"]))
c4.metric("No connectivity",
    len(filtered[filtered.connectivity_status == "not_connected"]))
c5.metric("Avg score",
    round(filtered.final_score.mean(), 1)
    if len(filtered) > 0 else 0)

st.markdown("---")

# ── Tabs ──
tab1, tab2, tab3, tab4 = st.tabs([
    "🗺️ Map", "📊 Charts",
    "📋 Data Table", "🏫 School Profile"
])

with tab1:
    st.subheader("Risk Map")

    if len(filtered) > 0:
        center_lat = filtered.latitude.mean()
        center_lon = filtered.longitude.mean()
    else:
        center_lat, center_lon = 10.5, 78.5

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=6,
        tiles="CartoDB positron"
    )

    color_map = {
        "CRITICAL": "#CC0000",
        "HIGH":     "#FF6600",
        "MEDIUM":   "#FFAA00",
        "LOW":      "#2D8A4E"
    }

    # Use clustering for large datasets
    if len(filtered) > 50:
        cluster = MarkerCluster().add_to(m)
        add_to = cluster
    else:
        add_to = m

    for _, row in filtered.iterrows():
        color = color_map.get(row["risk_tier"], "gray")
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=7,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            tooltip=row["school_name"],
            popup=folium.Popup(
                f"<b>{row['school_name']}</b><br>"
                f"District: {row['district']}<br>"
                f"Country: {row['country']}<br>"
                f"Connectivity: {row['connectivity_status']}<br>"
                f"Score: {row['final_score']}<br>"
                f"Risk: <b>{row['risk_tier']}</b>",
                max_width=250
            )
        ).add_to(add_to)

    st_folium(m, width=1000, height=500)

with tab2:
    st.subheader("Risk Analysis Charts")

    ch1, ch2 = st.columns(2)

    with ch1:
        # Risk distribution
        risk_counts = filtered["risk_tier"].value_counts().reset_index()
        risk_counts.columns = ["Risk Tier", "Count"]
        fig1 = px.bar(
            risk_counts,
            x="Risk Tier", y="Count",
            color="Risk Tier",
            color_discrete_map=color_map,
            title="Risk Distribution",
            category_orders={"Risk Tier": [
                "CRITICAL", "HIGH", "MEDIUM", "LOW"
            ]}
        )
        fig1.update_layout(showlegend=False, height=350)
        st.plotly_chart(fig1, use_container_width=True)

    with ch2:
        # District risk heatmap
        dist_risk = filtered.groupby(
            ["district", "risk_tier"]
        ).size().reset_index(name="count")
        fig2 = px.bar(
            dist_risk,
            x="district", y="count",
            color="risk_tier",
            color_discrete_map=color_map,
            title="Risk by District",
            category_orders={"risk_tier": [
                "CRITICAL", "HIGH", "MEDIUM", "LOW"
            ]}
        )
        fig2.update_layout(
            height=350,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig2, use_container_width=True)

    ch3, ch4 = st.columns(2)

    with ch3:
        # Connectivity pie chart
        conn_counts = filtered[
            "connectivity_status"
        ].value_counts().reset_index()
        conn_counts.columns = ["Status", "Count"]
        fig3 = px.pie(
            conn_counts,
            values="Count",
            names="Status",
            title="Connectivity Status",
            color_discrete_sequence=["#2D8A4E", "#CC0000", "#FFAA00"]
        )
        fig3.update_layout(height=300)
        st.plotly_chart(fig3, use_container_width=True)

    with ch4:
        # Score distribution
        fig4 = px.histogram(
            filtered,
            x="final_score",
            color="risk_tier",
            color_discrete_map=color_map,
            title="Risk Score Distribution",
            nbins=20
        )
        fig4.update_layout(height=300)
        st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.subheader("School Data Table")

    # Top 50 most at risk
    st.markdown(f"Showing top 50 of {len(filtered)} schools by risk score")
    display_df = filtered[[
        "school_name", "district", "country",
        "risk_tier", "final_score",
        "connectivity_status"
    ]].sort_values(
        "final_score", ascending=False
    ).head(50)
    display_df.columns = [
        "School", "District", "Country",
        "Risk", "Score", "Connectivity"
    ]
    st.dataframe(display_df, height=400, hide_index=True)

    # Download
    csv = filtered.to_csv(index=False)
    st.download_button(
        label="Download all filtered schools (CSV)",
        data=csv,
        file_name="filtered_schools.csv",
        mime="text/csv"
    )

with tab4:
    st.subheader("School Profile")
    selected = st.selectbox(
        "Select a school",
        options=filtered["school_name"].tolist()
    )

    if selected:
        school = filtered[
            filtered.school_name == selected
        ].iloc[0]

        st.markdown(f"### {school['school_name']}")

        i1, i2, i3, i4 = st.columns(4)
        i1.metric("District", school["district"])
        i2.metric("Country", school["country"])
        i3.metric("Risk Tier", school["risk_tier"])
        i4.metric("Score", school["final_score"])

        i5, i6 = st.columns(2)
        i5.metric("Connectivity", school["connectivity_status"])
        i6.metric("Flood Score", school["flood_score"])

        # Mini map
        mini_map = folium.Map(
            location=[school["latitude"], school["longitude"]],
            zoom_start=12,
            tiles="CartoDB positron"
        )
        folium.CircleMarker(
            location=[school["latitude"], school["longitude"]],
            radius=15,
            color=color_map.get(school["risk_tier"], "gray"),
            fill=True,
            fill_opacity=0.8,
            tooltip=school["school_name"]
        ).add_to(mini_map)
        st_folium(mini_map, width=600, height=300)

st.markdown("---")
with st.expander("📖 Methodology"):
    st.markdown("""
    ### Risk Framework — IPCC H x E x V
    - **Hazard:** JRC Surface Water + GFD + Sentinel-1 SAR
    - **Exposure:** Coastal district classification
    - **Vulnerability:** Connectivity status

    ### Risk Tiers
    - 🚨 CRITICAL: Score >= 50
    - 🔴 HIGH: Score 25-50
    - 🟡 MEDIUM: Score 10-25
    - 🟢 LOW: Score < 10

    **Full code:** github.com/ayyanarh1/tamil-nadu-school-flood-risk
    """)

st.caption(
    "Data: Sentinel-1 SAR, JRC Surface Water, Global Flood Database, "
    "ERA5, IBTrACS Cyclones | "
    "github.com/ayyanarh1/tamil-nadu-school-flood-risk"
)
