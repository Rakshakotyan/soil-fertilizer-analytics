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
# 2. DESIGN & STYLING (Custom CSS for Menu & Metrics)
# ==========================================
st.set_page_config(page_title="Soil Health Advisor", page_icon="🌱", layout="wide")

st.markdown("""
    <style>
    /* Style the Sidebar Menu Panel */
    [data-testid="stSidebar"] {
        background-color: #f4f7f4 !important;
        border-right: 2px solid #e2eee2;
        padding-top: 20px;
    }
    
    /* Give the Menu Target Boxes a sleek card border */
    .menu-target-box {
        background-color: #ffffff;
        border: 1px solid #e0ebd0;
        border-left: 4px solid #2e7d32; /* Green Indicator Accent */
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }
    
    /* Clean text alignment for menu titles */
    .menu-title {
        color: #1b5e20;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR MENU PANEL (Left Side)
# ==========================================
with st.sidebar:
    st.markdown('<div class="menu-title">🎯 Ideal Target Ranges</div>', unsafe_allow_html=True)
    st.caption("Standard crop benchmarks:")
    st.markdown("---")
    
    # Target Card 1
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Nitrogen (N)", value="40 - 80 ppm")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Target Card 2
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Phosphorus (P)", value="20 - 40 ppm")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Target Card 3
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Potassium (K)", value="150 - 250 ppm")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Target Card 4
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Ideal Soil pH", value="6.0 - 7.0")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 4. MAIN BODY CONTENT (Right Side)
# ==========================================
st.markdown('<h1 style="color: #1b5e20; font-weight:800;">🌱 Soil Health Dashboard</h1>', unsafe_allow_html=True)
st.write("Adjust your metrics here. Check the left menu panel anytime for target comparisons.")
st.markdown("---")

# Main adjustable controls
st.subheader("📊 Live Soil Inputs")
user_n = st.slider("Current Nitrogen (N)", 0, 100, 25)
user_p = st.slider("Current Phosphorus (P)", 0, 100, 15)
user_k = st.slider("Current Potassium (K)", 0, 300, 180)
ph = st.slider("Current Soil pH", 0.0, 14.0, 6.5, step=0.1)

# ==========================================
# 5. LIVE OUTPUT RESULTS
# ==========================================
st.markdown("---")
result = get_soil_advice(user_n, user_p, user_k)

st.success(f"### ✅ AI Recommendation: {result}")
st.info("💡 **UI Info:** The targets menu on the left will stay anchored in place while you test different slider metrics here.")
