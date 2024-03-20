
#* 4)  Import streamlit and create the code
import pandas as pd
import streamlit as st
import joblib

model = joblib.load("final_model.joblib")

#* 5)  Create and attribute the buttons to the loading of the model

#? We will create three dictionaries for each diferent data type (numerical, boolean and lists). We will then create a button for each dictionary and update the values of each column depending on the input.
x_numerical = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'year': 0, 'month': 0, 'Amount amenities': 0, 'host_listings_count': 0}

x_boolean = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {'property_type': ['Apartment', 'House'], 'room_type': ['Entire home/apt', 'room_type_Private room'], 'cancelation_policy': ['flexible', 'moderate', 'strict_14_with_grace_period']}

#? Creating a button for each dictionary and updating the values after the user's input
for item in x_numerical :
    value = st.number_input(f'{item}')
    x_numerical[item] = value

for item in x_boolean :
    value = st.selectbox(f'{item}', ('Yes', 'No'))
    if value == 'Yes' :
        x_boolean[item] = 1
    else :
        x_boolean[item] = 0

for item in x_lists :
    value = st.selectbox(f'{item}', x_lists[item])

preview_button = st.button("View the predicted value")

#* 6)  Finish deployment