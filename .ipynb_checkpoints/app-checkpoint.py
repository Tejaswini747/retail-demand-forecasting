import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("demand_forecasting_model.pkl")

st.title("🛒 Retail Demand Forecasting App")

st.write("Enter details to predict product demand")

# User inputs
store_id = st.selectbox("Select Store ID", [101, 102, 103])
item_id = st.selectbox("Select Item ID", [1001, 1002, 1003, 1004])

price = st.slider("Price", 50, 200, 100)
on_promo = st.selectbox("On Promotion?", [0, 1])

day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)
year = st.slider("Year", 2022, 2023, 2023)
day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 3)

lag_1 = st.number_input("Yesterday Sales", min_value=0, value=30)
lag_7 = st.number_input("Last Week Sales", min_value=0, value=35)

rolling_mean_7 = st.number_input("7-day Avg Sales", min_value=0, value=32)
rolling_mean_14 = st.number_input("14-day Avg Sales", min_value=0, value=33)

# Prediction button
if st.button("Predict Demand"):

    input_data = pd.DataFrame([[
        store_id, item_id, price, on_promo,
        day, month, year, day_of_week,
        lag_1, lag_7, rolling_mean_7, rolling_mean_14
    ]], columns=[
        "store_id", "item_id", "price", "on_promo",
        "day", "month", "year", "day_of_week",
        "lag_1", "lag_7", "rolling_mean_7", "rolling_mean_14"
    ])

    prediction = model.predict(input_data)[0]

    st.success(f"📦 Predicted Demand: {int(prediction)} units")