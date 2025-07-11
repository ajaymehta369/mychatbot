import requests

payload = {
    "Gender": 1,
    "Married": 1,
    "Dependents": 0,
    "Education": 0,
    "Self_Employed": 0,
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 0,
    "LoanAmount": 120,
    "Loan_Amount_Term": 360,
    "Credit_History": 1.0,
    "Property_Area": 2
}

response = requests.post("http://127.0.0.1:8000/predict", json=payload)
print(response.json())
