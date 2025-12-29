import streamlit as st
from utils.predictor import load_or_create_model, predict_soil
from data.crop_mapping import soil_crop_map

# Load or create model
model = load_or_create_model()

st.set_page_config(
    page_title="Soil Classification & Crop Recommendation",
    layout="centered"
)

st.title("🌱 Soil Classification & Crop Recommendation")
st.write(
    "Enter soil parameters to identify soil type and get suitable crops for sustainable farming."
)

# Input fields
nitrogen = st.number_input("Nitrogen (N)", 0, 200, 50)
phosphorus = st.number_input("Phosphorus (P)", 0, 200, 50)
potassium = st.number_input("Potassium (K)", 0, 200, 50)
ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
moisture = st.number_input("Moisture (%)", 0.0, 100.0, 30.0)

if st.button("Analyze Soil"):
    soil_type = predict_soil(model, nitrogen, phosphorus, potassium, ph, moisture)

    st.success(f"🪴 Predicted Soil Type: **{soil_type}**")

    crops = soil_crop_map.get(soil_type, [])
    if crops:
        st.subheader("🌾 Suitable Crops")
        for crop in crops:
            st.write(f"- {crop}")
    else:
        st.warning("No crop recommendations available for this soil type.")
