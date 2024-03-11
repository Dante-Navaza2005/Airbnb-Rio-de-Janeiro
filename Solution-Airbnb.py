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
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#! 3) IMPORT AND CONSOLIDATE DATABASE

dataset_folder = pathlib.Path('dataset')
months = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
df_list = []


#* concatenating all the databases into one while adding the month and year collumns
for file in dataset_folder.iterdir() :
    month = months[file.name[:3]]

    year = int(file.name[-8:].replace('.csv', ''))

    df = pd.read_csv(file)
    df['month'] = month  
    df['year'] = year

    df_list.append(df)

main_dataframe = pd.concat(df_list)

#! 4) REDUCE EXCESSIVE AMOUNT OF COLLUMNS TO ENHANCE ALGORITHM EFFICIENCY
"""
As there are a lot of collumns, we are going to reduce the amount of collumns to enhance the algorithm efficiency. 
Furthermore, a rapid analysis of the data shows a significant number of redundant columns in the data for the prediction model, leading to the removal of the following collumns:
    1) Any collumn with unecessary data types that wont influence the final price such as images, verification methods, etc.
    2) ID: these quantitative values are unnecessary and could interfere with the final results as they would also be calculated.
    2) Repeated collumns: the data contains many columns that are repeated or very similar to each other, such as the date, state, and country.
    3) Any collumn that contains hyperlinks or free-form text: besides of not containing relevant data for the desired result, it could interfere with the prediction model.
    4) If over 30% of the data is missing we will remove that collumn
A excel file with the first 900 rows was generated in order to do a quick analysis of the data.    
main_dataframe.head(900).to_csv('first_900_rows.csv', sep=';', index=False)
"""

filtered_collumns = ['host_response_time','host_response_rate','host_is_superhost','host_listings_count','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','price','security_deposit','cleaning_fee','guests_included','extra_people','minimum_nights','maximum_nights','number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','instant_bookable','is_business_travel_ready','cancellation_policy','year','month']

main_dataframe = main_dataframe.loc[:, filtered_collumns]


#! 5) TREAT MISSING VALUES

#? Upon visualizing the dataset, it became apparent that certain columns contain a substantial amount of null values. Columns with over 30% of missing data will be entirely discarded, while those with fewer null values will undergo null value removal to ensure data integrity.

row_30_percent = main_dataframe.shape[0] * 0.3
for collumn in main_dataframe :
    if main_dataframe[collumn].isnull().sum() >= row_30_percent :
        main_dataframe = main_dataframe.drop(collumn, axis=1)

main_dataframe = main_dataframe.dropna()

#! 6) VERIFY THE DATA TYPES OF EACH COLLUMN

#? Following inspection the data types of each column, it is evident that the majority conform to their intended data types. However, the 'price' and 'extra people' columns are incorrectly represented as objects (strings) rather than integers as expected, necessitating a conversion to their appropriate data type.

#? Additionally, all data types of float64 and int64 will be converted to their 32-bit variants to optimize memory usage.

for collumn in main_dataframe :
    if main_dataframe[collumn].dtype == 'float64' :
        main_dataframe[collumn] = main_dataframe[collumn].astype(np.float32)
    elif main_dataframe[collumn].dtype == 'int64' :
        main_dataframe[collumn] = main_dataframe[collumn].astype(np.int32)

for collumn in ['price', 'extra_people'] :
    main_dataframe[collumn] = main_dataframe[collumn].str.replace(',', '').str.replace('$', '').astype(np.float32, copy=False) #used np.float32 to reduce memory usage


#! 7) EXPLORATORY ANALYSIS AND TREATMENT OF OUTLIERS
"""
- We will essentially examine each feature to:
    1. Conduct a correlation analysis among the features to ascertain their interrelationships and determine whether to retain all features. Features exhibiting strong correlations to the extent that they provide redundant information to the model will be removed. 
    2. Eliminate outliers (using a rule where values below Q1 - 1.5 * Interquartile Range and above Q3 + 1.5  Interquartile Range will be excluded). Interquartile Range (IQR) = Q3 - Q1.
    3. Verify if all features are relevant for our model or if any of them will not contribute and should be removed.

- We will begin with the columns of price (the ultimate target variable) and extra_people (also a monetary value). These are continuous numerical values.

- Next, we will analyze the columns of discrete numerical values (accommodates, bedrooms, guests_included, etc.).

- Finally, we will evaluate the text columns and determine which categories make sense to retain or discard.
"""

#* Making a heatmap from the correlation coefficient
plt.figure(figsize=(15,10))
sns.heatmap(main_dataframe.corr(numeric_only=True), annot=True)
plt.show()
print(main_dataframe.corr(numeric_only=True))

#? None of the correlation coefficients observed among the features reached a strength indicative of redundancy for the prediction model (excluding the coefficient of 1 present in the comparison of same features).

def calculate_limits(collumn) :
    q1 = collumn.quantile(0.25)
    q3 = collumn.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

print(calculate_limits(main_dataframe['price']))

#* Creating the graphs and removing outliers
def box_plot(main_dataframe_collumn) :
    plt.figure(figsize=(15,5))
    sns.boxplot(x = main_dataframe_collumn)
    plt.show()

def histogram(main_dataframe_collumn) :
    plt.figure(figsize=(15, 5))
    sns.histplot(x = main_dataframe_collumn, kde=True)
    plt.show()


#? Outliers above the upper limit represent luxury properties, which are not considered for the prediction model who's objective is to analyze common apparments, and thus should be removed. 

def exclude_outliers(main_df, collumn) :
    amount_lines = main_df.shape[0]
    lower_limit, upper_limit = calculate_limits(main_df[collumn])
    main_df = main_df.loc[(main_df[collumn] >= lower_limit) & (main_df[collumn] <= upper_limit), :]
    return main_df, amount_lines - main_df.shape[0]

for collumn in ['price', 'extra_people'] :
    main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, collumn)

    print(f"{amount_removed_lines} lines were removed from {collumn}")
    histogram(main_dataframe[collumn])
    box_plot(main_dataframe[collumn])

#? Obs: when the price collumn is a integer, the quantity of apparments increases because landlords usally put their price as a whole value.

#? Now we will analyze the columns of discrete numerical values (accommodates, bedrooms, guests_included, etc.) Excluding the 'price' and 'extra people' collumns and any non-numerical collumns.

def bar_graph(main_dataframe_collumn) :
    plt.figure(figsize=(15, 5))
    ax = sns.barplot(x = main_dataframe_collumn.value_counts().index, y = main_dataframe_collumn.value_counts())
    ax.set_xlim(calculate_limits(main_dataframe_collumn))
    plt.show()

#? The 'guests_included' column will be disregarded from the model's analysis due to its significant skew towards a single value, specifically 1, indicating a maximum limit of one guest per residency. Removing this column from the analysis as a whole is essential as excluding only the outliers could significantly influence the final result. Moreover, this concentration likely stems from data entry errors, as typical housing accommodations should accommodate more than one person.

#*main_dataframe.drop('guests_included')

#? The 'maximum_nights' column will also be diregarded from the model's analysis as not only it doesn't contribute signficiantly to a variation in the price, but also a large amount of the data is in the collumn 0, which represents that most users didn't fill out this area when searching for a residence.
    
for collumn in ['host_listings_count','accommodates', 'bathrooms', 'beds','bedrooms', 'minimum_nights'] :
    main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, collumn)
    print(f"{amount_removed_lines} lines were removed from {collumn}")
    box_plot(main_dataframe[collumn])
    bar_graph(main_dataframe[collumn])

plt.figure(figsize=(15,5))
sns.barplot(x = main_dataframe['guests_included'].value_counts().index, y = main_dataframe['guests_included'].value_counts())
plt.show()




#! 8) ENCODING TO ALLOW FOR MACHINE LEARNING

#! 9) PREDICTION MODELS

#! 10) ANALYZE THE BEST MODEL

#! 11) ADJUSTING AND IMPROVING THE BEST MODEL