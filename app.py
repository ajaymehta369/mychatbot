from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("loan_model.pkl")

# ✅ Health check route
@app.get("/")
def read_root():
    return {"message": "FastAPI is running! Use /predict to check loan eligibility."}

# Request schema
class LoanApplicant(BaseModel):
    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: int

# ✅ Prediction route
@app.post("/predict")
def predict_loan(applicant: LoanApplicant):
    total_income = applicant.ApplicantIncome + applicant.CoapplicantIncome
    ratio = total_income / applicant.LoanAmount if applicant.LoanAmount != 0 else 0  # avoid division error

    input_data = [[
        applicant.Gender,
        applicant.Married,
        applicant.Dependents,
        applicant.Education,
        applicant.Self_Employed,
        applicant.ApplicantIncome,
        applicant.CoapplicantIncome,
        applicant.LoanAmount,
        applicant.Loan_Amount_Term,
        applicant.Credit_History,
        applicant.Property_Area,
        total_income,
        ratio
    ]]

    print("📦 Input to model:", input_data)

    try:
        prediction = model.predict(np.array(input_data))[0]
        result = "Yes" if prediction == 1 else "No"
        return {"Loan_Eligibility": result}
    except Exception as e:
        print("❌ Prediction Error:", e)
        return {"error": str(e)}
