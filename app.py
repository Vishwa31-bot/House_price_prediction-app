import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title
st.write("यह एप्लीकेशन area के हिसाब से घर की कीमत का अनुमान लगाएगी।")

# Load data
df = pd.read_csv("house_price.csv")

# Show data
st.subheader("📊 Sample Data")
st.dataframe(df)

# Linear Regression (Without sklearn)
# y = m*x + c

X = df['Area'].values
y = df['Price'].values

# Mean
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculate slope (m) and intercept (c)
n = len(X)
numer = np.sum((X - mean_x) * (y - mean_y))
denom = np.sum((X - mean_x)**2)

m = numer / denom
c = mean_y - m * mean_x

# User input
area_input = st.number_input("📐 Enter Area in Sq Ft", min_value=100, max_value=10000, value=1000)

# Predict
predicted_price = m * area_input + c
st.success(f"🧮 Estimated Price: ₹ {round(predicted_price):,}")
