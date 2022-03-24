import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.read_csv("prediction.csv")



st.write("# Hello Welcome to the Crypto Forecaster Application! ")

st.header("Our Projects Purpose:")

st.markdown("The Crypto Forecaster Application was created to help investors make better buying and selling decisions in a volitile Cryptocurrency market.  By running a Logistic Regression Model Machine Learning Algorithm, the application is better able to predict movement in the market.  ")

st.header("Please Provide Your Age: This Application can only be used ages 21+")

age = st.slider('How old are you?', 0,110,25)
st.write("I'm", age, 'years old')

st.header("How to Use Application/Key:")

st.markdown("Below you will find a DataFrame that contains Predictions and Actual Results of Daily movement in the Cryptocurrency market...")

st.markdown("Please select a date that you would like to know the forecast for")

st.markdown("DataFrame Prediction Key:")
st.markdown("1 = We believe the market daily returns will be positive")  
st.markdown("0 = We believe the market daily returns will be negative")

st.write(df)






