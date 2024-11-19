import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('C:/Users/ncssa/carprice_prediction/final_regressor_optimized.pkl', 'rb') as model_file:
    final_regressor_optimized = pickle.load(model_file)

# Streamlit app header
st.title('Car Price Prediction')
st.write('Enter the details of the car to predict its price.')

# User input for each feature using Streamlit's selection boxes or sliders
km_options = list(range(0, 500001, 1000))  # 0 to 500000 km in steps of 1000 km
km = st.selectbox("Kilometers Driven", km_options, index=km_options.index(13000))

owner_no = st.sidebar.selectbox("Number of Owners", (1, 2, 3, 4))
years = list(range(1990, 2025))
model_year = st.sidebar.selectbox("Model Year", years, index=years.index(2020))

# Define possible values for Engine Displacement, Top Speed, and Mileage
displacement_options = list(range(500, 5001, 100))  # 500 to 5000 cc in steps of 100
top_speed_options = list(range(100, 301, 10))      # 100 to 300 km/h in steps of 10
mileage_options = list(range(5, 31))               # 5 to 30 km/l

# Dropdown selections
displacement = st.selectbox("Engine Displacement (cc)", displacement_options, index=displacement_options.index(1400))
top_speed = st.selectbox("Top Speed (km/h)", top_speed_options, index=top_speed_options.index(180))
mileage = st.selectbox("Mileage (km/l)", mileage_options, index=mileage_options.index(17))
seating_capacity = st.sidebar.selectbox("Seating Capacity", (2, 3, 4, 5, 6, 7, 8, 9))

# Transmission input
transmission = st.sidebar.selectbox("Transmission", ("Manual", "Automatic"))
transmission_encoded = 1 if transmission == "Manual" else 0  # Binary encoding

# Fuel Type and City input
fuel_type = st.sidebar.selectbox("Fuel Type", ("Petrol", "Diesel", "Electric", "CNG", "LPG"))
city = st.sidebar.selectbox("City", ("Bangalore", "Chennai", "Delhi", "Jaipur", "Hyderabad", "Kolkata"))

# Fit the encoders with complete categories
fuel_type_categories = ["Petrol", "Diesel", "Electric", "CNG", "LPG"]
city_categories = ["Bangalore", "Chennai", "Delhi", "Jaipur", "Hyderabad", "Kolkata"]

fuel_type_encoder = LabelEncoder()
city_encoder = LabelEncoder()

fuel_type_encoder.fit(fuel_type_categories)
city_encoder.fit(city_categories)

# Encode inputs
fuel_type_encoded = fuel_type_encoder.transform([fuel_type])[0]
city_encoded = city_encoder.transform([city])[0]

# Create a DataFrame with user inputs
input_data = pd.DataFrame({
    'km': [km],
    'transmission': [transmission_encoded],  # Matches the feature name in training data
    'Fuel Type': [fuel_type_encoded],        # Matches the feature name in training data
    'city': [city_encoded],                  # Matches the feature name in training data
    'ownerNo': [owner_no],
    'modelYear': [model_year],
    'Displacement': [displacement],
    'Top Speed': [top_speed],
    'Mileage': [mileage],
    'Seating Capacity': [seating_capacity]
})

# Reorder the columns to match the training feature order
trained_feature_order = [
    'km', 'transmission', 'Fuel Type', 'city', 
    'ownerNo', 'modelYear', 'Displacement', 
    'Top Speed', 'Mileage', 'Seating Capacity'
]

# Ensure the column order matches the training data
input_data = input_data[trained_feature_order]

# Button to make prediction
if st.button('Predict Price'):
    try:
        # Use the trained model to make a prediction
        predicted_price = final_regressor_optimized.predict(input_data)
        st.write(f"The predicted price of the car is: ₹{predicted_price[0]:,.2f}")
    except Exception as e:
        st.write(f"An error occurred during prediction: {e}")
