# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Banknotes import BankNote
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()
pickle_in = open("C:\\Users\\AKSHAT\\PycharmProjects\\deployment\\xgboost.pkl", "rb")
classifier = pickle.load(pickle_in)



# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}


# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To weather foretelling': f'{name}'}


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_cloudburst(data: BankNote):
    features = np.array([
        data.Location,
        data.MinimumTemperature,
        data.MaximumTemperature,
        data.Rainfall,
        data.Evaporation,
        data.Sunshine,
        data.WindGustDirection,
        data.WindGustSpeed,
        data.WindDirection9am,
        data.WindDirection3pm,
        data.WindSpeed9am,
        data.WindSpeed3pm,
        data.Humidity9am,
        data.Humidity3pm,
        data.Pressure9am,
        data.Pressure3pm,
        data.Cloud9am,
        data.Cloud3pm,
        data.Temperature9am,
        data.Temperature3pm,
        data.CloudBurstToday
    ]).reshape(1, -1)
    # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict(features)
    if prediction[0] > 0.5:
        prediction = "yes its a cloudburst"
    else:
        prediction = "Nope not a cloudburst"
    return {
        'prediction': prediction
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload