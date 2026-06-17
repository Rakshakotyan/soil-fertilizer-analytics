%%writefile app.py
import streamlit as st

# Set page configuration for a wider layout
st.set_page_config(layout="wide")

st.title("🌱 Soil Health & Fertilizer Advisor")
st.write("Enter your soil nutrient levels to get an instant recommendation.")

# Create a two-column layout: Left for inputs (sliders), Right for the reference chart
col1, col2 = st.columns([2, 1], gap="large")

# --- LEFT COLUMN: INPUT SLIDERS ---
with col1:
    st.subheader("📊 Your Soil Levels")
    
    # Sliders default to 20 and 7.00 as shown in your original screenshot
    nitrogen = st.slider("Nitrogen (N)", min_value=0, max_value=100, value=20)
    phosphorus = st.slider("Phosphorus (P)", min_value=0, max_value=100, value=20)
    potassium = st.slider("Potassium (K)", min_value=0, max_value=300, value=20)
    ph = st.slider("Soil pH", min_value=0.0, max_value=14.0, value=7.00, step=0.1)

# --- RIGHT COLUMN: THE "SHOULD BE" TARGET CHART ---
with col2:
    st.subheader("🎯 Ideal Target Levels")
    st.caption("Standard optimal guidelines for general crops")
    
    # Visual metric boxes showing what the values actually should be
    st.metric(label="Ideal Nitrogen (N)", value="40 - 80 ppm")
    st.metric(label="Ideal Phosphorus (P)", value="20 - 40 ppm")
    st.metric(label="Ideal Potassium (K)", value="150 - 250 ppm")
    st.metric(label="Ideal Soil pH", value="6.0 - 7.0 (Neutral)")

# --- DYNAMIC RECOMMENDATION LOGIC ---
st.markdown("---")

# Simple logic block based on your screenshot's output
if nitrogen < 40:
    recommendation = "High Nitrogen Fertilizer (Urea)"
elif potassium < 150:
    recommendation = "High Potassium Fertilizer (Muriate of Potash)"
elif phosphorus < 20:
    recommendation = "Phosphorus Rich Fertilizer (DAP)"
else:
    recommendation = "Your soil nutrients look well-balanced!"

# Display recommendation container
st.success(f"### ✅ Recommendation: {recommendation}")

st.info("This analysis is based on real-time nutrient input.")
