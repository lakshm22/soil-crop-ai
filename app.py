import streamlit as st
from utils.predictor import load_or_create_model, predict_soil
from data.crop_mapping import soil_crop_map, crop_guidance

model = load_or_create_model()

# Page config
st.set_page_config(
    page_title="Soil Classification & Crop Recommendation",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("🌱 Project Info")
    st.write("""
    **AI for Sustainability: Soil Classification & Crop Recommendation**  
    - Classifies soil based on nutrient levels.  
    - Suggests suitable crops with guidance for optimal growth.
    """)
    
    st.subheader("Tools & Stack")
    st.write("- Python 3") 
    st.write("- Scikit-learn (Decision Tree Classifier)")
    st.write("- Streamlit for UI")
    st.write("- Pandas & NumPy for data handling")
    
    st.subheader("Sustainable Development Goals (SDGs)")
    st.write("2️⃣ SDG 2: Zero Hunger – Promote sustainable agriculture and improve food security.")  
    st.write("13️⃣ SDG 13: Climate Action – Reduce resource wastage and optimize farming for climate resilience.")  
    st.write("15️⃣ SDG 15: Life on Land – Sustainably manage soil and land resources.")
st.sidebar.markdown("---")
st.sidebar.caption("Created by [Lakshitha M](https://github.com/lakshm22)")

# Main area
st.title("🌾 Soil Classification & Crop Recommendation")
st.markdown(
    "Enter the soil parameters below to identify the soil type and view suitable crops with guidance for best harvest."
)

# Input columns for clean UI
col1, col2, col3 = st.columns(3)

with col1:
    nitrogen = st.number_input("Nitrogen (N)", 0, 200, 50)
    phosphorus = st.number_input("Phosphorus (P)", 0, 200, 50)

with col2:
    potassium = st.number_input("Potassium (K)", 0, 200, 50)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)

with col3:
    moisture = st.number_input("Moisture (%)", 0.0, 100.0, 30.0)

# Prediction
if st.button("Analyze Soil"):
    soil_type = predict_soil(model, nitrogen, phosphorus, potassium, ph, moisture)
    st.success(f"🪴 Predicted Soil Type: **{soil_type}**")

    crops = soil_crop_map.get(soil_type, [])
    if crops:
        st.subheader("🌾 Suitable Crops and Growing Tips")
        for crop in crops:
            guidance = crop_guidance.get(crop, "Follow standard cultivation practices for this crop.")
            st.markdown(f"- **{crop}**: {guidance}")
    else:
        st.warning("No crop recommendations available for this soil type.")
