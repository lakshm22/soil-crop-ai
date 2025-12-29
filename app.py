import streamlit as st
from utils.predictor import load_or_create_model, predict_soil
from data.crop_mapping import soil_crop_map, crop_guidance

# Load or create model
model = load_or_create_model()

# Page config
st.set_page_config(
    page_title="Soil Classification & Crop Recommendation",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("🌱 AI- Powered Soil Classification & Crop Recommendation")
    st.write("""
    Classifies soil and suggests suitable crops with detailed growing tips.
    """)
    
    st.subheader("⚒️ Tech Stack")
    st.write("- Python") 
    st.write("- Scikit-learn (Decision Tree Classifier)")
    st.write("- Streamlit")
    st.write("- Pandas")
    st.write("- NumPy")
    
    st.subheader("🌏 Sustainable Development Goals (SDGs)")
    st.write("SDG 2: Zero Hunger – Promote sustainable agriculture and improve food security.")  
    st.write("SDG 13: Climate Action – Reduce resource wastage and optimize farming.")  
    st.write("SDG 15: Life on Land – Sustainably manage soil and land resources.")

st.sidebar.markdown("---")
st.sidebar.caption("Created by [Lakshitha M](https://github.com/lakshm22)")

# Main area
st.title("🌾 Soil Classification & Crop Recommendation")
st.markdown("Enter soil parameters to identify soil type and view crops with growing tips.")

# Input fields in columns
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
        st.subheader("🌾 Suitable Crops & Growing Tips")
        
        for crop in crops:
            details = crop_guidance.get(crop)
            if details:
                with st.expander(f"🌱 {crop}"):
                    col_a, col_b = st.columns([1, 2])
                    with col_a:
                        st.markdown(f"**Soil:** {details['Soil']}")
                        st.markdown(f"**Watering:** {details['Watering']}")
                        st.markdown(f"**Sunlight:** {details['Sunlight']}")
                        st.markdown(f"**Temperature:** {details['Temperature']}")
                    with col_b:
                        st.markdown(f"**Fertilization:** {details['Fertilization']}")
                        st.markdown(f"**Spacing:** {details['Spacing']}")
                        st.markdown(f"**Harvest:** {details['Harvest']}")
                        st.markdown(f"**Pests/Diseases:** {details['Pests/Diseases']}")
                        st.markdown(f"**Tips:** {details['Tips']}")
            else:
                st.info(f"{crop} – No guidance available.")
    else:
        st.warning("No crop recommendations available for this soil type.")
