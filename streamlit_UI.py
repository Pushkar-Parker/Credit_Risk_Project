import streamlit as st
from predictions import predict

# Title
st.title("Credit Default Risk Predictor")

# Expected columns and their data types
expected_cols = [
    'credit_utilization_ratio',
    'loan_tenure_months',
    'sanction_amount',
    'number_of_open_accounts',
    'age',
    'loan_purpose',
    'residence_type',
    'loan_type',
    'loan_amount',
    'delinquent_months',
    'total_dpd'
]

# Categorical columns and their categories
loan_purpose_options = ['Home', 'Personal', 'Auto', 'Education']
loan_type_options = ['Secured', 'Unsecured']
residence_type_options = ['Rented', 'Owned', 'Mortgage']

# Create input fields for the user to enter data
st.header("Enter the following details:")

# Numerical inputs
credit_utilization_ratio = st.slider("Credit Utilization Ratio", min_value=0.0, max_value=1.0, step=0.01)
loan_tenure_months = st.slider("Loan Tenure (Months)", min_value=1, max_value=360, step=1)
sanction_amount = st.number_input("Sanction Amount", min_value=1000.0, max_value=1_000_000.0, step=1000.0)
number_of_open_accounts = st.slider("Number of Open Accounts", min_value=0, max_value=50, step=1)
age = st.slider("Age", min_value=18, max_value=100, step=1)
loan_amount = st.number_input("Loan Amount", min_value=1000.0, max_value=1_000_000.0, step=1000.0)
delinquent_months = st.slider("Delinquent Months", min_value=0, max_value=120, step=1)
total_dpd = st.number_input("Total Days Past Due (DPD)", min_value=0.0, max_value=1000.0, step=1.0)
income = st.number_input("Income", min_value=1000.0, max_value=1_000_000.0, step=1000.0)

# Categorical inputs
loan_purpose = st.selectbox("Loan Purpose", loan_purpose_options)
residence_type = st.selectbox("Residence Type", residence_type_options)
loan_type = st.selectbox("Loan Type", loan_type_options)

# Predict button
if st.button("Predict"):
    # Create a dictionary of inputs
    input_data = {
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_tenure_months': loan_tenure_months,
        'sanction_amount': sanction_amount,
        'number_of_open_accounts': number_of_open_accounts,
        'age': age,
        'loan_purpose': loan_purpose,
        'residence_type': residence_type,
        'loan_type': loan_type,
        'loan_amount': loan_amount,
        'delinquent_months': delinquent_months,
        'total_dpd': total_dpd,
        'income': income
    }

    prediction = predict(input_data)

    st.success(prediction)