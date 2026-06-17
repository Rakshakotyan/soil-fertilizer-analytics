import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. CORE AI LOGIC
# ==========================================
def get_soil_advice(n, p, k):
    if n < 30:
        return "High Nitrogen Fertilizer (Urea)"
    elif p < 20:
        return "High Phosphorus Fertilizer (DAP)"
    elif k < 20:
        return "High Potassium Fertilizer (MOP)"
    else:
        return "Soil is Healthy! (Add Organic Compost)"

# ==========================================
# 2. DESIGN & STYLING (The "Good Design" Part)
# ==========================================
st.set_page_config(page_title="Soil Health Advisor", page_icon="🌱", layout="wide")

# Inject Custom CSS for professional cards and borders
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #fdfdfd;
    }
    
    /* Target Level Card Container */
    .target-container {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #2e7d32; /* Nature Green Accent */
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
    }
    
    /* Individual Metric Boxes */
    div[data-testid="stMetric"] {
        background-color: #f9fbf9;
        border: 1px solid #eef2ee;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    
    /* Custom Title Styling */
    .main-title {
        color: #1b5e20;
        font-weight: 800;
        letter-spacing: -1px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. WEBSITE CONTENT
# ==========================================
st.markdown('<h1 class="main-title">🌱 Soil Health & Fertilizer Advisor</h1>', unsafe_allow_html=True)
st.write("Real-time nutrient analysis dashboard for precision agriculture.")
st.markdown("---")

# Layout: 2 Columns
col1, col2 = st.columns([1.8, 1], gap="large")

with col1:
    st.subheader("📊 Live Soil Inputs")
    user_n = st.slider("Nitrogen (N)", 0, 100, 20)
    user_p = st.slider("Phosphorus (P)", 0, 100, 20)
    user_k = st.slider("Potassium (K)", 0, 300, 20)
    ph = st.slider("Soil pH", 0.0, 14.0, 7.0, step=0.1)

with col2:
    # --- STYLED TARGET CARD ---
    st.markdown('<div class="target-container">', unsafe_allow_html=True)
    st.subheader("🎯 Ideal Target Ranges")
    st.caption("Baseline requirements for maximum crop yield:")
    
    st.metric(label="Nitrogen (N) Target", value="40 - 80 ppm")
    st.metric(label="Phosphorus (P) Target", value="20 - 40 ppm")
    st.metric(label="Potassium (K) Target", value="150 - 250 ppm")
    st.metric(label="Ideal pH", value="6.0 - 7.0")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 4. OUTPUT RESULTS
# ==========================================
st.markdown("---")
result = get_soil_advice(user_n, user_p, user_k)

# Beautiful Result Display
st.success(f"### ✅ AI Recommendation: {result}")

st.info("💡 **Dashboard insight:** Adjust the sliders to match your lab report. The recommendation will update automatically based on the detected nutrient gaps.")
