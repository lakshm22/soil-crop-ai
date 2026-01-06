# Soil type crops mapping
soil_crop_map = {
    "Sandy": ["Carrot", "Groundnut", "Watermelon", "Cucumber", "Radish", "Peanut", "Okra", "Sweet Potato", "Millet", "Pumpkin", "Tomato", "Chili", "Lemon"],
    "Clayey": ["Rice", "Broccoli", "Cabbage", "Soybean", "Cauliflower", "Mustard", "Spinach", "Lettuce", "Onion", "Garlic", "Fenugreek", "Brinjal", "Lemon"],
    "Loamy": ["Wheat", "Tomato", "Sugarcane", "Cotton", "Maize", "Chili", "Pumpkin", "Potato", "Cabbage", "Carrot", "Capsicum", "Radish", "Lemon"],
    "Silt": ["Potato", "Onion", "Beans", "Lettuce", "Beetroot", "Peas", "Corn Salad", "Spinach", "Broccoli", "Cauliflower", "Chard", "Turnip", "Lemon"]
}

# Detailed crop guidance
crop_guidance = {

    "Carrot": {
        "Soil": "Loose, well-drained",
        "Watering": "Moderate, frequent to keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Light compost or balanced NPK; avoid excess nitrogen",
        "Temperature": "16–21°C",
        "Spacing": "2–3 cm between seeds, 25–30 cm between rows",
        "Harvest": "70–80 days, when roots reach maturity",
        "Pests/Diseases": "Aphids, carrot fly; practice crop rotation",
        "Tips": "Thin seedlings to prevent crowding; mulch to retain moisture"
    },

    "Groundnut": {
        "Soil": "Sandy loam, well-drained",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Phosphorus rich during planting, nitrogen during growth",
        "Temperature": "20–30°C",
        "Spacing": "30 cm between rows",
        "Harvest": "90–120 days, pods mature",
        "Pests/Diseases": "Aphids, leaf miner",
        "Tips": "Ensure deep plowing; rotate crops to prevent disease"
    },

    "Watermelon": {
        "Soil": "Sandy, fertile",
        "Watering": "Moderate; frequent during flowering and fruiting",
        "Sunlight": "Full sun",
        "Fertilization": "High potassium during fruiting stage",
        "Temperature": "21–29°C",
        "Spacing": "120–150 cm between plants",
        "Harvest": "80–100 days, rind hard and fruit full-sized",
        "Pests/Diseases": "Powdery mildew, aphids",
        "Tips": "Provide space for vines; mulch to retain moisture"
    },

    "Cucumber": {
        "Soil": "Sandy loam, fertile",
        "Watering": "Keep soil consistently moist",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK + compost",
        "Temperature": "18–30°C",
        "Spacing": "50–60 cm between plants",
        "Harvest": "50–70 days, fruits firm and green",
        "Pests/Diseases": "Cucumber beetle, powdery mildew",
        "Tips": "Use trellis for support; mulch soil"
    },

    "Radish": {
        "Soil": "Loose, sandy or loamy",
        "Watering": "Keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "10–25°C",
        "Spacing": "3–5 cm between seeds",
        "Harvest": "25–60 days, roots mature",
        "Pests/Diseases": "Flea beetle, root rot",
        "Tips": "Thin seedlings; mulch to retain moisture"
    },

    "Peanut": {
        "Soil": "Sandy loam, well-drained",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Phosphorus rich during planting, nitrogen during growth",
        "Temperature": "20–30°C",
        "Spacing": "30–50 cm between rows",
        "Harvest": "120–150 days, pods mature",
        "Pests/Diseases": "Leaf miner, aphids",
        "Tips": "Rotate crops; deep plowing improves yield"
    },

    "Okra": {
        "Soil": "Sandy loam, fertile",
        "Watering": "Moderate; keep soil slightly moist",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK",
        "Temperature": "20–35°C",
        "Spacing": "30–50 cm between plants",
        "Harvest": "50–70 days, pods tender",
        "Pests/Diseases": "Aphids, fruit borers",
        "Tips": "Prune lower leaves; mulch soil"
    },

    "Sweet Potato": {
        "Soil": "Sandy, well-drained",
        "Watering": "Moderate, consistent",
        "Sunlight": "Full sun",
        "Fertilization": "Compost rich in potassium",
        "Temperature": "21–29°C",
        "Spacing": "30–40 cm between plants",
        "Harvest": "90–120 days, roots mature",
        "Pests/Diseases": "Wireworms, root rot",
        "Tips": "Provide loose soil; mulch to retain moisture"
    },

    "Millet": {
        "Soil": "Sandy loam",
        "Watering": "Low; drought tolerant",
        "Sunlight": "Full sun",
        "Fertilization": "Low nitrogen; compost optional",
        "Temperature": "20–30°C",
        "Spacing": "20–25 cm between plants",
        "Harvest": "60–90 days",
        "Pests/Diseases": "Stem borers",
        "Tips": "Sow seeds shallow; minimal watering needed"
    },

    "Pumpkin": {
        "Soil": "Loamy, fertile",
        "Watering": "Moderate; keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "High phosphorus and potassium",
        "Temperature": "20–30°C",
        "Spacing": "100–150 cm between plants",
        "Harvest": "90–120 days, fruit skin hard",
        "Pests/Diseases": "Squash bugs, powdery mildew",
        "Tips": "Provide space for vines; mulch soil"
    },

    "Tomato": {
        "Soil": "Loamy, rich in organic matter",
        "Watering": "Moderate; keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK + compost",
        "Temperature": "20–30°C",
        "Spacing": "40–50 cm between plants",
        "Harvest": "60–80 days, fruits red and firm",
        "Pests/Diseases": "Blight, aphids",
        "Tips": "Stake plants; prune lower leaves; mulch soil"
    },

    "Chili": {
        "Soil": "Loamy, fertile",
        "Watering": "Moderate; avoid wetting leaves",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK + compost",
        "Temperature": "20–30°C",
        "Spacing": "30–50 cm between plants",
        "Harvest": "70–90 days, fruits red",
        "Pests/Diseases": "Aphids, blight",
        "Tips": "Stake plants; prune lower leaves"
    },

    "Lemon": {
        "Soil": "Well-drained loamy or silt, slightly acidic (pH 5.5–7)",
        "Watering": "Deep watering 1–2 times/week",
        "Sunlight": "Full sun (6–8 hours)",
        "Fertilization": "Balanced NPK + compost",
        "Temperature": "20–30°C optimal",
        "Spacing": "3–4 meters between trees",
        "Harvest": "6–9 months after flowering",
        "Pests/Diseases": "Aphids, citrus leaf miner, root rot",
        "Tips": "Mulch soil; prune regularly; ensure good drainage"
    },

    "Rice": {
        "Soil": "Clay, water-retentive",
        "Watering": "Flooded fields or constant moisture",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen, phosphorus, potassium",
        "Temperature": "20–35°C",
        "Spacing": "15–20 cm between plants",
        "Harvest": "120–150 days, grains golden",
        "Pests/Diseases": "Stem borers, leaf blight",
        "Tips": "Maintain water depth; rotate crops"
    },

    "Broccoli": {
        "Soil": "Fertile clay or silt",
        "Watering": "Keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen-rich during growth",
        "Temperature": "15–20°C",
        "Spacing": "45 cm between plants",
        "Harvest": "70–100 days, heads firm",
        "Pests/Diseases": "Cabbage worm, aphids",
        "Tips": "Mulch soil; remove yellow leaves"
    },

    "Cabbage": {
        "Soil": "Clay or loamy, fertile",
        "Watering": "Keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen-rich fertilizer",
        "Temperature": "15–20°C",
        "Spacing": "45–60 cm between plants",
        "Harvest": "80–120 days, heads firm",
        "Pests/Diseases": "Cabbage worm, aphids",
        "Tips": "Mulch soil; rotate crops"
    },

    "Soybean": {
        "Soil": "Clay, fertile, well-drained",
        "Watering": "Moderate; avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen not needed (legume)",
        "Temperature": "20–30°C",
        "Spacing": "30–50 cm between plants",
        "Harvest": "90–120 days, pods mature",
        "Pests/Diseases": "Aphids, leaf spot",
        "Tips": "Rotate crops; ensure drainage"
    },

    "Cauliflower": {
        "Soil": "Clay, fertile",
        "Watering": "Keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen-rich fertilizer",
        "Temperature": "15–20°C",
        "Spacing": "45–60 cm between plants",
        "Harvest": "80–100 days, heads compact",
        "Pests/Diseases": "Cabbage worms, aphids",
        "Tips": "Mulch soil; protect from pests"
    },

    "Mustard": {
        "Soil": "Clay or loamy, fertile",
        "Watering": "Moderate",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK",
        "Temperature": "10–25°C",
        "Spacing": "20–30 cm between rows",
        "Harvest": "90–100 days, pods yellow",
        "Pests/Diseases": "Aphids, flea beetle",
        "Tips": "Rotate crops; thin seedlings"
    },

    "Spinach": {
        "Soil": "Clay, loam or silt",
        "Watering": "Keep soil moist",
        "Sunlight": "Full sun to partial shade",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "10–25°C",
        "Spacing": "20–30 cm between plants",
        "Harvest": "30–50 days, leaves tender",
        "Pests/Diseases": "Aphids, leaf miners",
        "Tips": "Harvest regularly to encourage growth"
    },

    "Lettuce": {
        "Soil": "Clay or silt, fertile",
        "Watering": "Keep soil moist",
        "Sunlight": "Partial shade",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "10–20°C",
        "Spacing": "25–30 cm between plants",
        "Harvest": "50–70 days",
        "Pests/Diseases": "Aphids, slugs",
        "Tips": "Mulch soil; protect from heat"
    },

    "Onion": {
        "Soil": "Silt or clay, fertile",
        "Watering": "Moderate, consistent",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen early; potassium during bulb formation",
        "Temperature": "15–25°C",
        "Spacing": "10–15 cm between bulbs",
        "Harvest": "90–120 days, tops yellow",
        "Pests/Diseases": "Onion fly, thrips",
        "Tips": "Mulch soil; avoid waterlogging"
    },

    "Garlic": {
        "Soil": "Clay, fertile, well-drained",
        "Watering": "Moderate",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK + compost",
        "Temperature": "10–25°C",
        "Spacing": "10–15 cm between cloves",
        "Harvest": "90–120 days, leaves yellow",
        "Pests/Diseases": "Nematodes, aphids",
        "Tips": "Plant cloves upright; mulch soil"
    },

    "Fenugreek": {
        "Soil": "Clay or sandy loam",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Compost rich",
        "Temperature": "10–30°C",
        "Spacing": "10–15 cm between plants",
        "Harvest": "90–100 days, leaves and seeds mature",
        "Pests/Diseases": "Aphids, root rot",
        "Tips": "Rotate crops; thin seedlings"
    },

    "Brinjal": {
        "Soil": "Clay or loamy, fertile",
        "Watering": "Moderate; keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK",
        "Temperature": "20–30°C",
        "Spacing": "60–90 cm between plants",
        "Harvest": "70–90 days, fruits firm",
        "Pests/Diseases": "Aphids, fruit borers",
        "Tips": "Stake plants; remove diseased leaves"
    },

    "Wheat": {
        "Soil": "Loamy, well-drained",
        "Watering": "Moderate; ensure soil moisture during germination",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen-rich during vegetative stage",
        "Temperature": "15–25°C",
        "Spacing": "20–25 cm between rows",
        "Harvest": "120–150 days, grains golden and hard",
        "Pests/Diseases": "Aphids, rust; rotate crops",
        "Tips": "Plow soil deeply; ensure good drainage"
    },

    "Sugarcane": {
        "Soil": "Loamy, fertile, well-drained",
        "Watering": "Moderate; frequent during dry periods",
        "Sunlight": "Full sun",
        "Fertilization": "High nitrogen and potassium",
        "Temperature": "20–35°C",
        "Spacing": "90 cm between rows",
        "Harvest": "12–16 months, stems mature",
        "Pests/Diseases": "Stem borer, rust",
        "Tips": "Ensure deep plowing; maintain soil fertility"
    },

    "Cotton": {
        "Soil": "Loamy, fertile",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen-rich early, potassium during flowering",
        "Temperature": "20–35°C",
        "Spacing": "60–90 cm between plants",
        "Harvest": "150–180 days, bolls open",
        "Pests/Diseases": "Bollworm, aphids",
        "Tips": "Remove weeds; maintain plant spacing"
    },

    "Maize": {
        "Soil": "Loamy, well-drained",
        "Watering": "Moderate, keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Nitrogen and phosphorus at planting; potassium during flowering",
        "Temperature": "18–30°C",
        "Spacing": "20–30 cm between plants, 60–75 cm between rows",
        "Harvest": "90–120 days, grains hard",
        "Pests/Diseases": "Stem borers, leaf blight",
        "Tips": "Plant in rows; irrigate during dry periods"
    },

    "Capsicum": {
        "Soil": "Loamy, rich in organic matter",
        "Watering": "Moderate, avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK",
        "Temperature": "20–30°C",
        "Spacing": "30–50 cm between plants",
        "Harvest": "70–90 days, fruits firm",
        "Pests/Diseases": "Aphids, blight",
        "Tips": "Stake plants; mulch soil"
    },

    "Potato": {
        "Soil": "Loamy, well-drained",
        "Watering": "Moderate, consistent",
        "Sunlight": "Full sun",
        "Fertilization": "Compost + balanced NPK",
        "Temperature": "15–25°C",
        "Spacing": "30–40 cm between plants",
        "Harvest": "90–120 days, tubers mature",
        "Pests/Diseases": "Potato beetle, blight",
        "Tips": "Hill soil around stems; mulch soil"
    },

    "Beans": {
        "Soil": "Silt or loamy, fertile",
        "Watering": "Moderate; avoid waterlogging",
        "Sunlight": "Full sun",
        "Fertilization": "Compost rich; minimal nitrogen",
        "Temperature": "18–30°C",
        "Spacing": "30–50 cm between plants",
        "Harvest": "50–70 days, pods mature",
        "Pests/Diseases": "Aphids, root rot",
        "Tips": "Provide trellis for support; rotate crops"
    },

    "Beetroot": {
        "Soil": "Silt or loam, loose",
        "Watering": "Moderate; keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Balanced NPK",
        "Temperature": "15–25°C",
        "Spacing": "10–15 cm between plants",
        "Harvest": "60–80 days, roots firm",
        "Pests/Diseases": "Aphids, leaf miners",
        "Tips": "Thin seedlings; mulch soil"
    },

    "Peas": {
        "Soil": "Silt or loam, fertile",
        "Watering": "Moderate; avoid waterlogging",
        "Sunlight": "Full sun to partial shade",
        "Fertilization": "Compost rich; minimal nitrogen",
        "Temperature": "10–25°C",
        "Spacing": "5–10 cm between plants",
        "Harvest": "60–90 days, pods mature",
        "Pests/Diseases": "Aphids, powdery mildew",
        "Tips": "Provide support for climbing varieties; rotate crops"
    },

    "Corn Salad": {
        "Soil": "Silt, loose",
        "Watering": "Keep soil moist",
        "Sunlight": "Partial shade",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "10–20°C",
        "Spacing": "10–15 cm between plants",
        "Harvest": "40–60 days, leaves tender",
        "Pests/Diseases": "Aphids, slugs",
        "Tips": "Thin seedlings; mulch soil"
    },

    "Chard": {
        "Soil": "Silt, fertile",
        "Watering": "Keep soil moist",
        "Sunlight": "Full sun to partial shade",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "10–25°C",
        "Spacing": "20–30 cm between plants",
        "Harvest": "50–70 days, leaves tender",
        "Pests/Diseases": "Leaf miners, aphids",
        "Tips": "Harvest outer leaves first; mulch soil"
    },

    "Turnip": {
        "Soil": "Silt or loam, loose",
        "Watering": "Moderate; keep soil moist",
        "Sunlight": "Full sun",
        "Fertilization": "Compost or balanced NPK",
        "Temperature": "10–20°C",
        "Spacing": "10–15 cm between plants",
        "Harvest": "50–70 days, roots firm",
        "Pests/Diseases": "Root maggots, aphids",
        "Tips": "Thin seedlings; mulch soil"
    }
}
