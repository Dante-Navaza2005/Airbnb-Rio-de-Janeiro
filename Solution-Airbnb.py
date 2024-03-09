"""
RIO DE JANEIRO AIRBNB PROJECT - PRICE PREDICTION MODEL FOR COMMON USERS

#! 1) CONTEXT AND OBJECTIVE

Airbnb allows anyone with a spare room or property of any type (apartment, house, chalet, inn, etc.) to list their property for rent on a daily basis.

As a host, you create your profile and list your property. In this listing, hosts should provide a comprehensive description of the property to assist renters/travelers in choosing the best accommodation and to make their listing more appealing.

There are numerous customizations available in the listing, ranging from minimum stay requirements, pricing, number of rooms, to cancellation policies, extra guest fees, identity verification requirements for renters, etc.

### Our Objective

To build a price prediction model that enables property owners to determine the appropriate daily rate for their property. Additionally, to assist renters in evaluating whether a listed property offers a competitive price compared to similar properties with similar characteristics.

### Available Resources, Inspirations, and Credits

The datasets were sourced from Kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro. Data spans from April 2018 to May 2020, with the exception of June 2018, which lacks data.

Given the 50MB per file space restriction in GitHub Repositories, the datasets utilized in this project are accessible for download via this link: https://drive.google.com/file/d/1_RtxDTXtF3CGvioFi1_ophzLNmyguEHl/view?usp=sharing. Alternatively, you may procure the datasets directly from Kaggle. However, it's noteworthy that discrepancies may arise in results if the datasets have been updated subsequent to the project's inception.

- File names are in brazilian portuguese
- The datasets contain property prices and their respective characteristics for each month.
- Prices are listed in Brazilian Real (R$).

### Initial Expectations

- Seasonality is expected to be a significant factor, as months like December tend to have higher prices in Rio de Janeiro.
- Property location is likely to have a substantial impact on pricing, given that location can drastically alter the characteristics of a place (e.g., safety, natural beauty, proximity to tourist attractions).
- Additional amenities may have a significant impact, considering the prevalence of older buildings and houses in Rio de Janeiro.

We aim to explore the extent to which these factors influence pricing and identify any less intuitive yet crucial factors.
"""

#! 2) IMPORT LIBRARIES  

import pandas as pd
import pathlib


#! 3) IMPORT AND CONSOLIDATE DATABASE

dataset_folder = pathlib.Path('dataset')
months = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
df_list = []


#* concatenating all the databases into one and adding the month and year collumns
for file in dataset_folder.iterdir() :
    month = months[file.name[:3]]

    year = int(file.name[-8:].replace('.csv', ''))

    df = pd.read_csv(file)
    df['month'] = month  
    df['year'] = year

    df_list.append(df)

base_dataframe = pd.concat(df_list)

#! 4) REDUCE EXCESSIVE AMOUNT OF COLLUMNS TO ENHANCE ALGORITHM EFFICIENCY
"""
As there are a lot of collumns, we are going to reduce the amount of collumns to enhance the algorithm efficiency. 
Furthermore, a rapid analysis of the data shows a significant number of redundant columns in the data for the prediction model, leading to the removal of the following collumns:
    1) Any collumn with unecessary data types that wont influence the final price such as images, verification methods, etc.
    2) ID: these quantitative values are unnecessary and could interfere with the final results as they would also be calculated.
    2) Repeated collumns: the data contains many columns that are repeated or very similar to each other, such as the date, state, and country.
    3) Any collumn that contains hyperlinks or free-form text: besides of not containing relevant data for the desired result, it could interfere with the prediction model.
    4) If over 50% of the data is missing it will remove that collumn
A excel file with the first 900 rows will be generated in order to do a quick analysis of the data.    
"""
base_dataframe.head(900).to_csv('900_rows.csv', sep=';', index=False)

filtered_collumns = ['host_response_time','host_response_rate','host_is_superhost','host_listings_count','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','price','security_deposit','cleaning_fee','guests_included','extra_people','minimum_nights','maximum_nights','number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','instant_bookable','is_business_travel_ready','cancellation_policy','year','month']

base_dataframe = base_dataframe.loc[:, filtered_collumns]
print(base_dataframe)

#! 5) TREAT MISSING VALUES

#! 6) VERIFY THE DATA TYPES OF EACH COLLUMN

#! 7) EXPLORATORY ANALYSIS AND TREATMENT OF OUTLIERS

#! 8) ENCODING TO ALLOW FOR MACHINE LEARNING

#! 9) PREDICTION MODELS

#! 10) ANALYZE THE BEST MODEL

#! 11) ADJUSTING AND IMPROVING THE BEST MODEL