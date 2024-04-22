# Importing streamlit and starting to create buttons

Importing all necessary libraries:

```python
import pandas as pd
import streamlit as st
import joblib
import sys
from streamlit.web import cli as stcli
import os
```

Setting up the directories and making sure all requirements are installed:

```python
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

sys.argv = ["pip", "install", "-r", "requirements.txt"]
```

Now, we will write the code below in order to automatically run the streamlit website locally everytime the file is executed:

```python
try :
    if __name__ == '__main__':
            sys.argv = ["streamlit", "run", "airbnb_deploy.py"]
            sys.exit(stcli.main()) 
except RuntimeError as e:
    if str(e) == "Runtime instance already exists!":
        pass
```

**Obs:** This code **should always** be kept on the **bottom** of the file as it will instantly open the website with only the features of the code above it!

Now, in order to make the buttons for each feature used in the prediction model's analysis, we will first create three dictionaries for each diferent data type (numerical, boolean and lists).

Then, we will create a button for each dictionary and update the values of each column depending on the input.

Creating the dictionaries:

```
x_numerical = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0, 'year': 0, 'Amount amenities': 0, 'host_listings_count': 0}

x_boolean = {'host_is_superhost': 0, 'instant_bookable': 0}

x_lists = {'property_type': ['Apartment', 'House'], 'room_type': ['Entire home/apt', 'room_type_Private room'], 'cancellation_policy': ['flexible', 'moderate', 'strict_14_with_grace_period']}
```
