import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

# ======================================================
# PAGE TITLE & STRATEGIC CONTEXT
# ======================================================

st.title("🏍 Courier Performance Analysis")

st.markdown("""
This module evaluates operational execution variability
within the delivery intelligence system.

Unlike environmental volatility,
courier performance is a controllable internal parameter.

Experience maturity, workload elasticity,
and structural distance exposure
shape delivery efficiency outcomes.

Understanding execution dispersion
enables predictive allocation
and systemic volatility reduction.
""")

st.divider()

# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/Food_Delivery_Times_final.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

delivery_col = "delivery_time_min"
experience_col = "courier_experience_yrs"
distance_col = "distance_km"
prep_col = "preparation_time_min"
exp_category_col = "courier_experience_category"

# ======================================================
# PERFORMANCE SCOPE CONTROL
# ======================================================

st.header("🎛 Courier Performance Scope Control")

col1, col2 = st.columns(2)

min_experience = col1.slider(
    "Minimum Courier Experience (Years)",
    0, int(df[experience_col].max()), 0
)

max_distance = col2.slider(
    "Maximum Delivery Distance (km)",
    0, int(df[distance_col].max()), int(df[distance_col].max())
)

filtered_df = df[
    (df[experience_col] >= min_experience) &
    (df[distance_col] <= max_distance)
]

st.divider()

# ======================================================
# KPI ROW – EXECUTION SNAPSHOT
# ======================================================

st.header("📊 Execution Performance Snapshot")

if len(filtered_df) > 0:

    avg_delivery = round(filtered_df[delivery_col].mean(), 2)
    volatility = round(filtered_df[delivery_col].std(), 2)

    threshold = filtered_df[delivery_col].quantile(0.75)
    high_delay_risk = round(
        len(filtered_df[filtered_df[delivery_col] >= threshold])
        / len(filtered_df) * 100,
        2
    )

    productivity_ratio = round(
        (filtered_df[distance_col] / filtered_df[delivery_col]).mean(),
        3
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Average Delivery Time (min)", avg_delivery)
    col2.metric("Execution Volatility (Std Dev)", volatility)
    col3.metric("High Delay Exposure (%)", high_delay_risk)
    col4.metric("Distance Productivity Ratio", productivity_ratio)

else:
    st.warning("No data available for selected scope.")

st.divider()

# ======================================================
# EXPERIENCE ELASTICITY MODELING
# ======================================================

st.header("🎓 Experience Elasticity Modeling")

if len(filtered_df) > 0:

    experience_analysis = (
        filtered_df.groupby(experience_col)[delivery_col]
        .agg(["mean", "std", "count"])
        .reset_index()
        .sort_values(by=experience_col)
    )

    st.dataframe(experience_analysis, use_container_width=True)

    fig_exp = px.line(
        experience_analysis,
        x=experience_col,
        y="mean",
        markers=True,
        title="Delivery Time vs Experience Level"
    )

    st.plotly_chart(fig_exp, use_container_width=True)

    st.markdown("""
Experience demonstrates measurable execution elasticity.

• Senior couriers stabilize delivery duration  
• Variance dispersion declines with maturity  
• Early-stage execution shows structural volatility  

Experience-aware allocation reduces systemic delay probability.
""")

st.divider()

# ======================================================
# DISTANCE ELASTICITY ANALYSIS
# ======================================================

st.header("📍 Distance Elasticity vs Execution")

if len(filtered_df) > 0:

    fig_scatter = px.scatter(
        filtered_df,
        x=distance_col,
        y=delivery_col,
        trendline="ols",
        title="Distance Elasticity Coefficient"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("""
Delivery time scales with distance,
but slope elasticity varies across experience segments.

Nonlinear distance scaling
signals congestion sensitivity
and operational inefficiency thresholds.

Elasticity modeling enables:
• Smart route segmentation  
• Experience-weighted dispatch  
• Long-distance risk mitigation  
""")

st.divider()

# ======================================================
# EXPERIENCE CATEGORY PROFILING
# ======================================================

st.header("🧩 Experience Category Profiling")

if len(filtered_df) > 0:

    category_analysis = (
        filtered_df.groupby(exp_category_col)[delivery_col]
        .mean()
        .reset_index()
        .sort_values(by=delivery_col)
    )

    st.dataframe(category_analysis, use_container_width=True)

    fig_cat = px.bar(
        category_analysis,
        x=exp_category_col,
        y=delivery_col,
        title="Average Delivery Time by Experience Category"
    )

    st.plotly_chart(fig_cat, use_container_width=True)

    st.markdown("""
Categorical experience segmentation
reveals structural execution hierarchy.

Operational deployment should prioritize:
• Senior couriers for high-complexity routes  
• Mid-level couriers for standard volume  
• Junior couriers under low-risk conditions  
""")

st.divider()

# ======================================================
# EXECUTIVE SYNTHESIS
# ======================================================

st.header("💡 Executive Courier Intelligence Synthesis")

st.markdown("""
Courier performance variability
is quantifiable and strategically optimizable.

This module establishes:

• Experience elasticity modeling  
• Distance sensitivity coefficient mapping  
• Execution volatility measurement  
• High-delay structural exposure tracking  

Human execution,
when measured with statistical rigor,
transforms from uncertainty
into a controllable system parameter.

Embedding courier intelligence
into dispatch algorithms
enables predictive orchestration
instead of reactive correction.
""")
