import streamlit as st
import pandas as pd
import numpy as np

st.title("🏠 House Price Prediction (₹ India)")
st.markdown("### Enter Area (Sq Ft) to predict estimated house price")

# CSV file read
df = pd.read_csv("house_price.csv")

# Display sample data
st.subheader("📊 Sample Data from house_price.csv")
st.dataframe(df)

# Linear regression calculation (manual)
X = df['Area'].values
y = df['Price'].values

# Mean
mean_x = np.mean(X)
mean_y = np.mean(y)

# Slope (m) and Intercept (c)
n = len(X)
numer = np.sum((X - mean_x) * (y - mean_y))
denom = np.sum((X - mean_x)**2)

m = numer / denom
c = mean_y - m * mean_x

# User input
area_input = st.number_input("📐 Enter Area (in Sq Ft)", min_value=100, max_value=10000, value=1000)

# Prediction
predicted_price = m * area_input + c

st.success(f"🧮 Predicted Price: ₹ {round(predicted_price):,}")
