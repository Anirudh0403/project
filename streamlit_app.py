import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Custom CSS to add background image
def add_background(image_file):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url({image_file});
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Add background image of wheat and paddy fields
add_background('https://i.postimg.cc/kgHLg4YL/premium-photo-1698086768776-2fe137e167df.avif')  # Replace with your actual image URL or local file

# Title of the app
st.title('Crop Recommendation: Wheat or Paddy')
st.info('This app uses a machine learning model to recommend the best crop (Wheat or Paddy) based on your input!')

# Create a dataset for demonstration purposes (replace with real data in practice)
# Example dataset with soil nutrients and conditions
data = {
    'soil_type': ['Loamy', 'Sandy', 'Clay', 'Loamy', 'Sandy', 'Clay', 'Black', 'Red', 'Alluvial'],
    'temperature': [20, 30, 25, 18, 32, 28, 22, 28, 20],
    'rainfall': [200, 150, 220, 180, 140, 160, 250, 180, 190],
    'humidity': [50, 65, 70, 45, 60, 55, 60, 70, 65],
    'nitrogen': [50, 40, 60, 55, 45, 65, 70, 50, 60],
    'phosphorus': [30, 35, 40, 20, 45, 25, 30, 40, 35],
    'sulphur': [20, 25, 30, 15, 35, 20, 25, 30, 20],
    'potassium': [40, 50, 55, 60, 45, 50, 45, 50, 55],
    'crop': ['Wheat', 'Paddy', 'Paddy', 'Wheat', 'Paddy', 'Wheat', 'Wheat', 'Paddy', 'Paddy']
}

df = pd.DataFrame(data)

with st.expander('Data'):
    st.write('Raw data used for training')
    st.dataframe(df)

# Input features for the sidebar
with st.sidebar:
    st.header('Input Conditions for Your Farm')
    
    soil_type = st.selectbox('Soil Type', ('Loamy', 'Sandy', 'Clay', 'Black', 'Red', 'Alluvial'))
    temperature = st.slider('Temperature (°C)', 10, 45, 25)
    rainfall = st.slider('Rainfall (mm)', 50, 300, 150)
    humidity = st.slider('Humidity (%)', 30, 90, 60)
    
    nitrogen = st.slider('Nitrogen (N) level', 0, 100, 50)
    phosphorus = st.slider('Phosphorus (P) level', 0, 100, 30)
    sulphur = st.slider('Sulphur (S) level', 0, 100, 20)
    potassium = st.slider('Potassium (K) level', 0, 100, 40)

    # Create DataFrame for the input features
    input_data = {
        'soil_type': soil_type,
        'temperature': temperature,
        'rainfall': rainfall,
        'humidity': humidity,
        'nitrogen': nitrogen,
        'phosphorus': phosphorus,
        'sulphur': sulphur,
        'pot
