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
# 2. DESIGN & STYLING (Sidebar Menu Customizations)
# ==========================================
st.set_page_config(page_title="Soil Health Advisor", page_icon="🌱", layout="wide")

st.markdown("""
    <style>
    /* Style the Left Sidebar Menu Panel */
    [data-testid="stSidebar"] {
        background-color: #f4f7f4 !important;
        border-right: 2px solid #e2eee2;
        padding-top: 20px;
    }
    
    /* Give Menu Items a clean card border */
    .menu-target-box {
        background-color: #ffffff;
        border: 1px solid #e0ebd0;
        border-left: 4px solid #2e7d32; /* Green Indicator Accent */
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }
    
    /* Title for the Left Sidebar Menu */
    .menu-title {
        color: #1b5e20;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 15px;
    }
    
    /* Centered Text Helpers */
    .center-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR MENU PANEL (Left Side Targets)
# ==========================================
with st.sidebar:
    st.markdown('<div class="menu-title">🎯 Ideal Target Ranges</div>', unsafe_allow_html=True)
    st.caption("Standard crop benchmarks:")
    st.markdown("---")
    
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Nitrogen (N)", value="40 - 80 ppm")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Phosphorus (P)", value="20 - 40 ppm")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Potassium (K)", value="150 - 250 ppm")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="menu-target-box">', unsafe_allow_html=True)
    st.metric(label="Ideal Soil pH", value="6.0 - 7.0")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 4. MAIN BODY CONTENT (Centering Mechanism)
# ==========================================
# Creating 3 columns: Left and Right act as padding, Middle (3) holds your app
pad_left, mid_col, pad_right = st.columns([1, 2.5, 1])

# Everything we build must now go inside 'with mid_col:' to keep it in the middle!
with mid_col:
    st.markdown('<h1 style="color: #1b5e20; font-weight:800; text-align: center;">🌱 Soil Health Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #555555;">Adjust your metrics below. The menu on the left
