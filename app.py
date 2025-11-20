import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import pickle

#load the trainded mode

model=tf.keras.models.load_model('model.h5')

# load the encoders and scalar.
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender=pickle.load(file)

with open('onehot_encoder_geo.pkl','rb') as file:
    onehot_encoder_geo=pickle.load(file)
    
with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

# Title for the app
st.title("Salary Prediction App")

# Input fields
gender = st.selectbox("Select Gender", ["Male", "Female"])
geography = st.selectbox("Select Geography", ["France", "Germany", "Spain"])
age = st.number_input("Enter Age", min_value=18, max_value=100, step=1)
balance = st.number_input("Enter Account Balance", min_value=0.0, step=100.0)
num_of_products = st.number_input("Enter Number of Products", min_value=1, max_value=4, step=1)
has_credit_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])

st.write(onehot_encoder_geo.categories[0])
st.write("testing")
