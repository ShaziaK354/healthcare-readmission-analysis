import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("C:/Users/shazi/Healthcare_Project/models/logistic_readmission_model.pkl")

# Custom title banner
st.markdown("""
# 🩺 Healthcare Readmission Predictor  
""")

# Description
st.info("Use this app to predict whether a hospital is at risk of **worse readmission performance** based on key metrics.")

# Input Features
ownership = st.selectbox("🏢 Hospital Ownership", ["Government", "Proprietary", "Voluntary"])
emergency = st.radio("🚑 Emergency Services Available?", ["Yes", "No"])
mortality_worse = st.slider("☠️ Mortality Measures Rated Worse", 0, 10, 1)
safety_worse = st.slider("⚠️ Safety Measures Rated Worse", 0, 10, 1)
readm_worse = st.slider("🔁 Readmission Measures Rated Worse", 0, 10, 1)

# Convert to numeric input
ownership_map = {"Government": 0, "Proprietary": 1, "Voluntary": 2}
emergency_map = {"No": 0, "Yes": 1}

input_features = np.array([
    ownership_map[ownership],
    emergency_map[emergency],
    mortality_worse,
    safety_worse,
    readm_worse
]).reshape(1, -1)

# Prediction
if st.button("🔍 Predict Readmission Risk"):
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Readmission Risk! | Probability: **{probability:.2f}**")
    else:
        st.success(f"✅ Low Readmission Risk! | Probability: **{probability:.2f}**")
        
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/shazi/Healthcare_Project/output/hospital_readmission_summary_v3.csv")

st.markdown("---")
st.subheader("📊 Readmission Summary Dashboard")

# Preview data
if st.checkbox("🔍 Show raw data sample"):
    st.dataframe(df.head(10))

# Grouped bar chart
st.markdown("### 🔁 Average Readmission Metrics by Hospital Type")

#grouped = df.groupby("hospital_type")["count_of_readm_measures_worse"].mean().sort_values(ascending=False)
grouped = df.groupby("facility_name")["count_of_readm_measures_worse"].mean().sort_values(ascending=False)


fig, ax = plt.subplots()
sns.barplot(x=grouped.values, y=grouped.index, ax=ax, palette="Blues_r")
ax.set_xlabel("Average Readmission Measures Rated Worse")
ax.set_ylabel("Hospital Type")

st.pyplot(fig)

st.markdown("---")
st.markdown(" Built by Shazia & Ace • Powered by Streamlit •  GitHub: [healthcare-readmission-analysis](https://github.com/ShaziaK354/healthcare-readmission-analysis)")

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label=" Download Readmission Data",
    data=csv,
    file_name='hospital_readmission_summary.csv',
    mime='text/csv',
)

with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=120)
    st.markdown("##  Healthcare Readmission")
    st.markdown(" Built with Streamlit")
    st.markdown(" Project: Predicting Hospital Readmission")
    st.markdown(" [View on GitHub](https://github.com/ShaziaK354/healthcare-readmission-analysis)")





