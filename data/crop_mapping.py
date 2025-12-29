# Soil type crops mapping
soil_crop_map = {
    "Sandy": ["Carrot", "Groundnut", "Watermelon", "Cucumber"],
    "Clay": ["Rice", "Broccoli", "Cabbage", "Soybean"],
    "Loamy": ["Wheat", "Tomato", "Sugarcane", "Cotton"],
    "Silt": ["Potato", "Onion", "Beans", "Lettuce"]
}

# Detailed crop guidance
crop_guidance = {
    "Carrot": {
        "Soil": "Loose, sandy soil, well-drained",
        "Watering": "Moderate, frequent to keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Light compost or balanced NPK; avoid excess nitrogen",
        "Temperature": "16–21°C optimal",
        "Spacing": "2–3 cm between seeds, 25–30 cm between rows",
        "Harvest": "70–80 days, when roots reach maturity",
        "Pests/Diseases": "Aphids, carrot fly; practice crop rotation",
        "Tips": "Thin seedlings to prevent crowding; mulch to retain moisture"
    },
    "Groundnut": {
        "Soil": "Sandy, well-drained soil",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen during flowering, phosphorus at planting",
        "Temperature": "25–30°C optimal",
        "Spacing": "30–40 cm between plants, 60 cm between rows",
        "Harvest": "120–150 days, leaves yellow and pods mature",
        "Pests/Diseases": "Aphids, leaf spot; rotate crops",
        "Tips": "Ensure loose soil for pod development; avoid overwatering"
    },
    "Watermelon": {
        "Soil": "Sandy loam",
        "Watering": "Deep watering 1–2 times per week",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced fertilizer; high potassium during fruiting",
        "Temperature": "20–30°C",
        "Spacing": "100–150 cm between plants, 200–300 cm between rows",
        "Harvest": "80–100 days, fruit skin hardens",
        "Pests/Diseases": "Aphids, powdery mildew; use trellising if space-limited",
        "Tips": "Provide ample space for vines; water at base to avoid fungus"
    },
    "Cucumber": {
        "Soil": "Sandy to loamy",
        "Watering": "Keep soil consistently moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen during vegetative stage; potassium during flowering",
        "Temperature": "18–24°C",
        "Spacing": "30–50 cm between plants, 100 cm between rows",
        "Harvest": "50–70 days, harvest green and firm cucumbers",
        "Pests/Diseases": "Powdery mildew, aphids; rotate crops",
        "Tips": "Use trellis for climbing varieties; mulch to retain moisture"
    },
    "Rice": {
        "Soil": "Clay soil with good water retention",
        "Watering": "Flooded or continuously moist",
        "Sunlight": "Full sun",
        "Fertilization": "Split doses of NPK during growth stages",
        "Temperature": "20–35°C",
        "Spacing": "20×20 cm seedlings",
        "Harvest": "120–150 days, grains harden",
        "Pests/Diseases": "Stem borer, leaf blight; rotate with legumes",
        "Tips": "Maintain water depth properly; remove weeds regularly"
    },
    "Broccoli": {
        "Soil": "Clay-loam, rich in organic matter",
        "Watering": "Consistent, keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen-rich fertilizer during growth",
        "Temperature": "15–20°C",
        "Spacing": "45 cm between plants, 60 cm between rows",
        "Harvest": "80–100 days, harvest head before flowering",
        "Pests/Diseases": "Cabbage worm, aphids; rotate crops",
        "Tips": "Mulch to retain moisture; remove yellow leaves"
    },
    "Cabbage": {
        "Soil": "Fertile clay soil",
        "Watering": "Moderate, regular",
        "Sunlight": "Full sun",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "15–20°C",
        "Spacing": "30–45 cm between plants, 60–70 cm between rows",
        "Harvest": "70–120 days, harvest firm heads",
        "Pests/Diseases": "Cabbage worm, aphids; crop rotation recommended",
        "Tips": "Thin seedlings; water at base to avoid fungal disease"
    },
    "Soybean": {
        "Soil": "Well-drained clay soil",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Phosphorus and potassium during flowering",
        "Temperature": "20–30°C",
        "Spacing": "30–50 cm between plants, 50–75 cm between rows",
        "Harvest": "90–120 days, pods dry and brown",
        "Pests/Diseases": "Aphids, stem rot; rotate crops",
        "Tips": "Ensure soil is loose; avoid planting in waterlogged areas"
    },
    "Wheat": {
        "Soil": "Loamy soil",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen at early growth stage",
        "Temperature": "10–25°C",
        "Spacing": "25–30 cm between rows",
        "Harvest": "110–130 days, grains golden",
        "Pests/Diseases": "Aphids, rust; rotate crops",
        "Tips": "Use well-prepared seedbed; irrigate during tillering"
    },
    "Tomato": {
        "Soil": "Loamy soil",
        "Watering": "Keep soil moist, avoid water on leaves",
        "Sunlight": "Full sun",
        "Fertilization": "High phosphorus at planting, potassium during fruiting",
        "Temperature": "18–27°C",
        "Spacing": "45–60 cm between plants, 90 cm between rows",
        "Harvest": "60–80 days, firm red fruits",
        "Pests/Diseases": "Aphids, blight; stake plants for support",
        "Tips": "Prune lower leaves; mulch to retain moisture"
    },
    "Sugarcane": {
        "Soil": "Loamy, rich in organic matter",
        "Watering": "Regular irrigation",
        "Sunlight": "Full sun",
        "Fertilization": "Split doses of NPK over growing period",
        "Temperature": "20–35°C",
        "Spacing": "100–120 cm between rows",
        "Harvest": "10–12 months, stalks mature",
        "Pests/Diseases": "Stem borer, smut; rotate crops",
        "Tips": "Remove weeds; keep soil moist"
    },
    "Cotton": {
        "Soil": "Well-drained loamy soil",
        "Watering": "Moderate",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen early, potassium during flowering",
        "Temperature": "25–30°C",
        "Spacing": "75 cm between rows",
        "Harvest": "150–180 days, bolls open",
        "Pests/Diseases": "Bollworm, aphids; monitor regularly",
        "Tips": "Prune for air circulation; avoid excess nitrogen"
    },
    "Potato": {
        "Soil": "Loose silt soil, well-drained",
        "Watering": "Moderate and frequent",
        "Sunlight": "Partial to full sun",
        "Fertilization": "Balanced NPK; compost recommended",
        "Temperature": "15–20°C",
        "Spacing": "25–30 cm between plants, 60 cm between rows",
        "Harvest": "70–120 days, tubers mature",
        "Pests/Diseases": "Aphids, blight; rotate crops",
        "Tips": "Hill soil around plants; keep soil moist"
    },
    "Onion": {
        "Soil": "Silt-loam",
        "Watering": "Moderate, keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen early, potassium before bulb formation",
        "Temperature": "12–25°C",
        "Spacing": "10–15 cm between bulbs, 30 cm between rows",
        "Harvest": "90–120 days, bulbs mature",
        "Pests/Diseases": "Thrips, downy mildew; rotate crops",
        "Tips": "Thin seedlings; avoid overwatering"
    },
    "Beans": {
        "Soil": "Silt soil",
        "Watering": "Moderate",
        "Sunlight": "Full sun",
        "Fertilization": "Phosphorus at sowing, potassium during flowering",
        "Temperature": "18–25°C",
        "Spacing": "10–15 cm between plants, 30–50 cm between rows",
        "Harvest": "50–70 days, pods firm and green",
        "Pests/Diseases": "Aphids, mosaic virus; stake climbing varieties",
        "Tips": "Harvest regularly to encourage production"
    },
    "Lettuce": {
        "Soil": "Silt soil, well-drained",
        "Watering": "Keep soil consistently moist",
        "Sunlight": "Partial sun",
        "Fertilization": "Light compost or balanced fertilizer",
        "Temperature": "15–20°C",
        "Spacing": "15–20 cm between plants, 30 cm between rows",
        "Harvest": "30–60 days, harvest young leaves for best taste",
        "Pests/Diseases": "Aphids, slugs; use mulch and nets",
        "Tips": "Grow in cooler weather; water in morning"
    }
}
