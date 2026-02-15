import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# ======================================================
# PAGE TITLE — EXECUTIVE HIERARCHY
# ======================================================

st.title("📊 Executive Operational Intelligence Dashboard")

st.markdown("""
This Executive Dashboard functions as the strategic command center
for monitoring delivery performance across the food logistics ecosystem.

Rather than presenting isolated metrics,
this interface synthesizes operational data into
decision-grade intelligence.

Executives require clarity on systemic efficiency,
risk concentration,
and environmental sensitivity —
not fragmented analytics.
""")

st.divider()

# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/Food_Delivery_Times_final.csv")
    return df

df = load_data()

# ======================================================
# DATA STRUCTURE ALIGNMENT
# ======================================================

delivery_col = "delivery_time_min"
distance_col = "distance_km"
traffic_col = "traffic_level"
weather_col = "weather"
time_col = "time_of_day"

# ======================================================
# STRATEGIC SCOPE CONTROL
# ======================================================

st.header("🎛 Strategic Scope Control")

st.markdown("""
This control panel allows executive-level scope adjustment
to evaluate structural performance sensitivity
under different operational conditions.

The objective is not granular filtering —
but strategic scenario framing.
""")

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

# Apply Filters
filtered_df = df.copy()

if selected_time != "All":
    filtered_df = filtered_df[filtered_df[time_col] == selected_time]

if selected_traffic != "All":
    filtered_df = filtered_df[filtered_df[traffic_col] == selected_traffic]

if selected_weather != "All":
    filtered_df = filtered_df[filtered_df[weather_col] == selected_weather]

st.divider()

# ======================================================
# KPI CALCULATIONS
# ======================================================

avg_delivery = round(filtered_df[delivery_col].mean(), 2)

late_threshold = 40
late_rate = round((filtered_df[delivery_col] > late_threshold).mean() * 100, 2)

avg_distance = round(filtered_df[distance_col].mean(), 2)

if len(filtered_df) > 0:
    peak_period = (
        filtered_df.groupby(time_col)[delivery_col]
        .mean()
        .sort_values(ascending=False)
        .index[0]
    )
else:
    peak_period = "N/A"

# ======================================================
# CORE PERFORMANCE INDICATORS
# ======================================================

st.header("📌 Core Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Delivery Time (minutes)", avg_delivery)
col2.metric("Late Delivery Rate (%)", late_rate)
col3.metric("Peak Risk Time Segment", peak_period)
col4.metric("Average Delivery Distance (km)", avg_distance)

st.markdown(f"""
Interpretation:

• Average delivery time under selected scope: **{avg_delivery} minutes**  
• Deliveries exceeding {late_threshold} minutes: **{late_rate}%**  
• Highest delay concentration occurs during: **{peak_period}**  
• Average delivery radius: **{avg_distance} km**

These metrics dynamically adapt
to the selected strategic scope,
allowing executive-level sensitivity evaluation.
""")

st.divider()

# ======================================================
# TIME SEGMENT ANALYSIS
# ======================================================

st.header("📈 Time-of-Day Performance Distribution")

if len(filtered_df) > 0:
    time_trend = (
        filtered_df.groupby(time_col)[delivery_col]
        .mean()
        .sort_values()
    )
    st.bar_chart(time_trend)
else:
    st.warning("No data available for selected filter combination.")

st.markdown("""
Temporal clustering reveals structural demand pressure patterns.

Evening and peak windows typically exhibit
increased systemic stress.

Strategic capacity alignment
should prioritize high-volatility periods.
""")

st.divider()

# ======================================================
# TRAFFIC IMPACT ANALYSIS
# ======================================================

st.header("🚦 Traffic Impact Intelligence")

if len(filtered_df) > 0:
    traffic_analysis = (
        filtered_df.groupby(traffic_col)[delivery_col]
        .mean()
        .sort_values()
    )
    st.bar_chart(traffic_analysis)

st.markdown("""
Traffic congestion introduces nonlinear delay expansion.

High congestion levels often trigger
disproportionate performance degradation.

Embedding predictive traffic modeling
into ETA systems enhances resilience.
""")

st.divider()

# ======================================================
# WEATHER SENSITIVITY ANALYSIS
# ======================================================

st.header("🌧 Weather Sensitivity Overview")

if len(filtered_df) > 0:
    weather_analysis = (
        filtered_df.groupby(weather_col)[delivery_col]
        .mean()
        .sort_values()
    )
    st.bar_chart(weather_analysis)

st.markdown("""
Environmental volatility amplifies uncertainty.

Adverse weather increases delay dispersion,
affecting reliability and courier safety.

Proactive environmental modeling
reduces structural inefficiency.
""")

st.divider()

# ======================================================
# COMPOUNDED RISK EXPOSURE
# ======================================================

st.header("⚠️ Compounded Environmental Risk Exposure")

if len(filtered_df) > 0:
    high_risk = filtered_df[
        (filtered_df[traffic_col] == "High") &
        (filtered_df[weather_col] != "Clear")
    ]

    risk_rate = round(len(high_risk) / len(filtered_df) * 100, 2)

    st.markdown(f"""
    Under the selected scope,
    **{risk_rate}%** of deliveries occur under compounded stress conditions
    (High Traffic + Non-Clear Weather).

    These scenarios disproportionately contribute to:
    • Delay escalation  
    • Compensation exposure  
    • Operational fatigue  

    Predictive mitigation strategies
    should prioritize this segment.
    """)
else:
    st.warning("No data available for compounded risk calculation.")

st.divider()

# ======================================================
# EXECUTIVE SYNTHESIS
# ======================================================

st.header("💡 Executive Synthesis")

st.markdown("""
This dashboard establishes a dynamic executive decision layer.

By adjusting strategic scope,
leadership can evaluate:

• Environmental sensitivity  
• Temporal volatility  
• Structural congestion impact  
• System-wide delay elasticity  

The objective is not only operational visibility —
but forward-looking strategic optimization.

This module forms the foundational layer
of the broader Food Delivery Intelligence System.
""")
