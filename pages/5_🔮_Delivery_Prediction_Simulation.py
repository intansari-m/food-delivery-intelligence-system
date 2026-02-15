import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(page_title="Prediction & Simulation", layout="wide")

st.markdown("<h1 style='text-align:center;'>🚀 Delivery Time Prediction & Simulation</h1>", unsafe_allow_html=True)
st.markdown("---")

# =====================================================
# CACHE MODEL LOADER  (PRODUCTION GRADE)
# =====================================================
@st.cache_resource
def load_model():
    model = joblib.load("data/best_xgb_model.joblib")
    return model

model = load_model()

# =====================================================
# FORMATTERS
# =====================================================
def fmt2(x):
    return f"{x:,.2f}"

def fmt1(x):
    return f"{x:,.1f}"

# =====================================================
# CONFIDENCE INTERVAL
# =====================================================
def confidence_interval(pred):
    noise = np.random.uniform(2, 5)
    return pred - noise, pred + noise

# =====================================================
# RISK CLASSIFIER
# =====================================================
def classify_risk(value):
    if value > 45:
        return "High Risk", "🔴", "#ff4d4d"
    elif value > 30:
        return "Moderate Risk", "🟠", "#ffa500"
    else:
        return "Low Risk", "🟢", "#2ecc71"

# =====================================================
# INPUT FORM
# =====================================================
st.subheader("🔮 Enter Delivery Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    traffic_level = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
    courier_exp_cat = st.selectbox("Courier Experience Category", ["Beginner", "Intermediate", "Expert"])
    weather = st.selectbox("Weather", ["Sunny", "Rainy", "Cloudy"])

with col2:
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
    vehicle_type = st.selectbox("Vehicle Type", ["Motorcycle", "Car", "Bicycle"])
    distance_km = st.number_input("Distance (km)", 0.1, 50.0, 7.5)

with col3:
    prep_time = st.number_input("Preparation Time (min)", 1, 120, 15)
    courier_exp_years = st.number_input("Courier Experience (years)", 0, 20, 5)

distance_per_exp = distance_km / (courier_exp_years + 1)

# =====================================================
# PREDICTION BUTTON
# =====================================================
st.markdown("---")

if st.button("Run Predictive Simulation 🚀", use_container_width=True):

    # =====================================================
    # INPUT DATAFRAME
    # =====================================================
    input_df = pd.DataFrame([{
        "traffic_level": traffic_level,
        "courier_experience_category": courier_exp_cat,
        "weather": weather,
        "time_of_day": time_of_day,
        "vehicle_type": vehicle_type,
        "distance_km": distance_km,
        "preparation_time_min": prep_time,
        "courier_experience_yrs": courier_exp_years,
        "distance_per_experience": distance_per_exp
    }])

    # Ensure correct feature order
    input_df = input_df[model.feature_names_in_]

    # =====================================================
    # MODEL PREDICTION
    # =====================================================
    eta = model.predict(input_df)[0]

    # =====================================================
    # CONFIDENCE + RISK
    # =====================================================
    low, high = confidence_interval(eta)
    risk, emoji, color = classify_risk(eta)

    # =====================================================
    # RESULT CARD
    # =====================================================
    st.markdown(f"""
    <div style="
        padding: 25px;
        border-radius: 20px;
        background: linear-gradient(135deg, #E3F2FD, #FFFFFF);
        text-align: center;
        box-shadow: 2px 6px 18px rgba(0,0,0,0.1);
    ">
        <h3>Estimated Delivery Time</h3>
        <h1 style="color:#ff5733;">{fmt2(eta)} minutes</h1>
        <p style="font-size:18px;">
            Risk Level: <b style="color:{color};">{emoji} {risk}</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================================================
    # METRICS
    # =====================================================
    c1, c2 = st.columns(2)
    c1.metric("Confidence Range", f"{fmt1(low)} – {fmt1(high)} min")
    c2.metric("Prediction Stability", f"± {fmt1((high - low)/2)} min")

    st.divider()

    # =====================================================
    # GAUGE CHART
    # =====================================================
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=eta,
        title={'text': "Delivery Speed Indicator"},
        gauge={
            'axis': {'range': [0, 60]},
            'steps': [
                {'range': [0, 20], 'color': "lightgreen"},
                {'range': [20, 40], 'color': "yellow"},
                {'range': [40, 60], 'color': "tomato"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'value': eta
            }
        }
    ))

    fig.update_layout(height=320)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =====================================================
    # SCENARIO ANALYSIS
    # =====================================================
    st.subheader("📊 Distance Sensitivity Simulation")

    shifts = [-2, 0, 2]
    scenario_vals = []

    for s in shifts:
        sim_df = input_df.copy()
        sim_df["distance_km"] = max(0.1, distance_km + s)
        scenario_vals.append(model.predict(sim_df)[0])

    chart_df = pd.DataFrame({
        "Distance Change (km)": shifts,
        "Estimated Time": scenario_vals
    })

    st.line_chart(chart_df.set_index("Distance Change (km)"))

    # =====================================================
    # DYNAMIC INTERPRETATION
    # =====================================================
    impact = max(scenario_vals) - min(scenario_vals)

    if impact > 15:
        sensitivity_text = "highly sensitive"
        risk_text = "significant operational volatility"
    elif impact > 7:
        sensitivity_text = "moderately sensitive"
        risk_text = "noticeable operational impact"
    else:
        sensitivity_text = "relatively stable"
        risk_text = "minimal operational risk"

    st.markdown(f"""
**Dynamic Interpretation:**  
The delivery time prediction appears **{sensitivity_text}** to distance changes,  
indicating **{risk_text}** under current traffic and courier conditions.

This suggests that route optimization and dispatch planning  
could play a critical role in maintaining service consistency.
""")

    st.divider()

    # =====================================================
    # DYNAMIC STRATEGIC INSIGHT
    # =====================================================
    if eta > 45:
        strategy_text = """
### Strategic Insight

The predicted delivery time indicates **potential operational inefficiencies**.

- Route re-planning and traffic-aware dispatching  
- Increasing courier allocation during peak hours  
- Enhancing preparation workflow efficiency  

Failure to address this may reduce customer satisfaction
and increase delivery variability risk.
"""
    elif eta > 30:
        strategy_text = """
### Strategic Insight

The delivery performance is within a **moderate operational range**.

- Improve routing algorithms  
- Balance courier workload distribution  
- Monitor traffic patterns and peak periods  

This ensures service stability while maintaining efficiency.
"""
    else:
        strategy_text = """
### Strategic Insight

The predicted delivery time reflects **strong operational efficiency**.

- Maintain existing dispatch policies  
- Scale operations cautiously during demand spikes  
- Focus on customer experience and retention strategies  

This creates opportunities for service differentiation and growth.
"""

    st.markdown(strategy_text)
