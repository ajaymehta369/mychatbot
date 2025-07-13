# mychatbot
🏦 Loan Eligibility Prediction App
An end-to-end machine learning project that helps users check loan eligibility based on financial input. a Streamlit interface for user interaction. Deployed through Streamlit Cloud, this application demonstrates model serving, real-time API handling, and full-stack integration.

🚀 Features
- Machine learning model trained on loan eligibility data
- Streamlit UI for user-friendly interaction
- Hosted on GitHub and deployed using Streamlit Cloud
1. Clone the Repository
git clone https://github.com/<your-username>/loan-eligibility-app.git
cd loan-eligibility-app
2. Create a Virtual Environment
python -m venv venv
.\venv\Scripts\activate  # Windows
3. Install Dependencies
pip install -r requirements.txt

🧠 Model Details
- Algorithms used: Random Forest, Decision Tree
- Features:
- Gender, Married, Dependents
- Education, Self_Employed
- ApplicantIncome, CoapplicantIncome, LoanAmount
- Loan_Amount_Term, Credit_History, Property_Area
- Engineered: TotalIncome, IncomeLoanRatio
- Model saved with joblib as loan_model.pkl

💬 Streamlit Interface
Run locally:
streamlit run chatbot_ui.py
Or deploy via streamlit.io/cloud:
- Connect GitHub
- Select chatbot_ui.py
- It auto-installs from requirements.txt

📂 File Structure
loan-eligibility-app/
├── chatbot_ui.py         # Streamlit interface
├── loan_model.pkl        # Pretrained model
├── requirements.txt      # Dependencies
└── README.md             # Project documentation







