import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("loan_model.pkl")

st.title("Loan Eligibility Assistant 🏦")

# Collect inputs from user
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)
loan_amt = st.number_input("Loan Amount", min_value=1)
term = st.selectbox("Loan Term (months)", [360, 120, 180, 240])
credit = st.selectbox("Credit History", [1.0, 0.0])
area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

if st.button("Check Eligibility"):
    total_income = income + co_income
    income_ratio = total_income / loan_amt if loan_amt != 0 else 0

    # Prepare input data for the model
    input_data = np.array([[
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        int(dependents.replace("+", "")),
        0 if education == "Graduate" else 1,
        1 if self_employed == "Yes" else 0,
        income,
        co_income,
        loan_amt,
        term,
        credit,
        {"Urban": 2, "Semiurban": 1, "Rural": 0}[area],
        total_income,
        income_ratio
    ]])

    # Run prediction
    try:
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.success("🎉 You're eligible for a loan!")
        else:
            st.error("❌ Sorry, you're not eligible right now.")
    except Exception as e:
        st.error(f"Prediction error: {e}")
