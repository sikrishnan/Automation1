import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter Your Height",50,500,250)
weight = st.slider("Enter Your Weight", 50,250,100)

bmi = weight / ((height/100)**2)
st.write(f"your BMI value is {bmi:.2f} ")

st.write("BMI Catergories")
st.write("Underwait: BMI less than 18.5")
st.write("Normal: BMI between 18.5 and 24.5")
st.write("Overweight: BMI greater than 25 and 29.5")
st.write("Obisity: BMI greater than 30")