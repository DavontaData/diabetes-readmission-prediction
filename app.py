import streamlit as st
import pandas as pd
import joblib

if st.button("Predict Readmission Risk"):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]
  st.success(...)
st.error(...)
st.info(...)
