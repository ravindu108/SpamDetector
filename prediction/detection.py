# -*- coding: utf-8 -*-
"""Spam Mail Prediction using Machine Learning"""

# Importing the Dependencies
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Data Collection & Pre-Processing

# Loading the data from the CSV file to a pandas DataFrame
raw_mail_data = pd.read_csv("prediction/mailData.csv")

# Replace the null values with a null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), "")

# Label Encoding

# Label spam mail as 0 and ham mail as 1
mail_data["Category"] = mail_data["Category"].map({"spam": 0, "ham": 1})

# Separating the data as texts and labels
X = mail_data["Message"]
Y = mail_data["Category"]

# Feature Extraction

# Transform the text data to feature vectors that can be used as input to Logistic Regression
feature_extraction = TfidfVectorizer(min_df=1, stop_words="english", lowercase=True)

X_features = feature_extraction.fit_transform(X)

# Convert Y values to integers
Y = Y.astype("int")

# Training the Model (Logistic Regression)
model = LogisticRegression()

# Training the Logistic Regression model with the entire dataset
model.fit(X_features, Y)

# The main prediction function
def classify(input_mail):
    # Convert user input to a feature vector
    input_data_features = feature_extraction.transform([input_mail])

    # Making prediction
    prediction = model.predict(input_data_features)

    if prediction[0] == 1:
        # Is not a spam email
        return False
    else:
        # Is a spam email
        return True
