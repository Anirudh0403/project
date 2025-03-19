import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Title of the app
st.title("Crop Recommendation System: Wheat or Paddy")
st.info("This app recommends the best crop (Wheat or Paddy) based on your farm's conditions!")

# Dataset for training
data = {
    'soil_type': ['Loamy', 'Sandy', 'Clay', 'Loamy', 'Sandy', 'Clay', 'Black', 'Alluvial', 'Red'],
    'temperature': [20, 30, 25, 18, 32, 28, 25, 27, 22],
    'rainfall': [20, 15, 22, 18, 14, 16, 23, 21, 19],  # Rainfall in cm
    'humidity': [50, 65, 70, 45, 60, 55, 68, 52, 62],
    'nitrogen': [50, 40, 60, 55, 45, 65, 55, 60, 50],
    'phosphorus': [30, 35, 40, 20, 45, 25, 40, 35, 30],
    'sulphur': [20, 25, 30, 15, 35, 20, 28, 22, 25],
    'potassium': [40, 50, 55, 60, 45, 50, 60, 55, 52],
    'crop': ['Wheat', 'Paddy', 'Paddy', 'Wheat', 'Paddy', 'Wheat', 'Wheat', 'Paddy', 'Wheat']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Display raw data
with st.expander("View Raw Data"):
    st.write(df)

# Sidebar for user input
st.sidebar.header("Input Farm Conditions")

# Input fields
soil_type = st.sidebar.selectbox("Soil Type", ["Loamy", "Sandy", "Clay", "Black", "Alluvial", "Red"])
temperature = st.sidebar.slider("Temperature (°C)", 10, 45, 25)
rainfall = st.sidebar.slider("Rainfall (cm)", 5, 30, 15)
humidity = st.sidebar.slider("Humidity (%)", 30, 90, 60)
nitrogen = st.sidebar.slider("Nitrogen (N) level", 0, 100, 50)
phosphorus = st.sidebar.slider("Phosphorus (P) level", 0, 100, 30)
sulphur = st.sidebar.slider("Sulphur (S) level", 0, 100, 20)
potassium = st.sidebar.slider("Potassium (K) level", 0, 100, 40)

# Prepare input data
input_data = {
    'soil_type': soil_type,
    'temperature': temperature,
    'rainfall': rainfall,
    'humidity': humidity,
    'nitrogen': nitrogen,
    'phosphorus': phosphorus,
    'sulphur': sulphur,
    'potassium': potassium
}

# Convert input data to DataFrame
input_df = pd.DataFrame(input_data, index=[0])

# Display user input
with st.expander("View Input Data"):
    st.write(input_df)

# Data Preprocessing
# One-hot encode soil_type
X = pd.get_dummies(df.drop("crop", axis=1), columns=["soil_type"])
y = df["crop"]

# Encode input data
input_encoded = pd.get_dummies(input_df, columns=["soil_type"])

# Ensure input_encoded has the same columns as X
input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Make prediction
prediction = model.predict(input_encoded)

# Display prediction
st.subheader("Crop Recommendation")
st.success(f"Recommended Crop: **{prediction[0]}**")
