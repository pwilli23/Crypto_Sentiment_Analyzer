import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.read_csv("prediction.csv", index_col = "timestamp", parse_dates=True, infer_datetime_format = True)

df.sort_index(inplace=True, ascending = False)

def color_negative(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'


st.write("# Hello Welcome to the Crypto Forecaster Application! ")

st.header("Our Projects Purpose:")

st.markdown("The Crypto Forecaster Application was created to help investors make better buying and selling decisions in a volitile Cryptocurrency market.  By running a Logistic Regression Model Machine Learning Algorithm, the application is better able to predict movement in the market.  ")

st.header("Please Provide Your Age: This Application can only be used ages 21+")

age = st.slider('How old are you?', 0,110,25)
st.write("I'm", age, 'years old')

st.header("How to Use Application/Key:")

st.markdown("Below you will find a DataFrame that contains Predictions and Actual Results of Daily movement in the Cryptocurrency market.  In this DataFrame, you can examine previous predictions on daily market movement and compare the results to what the daily returns actually were for that day.")

st.markdown("Please select a date that you would like to know the forecast for")

st.header("DataFrame Prediction Key:")
st.markdown("Green Highlight = We believe the market daily returns will be positive")  
st.markdown("Red Highlight = We believe the market daily returns will be negative")

start = st.selectbox("Choose a start date", df.index)
end = st.selectbox("Choose an end date", df.index)
st.dataframe(df[:][end:start].style.applymap(color_negative, subset=['Prediction','Actual']))






