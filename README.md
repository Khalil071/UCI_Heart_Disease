Project Overview

This project aims to predict heart disease using machine learning models. It involves data preprocessing, exploratory data analysis (EDA), feature selection, model training, and API deployment using Flask.

Steps Implemented

Data Preprocessing
The dataset was loaded from UCI_Heart_Disease_Data.csv.

Missing values in numerical columns were replaced with their median values.

Categorical variables were imputed using their most frequent values.

Label Encoding was applied to categorical features.

Exploratory Data Analysis (EDA)
Statistical summaries and unique values of categorical features were analyzed.

The correlation matrix was plotted to identify relationships between features.

Data imbalance was handled using SMOTE (Synthetic Minority Over-sampling Technique).

Visualizations were generated to analyze relationships between age, cholesterol levels, and disease severity.

Feature Selection
Feature importance was analyzed using Random Forest.

SelectKBest method was used to select the most significant features for prediction.

Model Building & Evaluation
Multiple models were trained and evaluated:

Random Forest Classifier

XGBoost Classifier

The best model was selected based on accuracy and classification reports.

Hyperparameter tuning was performed using GridSearchCV to optimize the XGBoost model.

The confusion matrix was plotted for model evaluation.

Model Deployment
The best model was saved as a pickle file (xgb_model.pkl).

A Flask API was created to serve predictions.

API testing was conducted using Postman.

API Usage (Postman)

Endpoint:

POST /predict

Request Body (JSON):

{ "age": 45, "cp": 2, "thalach": 150, "exang": 1, "oldpeak": 2.3, "sex": 1, "trestbps": 160, "chol": 230, "fbs": 0, "restecg": 1, "slope": 1, "ca": 3, "thal": 1, "dataset": 0 }

Response:

{ "prediction": 3 }

Repository Structure

|-- data/ | |-- UCI_Heart_Disease_Data.csv |-- models/ | |-- best_xgb_model.json |-- src/ | |-- data_preprocessing.py | |-- model_training.py | |-- feature_selection.py | |-- model_api.py |-- README.md |-- requirements.txt

Installation

To run the project locally, install the dependencies:

1. Create a virtual environment
python -m venv myenv

2. Activate the virtual environment On Windows:
myenv\Scripts\activate

3. Install project dependencies
pip install -r requirements.txt

4. Load the model
Ensure that the trained model file (best_xgb_model.json) is in the same directory as the Flask application (app.py).

5. Run Flask API and 
python app.py

6. Testing the API
You can send POST requests to the /predict endpoint to get predictions.

Example request (using Postman):

url = "http://127.0.0.1:5000/predict"

Sample JSON Body: {
  "features": [63, 1, 3, 145, 233, 1, 0, 150, 1, 0, 2.3, 0, 0, 1]
}

Response:
{
  "prediction": 3,
  "probability": [
    0.08369526267051697,
    0.008033085614442825,
    0.005890870466828346,
    0.8939110636711121,
    0.00846966914832592
  ]
}

