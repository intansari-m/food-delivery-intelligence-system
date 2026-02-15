import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# ======================================================
# PAGE TITLE & STRATEGIC CONTEXT
# ======================================================

st.title("🚦 Traffic & Weather Analytics")

st.markdown("""
This module isolates environmental performance drivers
that structurally influence delivery efficiency.

While operational logistics determine baseline execution,
external volatility — traffic density and weather instability —
introduces nonlinear delay amplification.

This layer transforms environmental noise
into measurable structural intelligence.
""")

st.divider()

# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/Food_Delivery_Times_final.csv")

df = load_data()

delivery_col = "delivery_time_min"
traffic_col = "traffic_level"
weather_col = "weather"
time_col = "time_of_day"

# ======================================================
# BASELINE CALCULATION (Low Traffic + Clear Weather)
# ======================================================

baseline_df = df[
    (df[traffic_col] == "Low") &
    (df[weather_col] == "Clear")
]

baseline_mean = baseline_df[delivery_col].mean()

# ======================================================
# ENVIRONMENTAL SCOPE CONTROL
# ======================================================

st.header("🎛 Environmental Scope Control")

col1, col2, col3 = st.columns(3)

selected_time = col1.selectbox(
    "Time Segment",
    ["All"] + sorted(df[time_col].unique().tolist())
)

selected_traffic = col2.selectbox(
    "Traffic Level",
    ["All"] + sorted(df[traffic_col].unique().tolist())
)

selected_weather = col3.selectbox(
    "Weather Condition",
    ["All"] + sorted(df[weather_col].unique().tolist())
)

filtered_df = df.copy()

if selected_time != "All":
    filtered_df = filtered_df[filtered_df[time_col] == selected_time]

if selected_traffic != "All":
    filtered_df = filtered_df[filtered_df[traffic_col] == selected_traffic]

if selected_weather != "All":
    filtered_df = filtered_df[filtered_df[weather_col] == selected_weather]

st.divider()

# ======================================================
# KPI ROW – ENVIRONMENTAL PERFORMANCE SNAPSHOT
# ======================================================

st.header("📊 Environmental Performance Snapshot")

if len(filtered_df) > 0:

    avg_delay = round(filtered_df[delivery_col].mean(), 2)
    volatility = round(filtered_df[delivery_col].std(), 2)

    # STRUCTURAL ESCALATION RISK (vs baseline)
    if pd.notna(baseline_mean) and baseline_mean != 0:
        structural_risk = round(
            ((avg_delay - baseline_mean) / baseline_mean) * 100,
            2
        )
    else:
        structural_risk = 0

    # PERFORMANCE RISK (Top 25% Slowest Deliveries)
    threshold = filtered_df[delivery_col].quantile(0.75)
    performance_risk = round(
        len(filtered_df[filtered_df[delivery_col] >= threshold])
        / len(filtered_df) * 100,
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Average Delivery Time (min)", avg_delay)
    col2.metric("Volatility (Std Dev)", volatility)
    col3.metric("Structural Escalation (%)", f"{structural_risk}%")
    col4.metric("Performance Risk (%)", f"{performance_risk}%")

else:
    st.warning("No data available for selected scope.")

st.divider()

# ======================================================
# TRAFFIC INTELLIGENCE
# ======================================================

st.header("🚦 Traffic Density Intelligence")

if len(filtered_df) > 0:

    traffic_analysis = (
        filtered_df.groupby(traffic_col)[delivery_col]
        .agg(["mean", "median", "std", "count"])
        .sort_values("mean")
    )

    st.dataframe(traffic_analysis, use_container_width=True)

    fig_traffic = px.bar(
        traffic_analysis.reset_index(),
        x=traffic_col,
        y="mean",
        text_auto=True
    )

    st.plotly_chart(fig_traffic, use_container_width=True)

    st.markdown("""
Congestion introduces asymmetric performance degradation.

• Mean delivery time escalates under high density  
• Variability widens, signaling unstable execution  
• Volume clustering amplifies systemic stress  

Congestion elasticity must be embedded
within predictive ETA systems.
""")

st.divider()

# ======================================================
# WEATHER INTELLIGENCE
# ======================================================

st.header("🌧 Weather Sensitivity Intelligence")

if len(filtered_df) > 0:

    weather_analysis = (
        filtered_df.groupby(weather_col)[delivery_col]
        .agg(["mean", "median", "std", "count"])
        .sort_values("mean")
    )

    st.dataframe(weather_analysis, use_container_width=True)

    fig_weather = px.bar(
        weather_analysis.reset_index(),
        x=weather_col,
        y="mean",
        text_auto=True
    )

    st.plotly_chart(fig_weather, use_container_width=True)

    st.markdown("""
Environmental volatility amplifies operational uncertainty.

Weather does not operate independently —
its interaction with congestion compounds delay escalation.
""")

st.divider()

# ======================================================
# TRAFFIC × WEATHER INTERACTION
# ======================================================

st.header("⚠️ Compounded Environmental Interaction Matrix")

if len(filtered_df) > 0:

    interaction_matrix = (
        filtered_df.groupby([traffic_col, weather_col])[delivery_col]
        .mean()
        .reset_index()
    )

    fig_heatmap = px.density_heatmap(
        interaction_matrix,
        x=traffic_col,
        y=weather_col,
        z=delivery_col,
        text_auto=True
    )

    st.plotly_chart(fig_heatmap, use_container_width=True)

    st.markdown("""
Compounded environmental states
generate nonlinear delay expansion.

These intersections represent disproportionate:

• Compensation exposure  
• Customer dissatisfaction  
• Operational fragility  

Mitigation must prioritize compounded volatility,
not isolated factors.
""")

st.divider()

# ======================================================
# RISK INTERPRETATION LAYER
# ======================================================

st.header("📊 Risk Interpretation Layer")

if len(filtered_df) > 0:

    st.markdown(f"""
Within the selected analytical scope:

• **Structural Escalation:** {structural_risk}%  
  (Performance increase relative to stable baseline)

• **Performance Risk:** {performance_risk}%  
  (Top 25% slowest deliveries)

Structural escalation measures vulnerability.
Performance risk captures realized severity.

The divergence between these indicators
reveals system resilience capacity.
""")

st.divider()

# ======================================================
# EXECUTIVE SYNTHESIS
# ======================================================

st.header("💡 Executive Environmental Synthesis")

st.markdown("""
This module elevates environmental monitoring
from descriptive observation
to structured risk modeling.

It establishes:

• Baseline-relative escalation measurement  
• Congestion elasticity profiling  
• Weather sensitivity quantification  
• Compounded volatility detection  

By embedding environmental intelligence
into dispatch allocation systems,
organizations transition from reactive correction
to anticipatory optimization.

This strengthens systemic resilience
within the Food Delivery Intelligence Platform.
""")
