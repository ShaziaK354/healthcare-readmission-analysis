#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("C:/Users/shazi/Healthcare_Project/models/logistic_readmission_model.pkl")

# App Title
st.title("🏥 Hospital Readmission Predictor")
st.markdown("Predict whether a hospital is likely to have worse readmission performance.")

# Input Features
ownership = st.selectbox("Hospital Ownership", ["Government", "Proprietary", "Voluntary"])
emergency = st.radio("Emergency Services Available?", ["Yes", "No"])
mortality_worse = st.slider("Mortality Measures Rated Worse", 0, 10, 1)
safety_worse = st.slider("Safety Measures Rated Worse", 0, 10, 1)
readm_worse = st.slider("Readmission Measures Rated Worse", 0, 10, 1)

# Convert to numeric input (simplified)
ownership_map = {"Government": 0, "Proprietary": 1, "Voluntary": 2}
emergency_map = {"No": 0, "Yes": 1}

input_features = np.array([
    ownership_map[ownership],
    emergency_map[emergency],
    mortality_worse,
    safety_worse,
    readm_worse
]).reshape(1, -1)

# Predict button
if st.button("🔍 Predict Readmission Risk"):
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Readmission Risk! Probability: {probability:.2f}")
    else:
        st.success(f"✅ Low Readmission Risk! Probability: {probability:.2f}")


# In[ ]:




