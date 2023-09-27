# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    Location: int
    MinimumTemperature: float
    MaximumTemperature: float
    Rainfall: float
    Evaporation: float
    Sunshine: float
    WindGustDirection: float
    WindGustSpeed: float
    WindDirection9am: float
    WindDirection3pm: float
    WindSpeed9am: float
    WindSpeed3pm: float
    Humidity9am: float
    Humidity3pm: float
    Pressure9am: float
    Pressure3pm: float
    Cloud9am: float
    Cloud3pm: float
    Temperature9am: float
    Temperature3pm: float
    CloudBurstToday: int