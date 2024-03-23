#* 4)  Import streamlit and create the code
import pandas as pd
import streamlit as st
import joblib

#* 5)  Create and attribute the buttons to the loading of the model

#? We will create three dictionaries for each diferent data type (numerical, boolean and lists). We will then create a button for each dictionary and update the values of each column depending on the input.
x_numerical = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'year': 0, 'Amount amenities': 0, 'host_listings_count': 0}

x_boolean = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {'property_type': ['Apartment', 'House'], 'room_type': ['Entire home/apt', 'room_type_Private room'], 'cancellation_policy': ['flexible', 'moderate', 'strict_14_with_grace_period']}

#? Now we will create another dictionary containing only the lists created by the dummy variables. This is so we can store the values the user enters. 
list_values = {'property_type_Apartment' : 0, 'property_type_House' : 0, 'room_type_Entire home/apt' : 0, 'room_type_Private room' : 0, 'cancellation_policy_flexible' : 0, 'cancellation_policy_moderate' : 0, 'cancellation_policy_strict_14_with_grace_period' : 0}


st.set_page_config(page_title="Airbnb Deployment", page_icon=":shark:")
st.title("Airbnb Machine Learning Model Deployment")

st.write("If you don't have the file of the model, download it [here](https://drive.google.com/file/d/1VMhrCh5l2neipciZF15Y1lBDS02lgeN5/view?usp=sharing)")

final_model = st.text_input("Enter the complete path of the file of the model")

#? Creating a button for each dictionary and updating the values after the user's input
#? Some buttons such as the latitude and logitude, will have float values and others will have integer, we will adjust their values as needed.
for item in x_numerical :
    if item == 'latitude' or item == 'longitude' :
        value = st.number_input(f'{item}', step=0.000001, value=0.0, format="%.6f")
    elif item == 'extra_people' :
        value = st.number_input(f'{item}', step=0.01, value = 0.0) #? default decimal places for floats are already two, so no format is needed
    else :
        value = st.number_input(f'{item}', step = 1, value = 0)
    x_numerical[item] = value

for item in x_boolean :
    value = st.selectbox(f'{item}', ('Yes', 'No'))
    if value == 'Yes' :
        x_boolean[item] = 1
    else :
        x_boolean[item] = 0

#? We will iterate over each element of the list_value dictionary, as it is the one that stores the values the user enters
for item in x_lists :
    value = st.selectbox(f'{item}', x_lists[item])
    list_values[f'{item}_{value}'] = 1

#? Lastly, we will create a button for the user to see the predicted value
    
preview_button = st.button("View the predicted value")

if preview_button :
    #? We will join all the dictionaries so we can transform them into a dataframe for the machine learning model to use.
    list_values.update(x_numerical)
    list_values.update(x_boolean)

    x_value_dataframe = pd.DataFrame(list_values, index = [0])

    #? As the data has to be in the same order as the data the model trained upon, we will create a list containing the columns in the same order (excluding the first column which is for indexing and the last column ('Price') which was implemented after the training).
    data = pd.read_csv("final_data.csv")
    column_order_list = list(data.columns)[1:-1]

    #? We will use the column order list to rearrange the columns in the dataframe
    x_value_dataframe = x_value_dataframe[column_order_list]

    model = joblib.load(final_model)
    prediction = model.predict(x_value_dataframe)


    st.write(f"The predicted value is R$ {prediction[0]:.2f}")

#* 6)  Finish deployment
