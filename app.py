import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load('house_price_model.pkl')

st.title("🏠 House Price Prediction")

# Inputs
bedrooms = st.number_input("Bedrooms", min_value=0)

bathrooms = st.number_input("Bathrooms", min_value=0.0)

sqft_living = st.number_input("Sqft Living", min_value=0)

sqft_lot = st.number_input("Sqft Lot", min_value=0)

floors = st.number_input("Floors", min_value=1)

waterfront = st.selectbox("Waterfront", [0, 1])

view = st.number_input("View", min_value=0)

condition = st.number_input("Condition", min_value=1)

sqft_above = st.number_input("Sqft Above", min_value=0)

sqft_basement = st.number_input("Sqft Basement", min_value=0)

yr_built = st.number_input("Year Built", min_value=1900)

yr_renovated = st.number_input("Year Renovated", min_value=0)

city = st.number_input("City Encoded Value")

statezip = st.number_input("StateZip Encoded Value")

year = st.number_input("Year", min_value=2000)

month = st.number_input("Month", min_value=1, max_value=12)

day = st.number_input("Day", min_value=1, max_value=31)

# Prediction
if st.button("Predict Price"):

    features = np.array([[

        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        city,
        statezip,
        year,
        month,
        day

    ]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")