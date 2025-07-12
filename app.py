import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# डेटा लोड करें
df = pd.read_csv("house_price.csv")

# Streamlit UI
st.title("🏠 House Price Prediction (INR)")

area = st.slider("Area (sq ft)", 500, 5000, 1500)
bhk = st.selectbox("Number of BHK", [1, 2, 3, 4, 5])
bath = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
loc = st.selectbox("Location", df['Location'].unique())

# मॉडल ट्रेन करें
X = df[['Area (sq ft)', 'BHK', 'Bathroom']]
y = df['Price (INR)']
model = LinearRegression()
model.fit(X, y)

# Prediction
input_data = pd.DataFrame([[area, bhk, bath]], columns=['Area (sq ft)', 'BHK', 'Bathroom'])
predicted_price = model.predict(input_data)[0]

st.subheader("Predicted Price:")
st.success(f"₹ {int(predicted_price):,}")
