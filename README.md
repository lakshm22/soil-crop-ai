# 🌱 Soil Crop AI - Soil Classification & Crop Recommendation 

[Soil Crop AI](https://soil-crop-ai-hwe7hdwhw9d8jakc4bdor5.streamlit.app/) is an AI-powered project that classifies soil based on nutrient levels and other parameters, and recommends suitable crops along with detailed growing tips for sustainable agriculture.

---

## Project Description

This project uses a **pre-trained Decision Tree model** to classify soil types (Sandy, Clay, Loamy, Silt) based on key soil parameters: Nitrogen (N), Phosphorus (P), Potassium (K), pH, and moisture.  
Once the soil type is predicted, the app provides a list of **suitable crops** along with **detailed growing guidance** including soil requirements, watering, sunlight, fertilization, spacing, harvest, common pests, and best-practice tips.

The app is built with **Python** and **Streamlit**, making it easy to run locally or deploy as a web app.

---

## Sustainable Development Goals (SDGs) Addressed

- **SDG 2: Zero Hunger** – Promote sustainable agriculture and improve food security.  
- **SDG 13: Climate Action** – Optimize farming and reduce resource wastage.  
- **SDG 15: Life on Land** – Sustainably manage soil and land resources.

---

## Features

- Predict soil type from user input parameters.
- Suggest suitable crops for each soil type.
- Provide detailed growing guidance for best harvest.
- Clean and interactive UI using Streamlit.
- Auto-generates the model if not present (`soil_model.pkl`).

---

## Tools & Stack

- **Python 3**
- **Scikit-learn** (Decision Tree Classifier)
- **Streamlit** for UI
- **Pandas & NumPy** for data handling

---

## Project Structure

<pre>
soil-crop-ai/
│
├── app.py                     # Main Streamlit app
├── data/
│   ├── __init__.py
│   ├── crop_mapping.py         # Soil-crop mapping and growing guidance
└── utils/
    ├── __init__.py
    └── predictor.py            # Model loading and prediction functions
</pre>

---

## Demo
Check out the live app here: [Soil Crop AI](https://soil-crop-ai-hwe7hdwhw9d8jakc4bdor5.streamlit.app/)
