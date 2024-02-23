import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('churn_prediction_model.pkl')

# Function to make predictions
def predict_churn(features):
    # Define the order of features to match x_train.columns
    feature_names = ['credit_score', 'age', 'tenure', 'balance', 'products_number',
                     'credit_card', 'active_member', 'estimated_salary', 
                     'country_France', 'country_Germany', 'country_Spain',
                     'gender_Female', 'gender_Male']
    
    # Create a DataFrame with the input features in the correct order
    input_data = pd.DataFrame([features], columns=feature_names)
    
    # Predict churn
    prediction = model.predict(input_data)
    return prediction[0]

# UI
st.title('Churn Prediction App')

# User inputs
credit_score = st.slider('Credit Score', 300, 850, 700)
age = st.slider('Age', 18, 100, 35)
tenure = st.slider('Tenure', 0, 10, 5)
balance = st.number_input('Balance', min_value=0.0, max_value=1e6, value=5000.0)
products_number = st.slider('Number of Products', 1, 5, 2)
credit_card = st.selectbox('Has Credit Card', ['Yes', 'No'])
active_member = st.selectbox('Active Member', ['Yes', 'No'])
estimated_salary = st.number_input('Estimated Salary', min_value=0.0, max_value=1e6, value=50000.0)
gender = st.selectbox('Gender', ['Female', 'Male'])
country = st.selectbox('Country', ['France', 'Germany', 'Spain'])

# Button to trigger prediction
if st.button('Predict Churn'):
    # Map user inputs to feature values
    features = {
        'credit_score': credit_score,
        'age': age,
        'tenure': tenure,
        'balance': balance,
        'products_number': products_number,
        'credit_card': 1 if credit_card == 'Yes' else 0,
        'active_member': 1 if active_member == 'Yes' else 0,
        'estimated_salary': estimated_salary,
        'gender_Female': 1 if gender == 'Female' else 0,
        'gender_Male': 1 if gender == 'Male' else 0,
        'country_France': 1 if country == 'France' else 0,
        'country_Germany': 1 if country == 'Germany' else 0,
        'country_Spain': 1 if country == 'Spain' else 0
    }
    # Predict churn
    churn_prediction = predict_churn(features)
    if churn_prediction == 0:
        st.write('0\nChurn Prediction: Not Churning')
    else:
        st.write('1\nChurn Prediction: Churning')
