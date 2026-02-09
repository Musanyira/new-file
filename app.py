import streamlit as st
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the saved model
model = joblib.load('linear_regression_model.pkl')

# Function to make predictions
def make_prediction(study_hours, attendance, participation, grade):
    input_data = np.array([[study_hours, attendance, participation, grade]])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit App UI
st.title("Student Performance Prediction")

# User Input Fields
study_hours = st.number_input("Weekly Self-Study Hours", min_value=0.0, max_value=40.0, step=0.1)
attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0, step=0.1)
participation = st.number_input("Class Participation Score", min_value=0.0, max_value=10.0, step=0.1)
grade = st.selectbox("Grade (A=1, B=2, C=3, D=4, F=5)", options=[1, 2, 3, 4, 5])

# Prediction Button
if st.button("Predict Total Score"):
    predicted_score = make_prediction(study_hours, attendance, participation, grade)
    st.write(f"The predicted total score is: {predicted_score:.2f}")
