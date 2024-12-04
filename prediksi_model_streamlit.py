import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

# Load dataset and build model
data_path = "https://raw.githubusercontent.com/daruadiyatma/tes_data/refs/heads/main/data.csv"
data = pd.read_csv(data_path, sep=';')

scaler = MinMaxScaler()
numerical_columns = ['Unemployment_rate', 'Inflation_rate', 'Curricular_units_2nd_sem_grade', 'Curricular_units_1st_sem_grade', 'GDP']  
X = scaler.fit_transform(data[numerical_columns])
y = data['Status']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Streamlit app title
st.title("Graduate Prediction using Random Forest")

# Create input fields for user to enter flower features
st.sidebar.header("Input Features")

def user_input_features():
    Unemployment_rate = st.sidebar.slider("Unemployment rate", 7.6, 16.2, 10.2) 
    Inflation_rate = st.sidebar.slider("Inflation rate", 0.8, 3.7, 2.1)
    Curricular_units_1st_sem_grade = st.sidebar.slider("Curricular units 1st semester grade", 0.0, 18.5, 12.3)
    Curricular_units_2nd_sem_grade = st.sidebar.slider("Curricular units 2nd semester grade", 0.0, 18.8, 13.4)
    GDP = st.sidebar.slider("GDP", 0.0, 3.51, 2.7)
    
    data = {
        "Unemployment_rate": Unemployment_rate,
        "Inflation_rate": Inflation_rate,
        "Curricular_units_1st_sem_grade": Curricular_units_1st_sem_grade,
        "Curricular_units_2nd_sem_grade": Curricular_units_2nd_sem_grade,
        "GDP": GDP,
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display input features
st.subheader("User Input Features")
st.write(input_df)

# Make prediction
prediction_proba = model.predict_proba(input_df)

# Show prediction and probabilities
st.subheader("Prediction Probabilities")
st.write(prediction_proba)
