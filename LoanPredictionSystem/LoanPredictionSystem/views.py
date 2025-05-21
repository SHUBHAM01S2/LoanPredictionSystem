from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    # 1) Load raw data
    df = pd.read_csv(
        '/home/shubham-sharma/Desktop/Machine Learning Projects/'
        'Loan-Prediction-System/train_u6lujuX_CVtuZ9i.csv'
    )

    # 2) Keep only the 6 features + target
    df = df[['Gender','Married','Education','Self_Employed',
             'ApplicantIncome','LoanAmount','Loan_Status']].copy()

    # 3) Fill missing
    df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
    df['Married'].fillna(df['Married'].mode()[0], inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)

    # 4) Separate inputs & target
    X = df.drop('Loan_Status', axis=1)
    y = df['Loan_Status']

    # 5) Encode only the categorical INPUT columns
    cat_cols = ['Gender','Married','Education','Self_Employed']
    enc = OrdinalEncoder()
    X[cat_cols] = enc.fit_transform(X[cat_cols])

    # 6) Train/test split + model
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    rf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
    rf.fit(X_train, y_train)

    # 7) Read your 6 form inputs
    gender         = request.GET.get('gender')
    married        = request.GET.get('married')
    education      = request.GET.get('education')
    self_employed  = request.GET.get('self_employed')
    applicant_inc  = float(request.GET.get('applicant_income'))
    loan_amount    = float(request.GET.get('loan_amount'))

    # 8) Build a single-row DataFrame and encode it
    input_df = pd.DataFrame(
        [[gender, married, education, self_employed,
          applicant_inc, loan_amount]],
        columns=['Gender','Married','Education','Self_Employed',
                 'ApplicantIncome','LoanAmount']
    )
    input_df[cat_cols] = enc.transform(input_df[cat_cols])

    # 9) Predict!
    pred = rf.predict(input_df)[0]
    status = "Approved ✅" if pred == 1 else "Rejected ❌"

    # 10) Show result
    return render(request, 'predict.html', {
        "result2": f"Loan Status: {status}"
    })
