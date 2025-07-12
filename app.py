import streamlit as st
import pandas as pd
import numpy as np

# CSV डेटा लोड करें
df = pd.read_csv("house_price.csv")

# Streamlit UI
st.title("🏠 House Price Prediction (INR)")

area = st.slider("Area (sq ft)", 500, 5000, 1500)
bhk = st.selectbox("Number of BHK", [1, 2, 3, 4, 5])
bath = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
loc = st.selectbox("Location", df['Location'].unique())

# केवल नंबरिकल डेटा लें
X = df[['Area (sq ft)', 'BHK', 'Bathroom']].values
y = df['Price (INR)'].values

# Linear Regression manually using Normal Equation: θ = (XᵀX)^(-1) Xᵀy
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Bias term जोड़ें
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Input से prediction
input_data = np.array([[1, area, bhk, bath]])  # bias term + features
predicted_price = input_data.dot(theta_best)[0]

# Output
st.subheader("Predicted Price:")
st.success(f"₹ {int(predicted_price):,}")
