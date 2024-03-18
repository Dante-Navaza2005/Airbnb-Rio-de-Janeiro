
#* 4)  Import streamlit and create the code
import pandas as pd
import streamlit as st
import joblib

model = joblib.load("final_model.joblib")

#* 5)  Create and attribute the buttons to the loading of the model

x_numerical = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'year': 0, 'month': 0, 'Amount amenities': 0, 'host_listings_count': 0}

x_boolean = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {'property_type': ['Apartment', 'House'], 'room_type': ['Entire home/apt'], 'cancelation_policy': ['flexible', 'moderate', 'strict_14_with_grace_period']}

#* 6)  Finish deployment