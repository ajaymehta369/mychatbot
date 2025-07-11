import streamlit as st
import requests
st.title("Loan Eligibility Assistant 🏦")
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
    payload = {
        "Gender": 1 if gender == "Male" else 0,
        "Married": 1 if married == "Yes" else 0,
        "Dependents": int(dependents.replace("+", "")),
        "Education": 0 if education == "Graduate" else 1,
        "Self_Employed": 1 if self_employed == "Yes" else 0,
        "ApplicantIncome": income,
        "CoapplicantIncome": co_income,
        "LoanAmount": loan_amt,
        "Loan_Amount_Term": term,
        "Credit_History": credit,
        "Property_Area": {"Urban": 2, "Semiurban": 1, "Rural": 0}[area],
        "TotalIncome": total_income,
        "IncomeLoanRatio": income_ratio
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload).json()
        if response["Loan_Eligibility"] == "Yes":
            st.success("🎉 You're eligible for a loan!")
        else:
            st.error("❌ Sorry, you're not eligible right now.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
