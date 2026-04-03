import streamlit as st
import pandas as pd

# Title of your Web App
st.title("🌱 Soil Health & Fertilizer Advisor")
st.write("Enter your soil nutrient levels to get an instant recommendation.")

# 1. User Input Sliders
n = st.slider("Nitrogen (N)", 0, 100, 20)
p = st.slider("Phosphorus (P)", 0, 100, 20)
k = st.slider("Potassium (K)", 0, 100, 20)
ph = st.slider("Soil pH", 0.0, 14.0, 7.0)

# 2. Recommendation Logic
def get_advice(n, p, k, ph):
    if n < 30: return "High Nitrogen Fertilizer (Urea)"
    if p < 20: return "High Phosphorus (DAP)"
    if k < 20: return "High Potassium (MOP)"
    if ph < 6.0: return "Acidic Soil (Add Lime)"
    if ph > 7.5: return "Alkaline Soil (Add Gypsum)"
    return "Your Soil is Healthy! Use Organic Compost."

# 3. Display Result
result = get_advice(n, p, k, ph)

st.subheader(f"✅ Recommendation: {result}")
st.info("This analysis is based on real-time nutrient input.")
