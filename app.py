import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Food Delivery Intelligence & Predictive Operations System",
    page_icon="🚚",
    layout="wide"
)

# ======================
# HERO SECTION
# ======================
st.title("🚚 Food Delivery Intelligence & Predictive Operations System")

st.markdown("""
An **end-to-end operational analytics & predictive intelligence system**
built to forecast delivery time, uncover delay drivers,
and enable data-driven logistics optimization.

This platform transforms operational data into
**strategic decision intelligence for last-mile delivery performance**.
""")

st.divider()

# ======================
# INDUSTRY + BUSINESS PROBLEM (SIDE BY SIDE)
# ======================
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.header("🌍 Industry Context")
        st.markdown("""
The food delivery industry is one of the most competitive and
operationally complex ecosystems today.

Customers expect:

- ⏱ Fast delivery  
- 📍 Accurate ETA prediction  
- ⭐ Consistent service quality  

Even small delivery delays can result in:

- Increased refund & compensation cost  
- Lower app ratings  
- Reduced customer retention  
- Brand trust erosion  

In high-volume environments, **operational inefficiency scales exponentially**.

Therefore, predictive intelligence becomes critical —  
not just for monitoring performance,  
but for preventing delays before they occur.
""")

with col2:
    with st.container(border=True):
        st.header("📌 Business Problem")
        st.markdown("""
Traditional operational dashboards are reactive.

They show what already happened —  
but do not help anticipate future delivery risks.

Key operational questions addressed in this system:

- Which factors most impact delivery time?
- How does traffic condition influence ETA?
- Does weather significantly increase delay?
- Which courier performance patterns predict inefficiency?
- Can we simulate scenarios before peak hours?

This system addresses these gaps  
through predictive modeling and operational analytics.
""")

st.divider()

# ======================
# OBJECTIVES + MODELING (SIDE BY SIDE)
# ======================
col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.header("🎯 Project Objectives")
        st.markdown("""
The project aims to:

- Predict food delivery time using supervised machine learning  
- Identify primary operational delay drivers  
- Quantify traffic and weather impact  
- Enable scenario-based ETA simulation  
- Provide strategic logistics recommendations  
- Deploy an interactive intelligence dashboard  

The objective is not only prediction accuracy,  
but **decision-grade operational insight**.
""")

with col4:
    with st.container(border=True):
        st.header("🤖 Modeling Strategy")
        st.markdown("""
Several regression algorithms were evaluated:

- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- XGBoost Regressor  

Feature engineering included:

- Distance calculation  
- Traffic condition encoding  
- Weather categorization  
- Courier experience metrics  
- Time-of-day segmentation  

Model performance was evaluated using:

- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- Cross-validation stability  
""")

st.success("""
✅ Final Production Model: XGBoost Regressor

- Highest predictive performance  
- Strong nonlinear relationship capture  
- Stable cross-validation results  
- High feature importance interpretability  

The model is suitable for real-time ETA estimation
and operational decision support.
""")

st.divider()

# ======================
# CAPABILITIES + IMPACT (SIDE BY SIDE)
# ======================
col5, col6 = st.columns(2)

with col5:
    with st.container(border=True):
        st.header("⚙️ System Capabilities")
        st.markdown("""
This system enables stakeholders to:

- 📊 Monitor operational KPIs  
- 🚦 Analyze traffic impact on delivery speed  
- 🌧 Evaluate weather-driven delay patterns  
- 🏍 Assess courier performance  
- 🔮 Simulate ETA predictions  
- 💡 Design operational intervention strategies  

The platform bridges analytics,  
predictive modeling,  
and strategic operations management.
""")

with col6:
    with st.container(border=True):
        st.header("💰 Strategic & Financial Impact")
        st.markdown("""
With predictive delivery intelligence,
companies can:

- Reduce late delivery rates  
- Optimize courier allocation  
- Improve ETA accuracy  
- Reduce compensation cost  
- Increase customer satisfaction scores  
- Improve long-term retention  

Even improving average delivery time
by 5–10% during peak traffic hours
can significantly enhance brand perception
and operational efficiency.
""")

st.divider()

# ======================
# NAVIGATION
# ======================
with st.container(border=True):
    st.markdown("""
👉 Use the sidebar to explore:

- 📊 Executive Dashboard  
- 🚦 Traffic & Weather Analytics  
- 🏍 Courier Performance Analysis  
- 🤖 Model Intelligence  
- 🔮 Delivery Time Simulation  
- 💡 Strategic Recommendations  
- 👤 About the Analyst  
""")

st.success("✅ System ready for operational and strategic exploration.")
