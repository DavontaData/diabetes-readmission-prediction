import streamlit as st
import pandas as pd
import joblib

model = joblib.load("diabetes_readmission_model.pkl")
model_features = joblib.load("model_features.pkl")

st.title("Diabetes 30-Day Readmission Risk Prediction")

age = st.number_input("Age", min_value=0, max_value=100, value=50)
number_inpatient_visits = st.number_input("Number of Prior Inpatient Visits", min_value=0, value=0)
number_emergency = st.number_input("Number of Emergency Visits", min_value=0, value=0)
time_in_hospital = st.number_input("Time in Hospital (Days)", min_value=1, value=3)

a1c_result = st.selectbox(
    "A1C Result",
    ["None", "Norm", ">8"]
)

max_glu_serum = st.selectbox(
    "Maximum Glucose Serum",
    ["None", "Norm", ">300"]
)

insulin = st.selectbox(
    "Insulin Treatment",
    ["No", "Steady", "Up"]
)

change_medication = st.selectbox(
    "Medication Change",
    ["No", "Yes"]
)

if st.button("Predict Readmission Risk"):

    input_data = pd.DataFrame({
        "age": [age],
        "number_inpatient_visits": [number_inpatient_visits],
        "number_emergency": [number_emergency],
        "time_in_hospital": [time_in_hospital],
        "a1c_result": [a1c_result],
        "max_glu_serum": [max_glu_serum],
        "insulin": [insulin],
        "change_medication": [change_medication]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error("Higher Risk of 30-Day Readmission")
    else:
        st.success("Lower Risk of 30-Day Readmission")

    st.write(f"Estimated Readmission Probability: {probability:.2%}")
