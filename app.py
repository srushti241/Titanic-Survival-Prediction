import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page settings
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢"
)

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger information to predict survival.")

# User inputs
pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

sibsp = st.number_input(
    "Number of Siblings/Spouses",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "Number of Parents/Children",
    min_value=0,
    max_value=10,
    value=0
)

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=32.0
)

# Prediction button
if st.button("Predict Survival"):

    passenger = pd.DataFrame({
        "Pclass": [pclass],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare]
    })

    prediction = model.predict(passenger)

    if prediction[0] == 1:
        st.success("🎉 Prediction: Passenger is likely to SURVIVE")
    else:
        st.error("❌ Prediction: Passenger is likely to NOT SURVIVE")
