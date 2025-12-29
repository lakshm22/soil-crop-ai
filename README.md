# 🌱 Soil Crop AI - Soil Classification & Crop Recommendation 

[Soil Crop AI](https://soil-crop-ai-hwe7hdwhw9d8jakc4bdor5.streamlit.app/) is an AI-powered project that classifies soil based on nutrient levels and other parameters, and recommends suitable crops along with detailed growing tips for sustainable agriculture.

---

## Project Description

This project uses a **pre-trained Decision Tree model** to classify soil types (Sandy, Clay, Loamy, Silt) based on key soil parameters: Nitrogen (N), Phosphorus (P), Potassium (K), pH, and moisture.  
Once the soil type is predicted, the app provides a list of **suitable crops** along with **detailed growing guidance** including soil requirements, watering, sunlight, fertilization, spacing, harvest, common pests, and best-practice tips.

The app is built with **Python** and **Streamlit**, making it easy to run locally or deploy as a web app.

---

## Sustainable Development Goals (SDGs) Addressed

- **SDG 2: Zero Hunger** 
- **SDG 13: Climate Action** 
- **SDG 15: Life on Land** 

---

## Features

- Predict soil type from user input parameters.
- Suggest suitable crops for each soil type.
- Provide detailed growing guidance for the best harvest.
- Clean and interactive UI using Streamlit.
- Uses a pre-trained model (`soil_model.pkl`) loaded with `joblib`.

---

## Tools & Stack

- `Python`
- `Scikit-learn` (Decision Tree Classifier)
- `Streamlit`
- `Pandas`
- `NumPy`
- `Joblib`

---

## Project Structure

<pre>
soil-crop-ai/
│                    
├── data/
│   ├── __init__.py
│   └── crop_mapping.py         # Soil-crop mapping and growing guidance
├── utils/
│   ├── __init__.py
│   └── predictor.py            # Model loading and prediction functions
├── .gitignore
├── README.md
├── app.py                      # Main Streamlit app
└── requirements.txt
</pre>

---

## Demo
Check out the live app here: [Soil Crop AI](https://soil-crop-ai-hwe7hdwhw9d8jakc4bdor5.streamlit.app/)
