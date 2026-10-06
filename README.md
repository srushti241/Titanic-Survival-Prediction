Titanic Survival Prediction 🚢
Project Overview

This project uses Machine Learning to predict whether a passenger on the Titanic would survive based on passenger information.

A Logistic Regression classification model is used to make the prediction.

Dataset

The project uses the Titanic dataset.

The target variable is:

Survived

0 = Did not survive

1 = Survived

Features Used

The model uses the following features:

Pclass - Passenger class

Age - Passenger age

SibSp - Number of siblings/spouses aboard

Parch - Number of parents/children aboard

Fare - Passenger fare

Machine Learning Model

The project uses:

Logistic Regression

The dataset is divided into training and testing data. The model is trained using the training data and evaluated using the test data.

Project Structure
Titanic/
│
├── app.py
├── model.pkl
├── data/
├── titanic.ipynb
├── requirements.txt
└── README.md

Streamlit Application

A Streamlit web application is created to allow users to enter passenger information and receive a survival prediction.

The application predicts:

🎉 Survived

❌ Did Not Survive

How to Run the Project
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder
cd Titanic

3. Install the required libraries
pip install -r requirements.txt

4. Run the Streamlit application
streamlit run app.py


The application will open in your web browser.

Model Workflow
Titanic Dataset
       ↓
Data Cleaning
       ↓
Feature Selection
       ↓
Train/Test Split
       ↓
Logistic Regression
       ↓
Model Evaluation
       ↓
Save Model
       ↓
Streamlit Application
       ↓
Survival Prediction

Technologies Used

Python

Pandas

Scikit-learn

Joblib

Streamlit

Jupyter Notebook

Author

Your Name