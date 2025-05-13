import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Air Pollution Detection by Vehicles")
 
# Sidebar for user input
st.sidebar.header("Input Pollution Data")
st.sidebar.write("Enter the percentage of each pollutant emitted by the vehicle:")

# Input fields for pollutants
co = st.sidebar.number_input("Carbon Monoxide (CO) (%)", min_value=0.0, max_value=100.0, value=0.0)
no2 = st.sidebar.number_input("Nitrogen Dioxide (NO2) (%)", min_value=0.0, max_value=100.0, value=0.0)
pm25 = st.sidebar.number_input("Particulate Matter 2.5 (PM2.5) (%)", min_value=0.0, max_value=100.0, value=0.0)
so2 = st.sidebar.number_input("Sulfur Dioxide (SO2) (%)", min_value=0.0, max_value=100.0, value=0.0)

# Validate total percentage
total = co + no2 + pm25 + so2
if total != 100:
    st.sidebar.error("The total percentage must equal 100%. Please adjust the values.")

# Main content
st.header("Pollution Analysis")

# Display the input data
st.write("### Input Data")
pollution_data = {
    "Pollutant": ["Carbon Monoxide (CO)", "Nitrogen Dioxide (NO2)", "Particulate Matter 2.5 (PM2.5)", "Sulfur Dioxide (SO2)"],
    "Percentage": [co, no2, pm25, so2]
}
df = pd.DataFrame(pollution_data)
st.table(df)

# Display a pie chart
st.write("### Pollutant Distribution")
fig, ax = plt.subplots()
ax.pie(df["Percentage"], labels=df["Pollutant"], autopct="%1.1f%%", startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)

# Display effects of pollutants
st.write("### Effects of Pollutants")
effects = {
    "Carbon Monoxide (CO)": "Reduces oxygen delivery to the body's organs and tissues.",
    "Nitrogen Dioxide (NO2)": "Causes respiratory problems and contributes to the formation of smog.",
    "Particulate Matter 2.5 (PM2.5)": "Can penetrate deep into the lungs and cause cardiovascular and respiratory diseases.",
    "Sulfur Dioxide (SO2)": "Causes respiratory issues and contributes to acid rain."
}

for pollutant, effect in effects.items():
    st.write(f"**{pollutant}:** {effect}")

# Footer
st.write("---")
st.write("Developed by [Your Name]")
