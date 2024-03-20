"""
RIO DE JANEIRO AIRBNB PROJECT - PRICE PREDICTION MODEL FOR COMMON USERS

#! 1) CONTEXT AND OBJECTIVE

Airbnb allows anyone with a spare room or property of any type (apartment, house, chalet, inn, etc.) to list their property for rent on a daily basis.

As a host, you create your profile and list your property. In this listing, hosts should provide a comprehensive description of the property to assist renters/travelers in choosing the best accommodation and to make their listing more appealing.

There are numerous customizations available in the listing, ranging from minimum stay requirements, pricing, number of rooms, to cancellation policies, extra guest fees, identity verification requirements for renters, etc.

### Our Objective

To build a price prediction model that enables property owners to determine the appropriate daily rate for their property. Additionally, to assist renters in evaluating whether a listed property offers a competitive price compared to similar properties with similar characteristics.

### Available Resources, Inspirations, and Credits

The datasets were sourced from Kaggle: https://www.kaggle.com/datasets/allanbruno/airbnb-rio-de-janeiro. Data spans from April 2018 to May 2020, with the exception of June 2018, which lacks data.

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

#? for path management
import os
import pathlib
import joblib
#? for data manipulation
import pandas as pd 
import numpy as np
#? for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import webbrowser
#? for machine learning
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split


#! 3) IMPORT AND CONSOLIDATE DATABASE

dataset_folder = pathlib.Path('dataset')
months = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
df_list = []



#* concatenating all the databases into one while adding the month and year columns
for file in dataset_folder.iterdir() :
    month = months[file.name[:3]]

    year = int(file.name[-8:].replace('.csv', ''))

    df = pd.read_csv(file)
    df['month'] = month  
    df['year'] = year

    df_list.append(df)

main_dataframe = pd.concat(df_list)

#! 4) REDUCE EXCESSIVE AMOUNT OF columns TO ENHANCE ALGORITHM EFFICIENCY
"""
As there are a lot of columns, we are going to reduce the amount of columns to enhance the algorithm efficiency. 
Furthermore, a rapid analysis of the data shows a significant number of redundant columns in the data for the prediction model, leading to the removal of the following columns:
    1) Any collumn with unecessary data types that wont influence the final price such as images, verification methods, etc.
    2) ID: these quantitative values are unnecessary and could interfere with the final results as they would also be calculated.
    2) Repeated columns: the data contains many columns that are repeated or very similar to each other, such as the date, state, and country.
    3) Any collumn that contains hyperlinks or free-form text: besides of not containing relevant data for the desired result, it could interfere with the prediction model.
    4) If over 30% of the data is missing we will remove that collumn
A excel file with the first 900 rows was generated in order to do a quick analysis of the data.    
main_dataframe.head(900).to_csv('first_900_rows.csv', sep=';', index=False)
"""

filtered_columns = ['host_response_time','host_response_rate','host_is_superhost','host_listings_count','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','price','security_deposit','cleaning_fee','guests_included','extra_people','minimum_nights','maximum_nights','number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','instant_bookable','is_business_travel_ready','cancellation_policy','year','month']

main_dataframe = main_dataframe.loc[:, filtered_columns]


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


#! 7.1) EXPLORATORY ANALYSIS AND TREATMENT OF OUTLIERS FOR NUMERICAL VALUES
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
###plt.show()

#? None of the correlation coefficients observed among the features reached a strength indicative of redundancy for the prediction model (excluding the coefficient of 1 present in the comparison of same features).

def calculate_limits(collumn) :
    q1 = collumn.quantile(0.25)
    q3 = collumn.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

# print(calculate_limits(main_dataframe['price']))

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
    ###histogram(main_dataframe[collumn])
    ###box_plot(main_dataframe[collumn])

#? Obs: when the price collumn is a integer, the quantity of apparments increases because landlords usally put their price as a whole value.

#? Now we will analyze the columns of discrete numerical values (accommodates, bedrooms, guests_included, etc.) Excluding the 'price' and 'extra people' columns and any non-numerical columns.

def bar_graph(main_dataframe_collumn) :
    plt.figure(figsize=(15, 5))
    ax = sns.barplot(x = main_dataframe_collumn.value_counts().index, y = main_dataframe_collumn.value_counts())
    ax.set_xlim(calculate_limits(main_dataframe_collumn))
    plt.show()

"""
The 'guests_included' column will be disregarded from the model's analysis due to its significant skew towards a single value, specifically 1, indicating a maximum limit of one guest per residency. 
Removing this column from the analysis as a whole is essential as excluding only the outliers could significantly influence the final result. 
Moreover, this concentration likely stems from data entry errors, as typical housing accommodations should accommodate more than one person.
"""

main_dataframe = main_dataframe.drop('guests_included', axis = 1)

#? The 'number_of_reviews' column will be disregarded from the model's analysis as its goal is to analyzze the price for normal users and landlords, which in most cases won't have reviews or a large number of them. Also simpler models are faster and less prone to overfitting.
main_dataframe = main_dataframe.drop('number_of_reviews', axis = 1)

#? The 'maximum_nights' column will also be diregarded from the model's analysis as not only it doesn't contribute signficiantly to a variation in the price, but also a large amount of the data is in the collumn 0, which represents that most users didn't fill out this area when searching for a residence.

main_dataframe = main_dataframe.drop('maximum_nights', axis = 1)

#* Removing the outliers of the remaining columns
for collumn in ['host_listings_count','accommodates', 'bathrooms', 'beds','bedrooms', 'minimum_nights'] :
    main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, collumn)
    print(f"{amount_removed_lines} lines were removed from {collumn}")
    ###box_plot(main_dataframe[collumn])
    ###bar_graph(main_dataframe[collumn])


#! 7.2) EXPLORATORY ANALYSIS AND TREATMENT OF OUTLIERS FOR TEXT VALUES
"""
First we will analyze the columns without true or false and list values:
- 'property_type'
- 'bed_type'
- 'room_type'
- 'cancellation_policy'
"""

#? First, we will create a function to group specific categories of a given collumn in case said collumn contains a significant amount of categories with small values (value determined by the 'amount' parameter). 

def group_categories(collumn, grouped_category_name, amount) :
    series_category = main_dataframe[collumn].value_counts()

    for category_type in series_category.index :
        if series_category[category_type] < amount :
            main_dataframe.loc[main_dataframe[collumn] == category_type, collumn] = grouped_category_name

    plt.figure(figsize=(15,10))
    category_graph = sns.countplot(x = main_dataframe[collumn])
    category_graph.tick_params(axis='x', rotation=90)
    ###plt.show()



#? Starting with the 'property_type' collumn, we will group all the entires will less than 2000 entries into the 'Other' category since they had a significant amount of categories and their low numbers would make the model more complex and less efficient.

group_categories('property_type', 'Other', 2000)

#? Next, the 'bed_type' collumn only has 5 categories, however only the 'real_bed' category has significant values, while the others have small, broken values. Therefore, we will group all these entries into a 'Other beds' category. (The amount 10,000 was chosen simply to choose the remaining categories)

group_categories('bed_type', 'Other beds', 10000)

#? Next, the 'room_type' collumn only has 4 categories whithout any major value discrepancies in the data (only two categories have significant smaller values), so no change/grouping of categories will be needed.

#? Finally, the 'cancellation_policy' collumn has 3 categories (strict, super_strict_60, super_strict_30) that contain small values in comparison to the rest. Therefore we will group all these entries into the 'strict' category.

group_categories('cancellation_policy', 'strict', 200)

#? Now we will treat the 'ammenities' collumn. Since analyzing each amenety would require exxcessive complexity and computing power, we will instead analyze the length of each amenety array (the higher the length the higher the final price will be)

#* creating a new collumn on the main dataframe of the length of each amenety array and removing the original one
main_dataframe["Amount amenities"] = main_dataframe['amenities'].str.split(',').apply(len)
main_dataframe = main_dataframe.drop('amenities', axis = 1)


#* removing outliers
main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, 'Amount amenities')
print(f"{amount_removed_lines} lines were removed from Amount amenities")


#! 8) VISUALIZING THE MAP OF PROPERTIES FROM THE LONGITUDE AND LATITUDE

#? In order to avoid crashes and slowdowns, only the first 70,000 samples will be visualized. 
data = main_dataframe.sample(71000)
center = {'lat':data.latitude.mean(), 'lon':data.longitude.mean()}
map_graph = px.density_mapbox(data, lat='latitude', lon='longitude',z='price', radius=2.5, center=center, zoom=10, mapbox_style='open-street-map')

#? In order to load all of the data into the browser, we will save the map as an html file, then open it in the browser
with open('map.html', 'w', encoding = 'utf-8') as f :
    f.write(map_graph.to_html())

webbrowser.open(os.path.realpath('map.html'))

#! 9) ENCODING TO ALLOW FOR MACHINE LEARNING

"""
We need to adjust some columns to facilitate the machine learning model's analysis.
There are two types of data inside the columns: caregories and True or False
Booleans will become 0 (false) and 1 (true)
Categories will be encoded using dummy encoding (creates columns for each category and applies binary values based if they are in the category or not)
"""

#? First, we will create a copy of the dataframe to not alter the original

main_dataframe_coded = main_dataframe.copy()

#* Encoding booleans
for collumn in ['host_is_superhost', 'instant_bookable', 'is_business_travel_ready'] :
    main_dataframe_coded[collumn] = main_dataframe[collumn].map({'f':0, 't':1})

#* Encoding text columns with dummy encoding
main_dataframe_coded = pd.get_dummies(data = main_dataframe_coded, columns = ['property_type', 'room_type', 'bed_type', 'cancellation_policy'])

#! 10) PREDICTION MODELS

"""
Regression prediction model equation: Y = price, x1 = rooms, x2 = beds, x3 = ameneties, x4 = bathrooms etc
Y = a*x1 + b*x2 + c*x3 + d*x4 ... + z
Computer automatically applies this logic via machine learning

Steps to build a prediction model:

1) Define if it is classification or regression problem
    - Classification: predict the category (non-numerical) -Ex: predict if email is SPAM or not
    - Regression: predict the price (numerical) - Ex: predict house price

2) Choose the metrics to evaluate the model
    - R² (0 to 1, measuring how much of the variation of data the model can explain) or RSME (Root Mean Square Error, says how much the model is off)

3) Choose which models we are going to use
    - Linear Regression - traces a line that minimizes the erros, values closer to the line are better, not efficient with weak/no correlations
    - Random Forest Regressor - Decision trees - doing questions separating the data into different groups, random forest regressor uses multiple decision trees with random smaller parts of the data and calculates the mean to reach the final result
    - Extra Trees - Same and random forest regressor, however the random forest chooses the best question (that will filter the most data) while extra trees asks a random question (which could work beest depending on the question)

4) Train the models and test
    - Randomly separate the data into two sets: training and testing data
    - Training data will be used for the model to know what values to analyze (x variable in the equation will be the properties' features) and what it wants to calculate (y variable in the equation will be the price of the property)
    - Testing data will be used for the model to analyze new data and check its accuracy after it is fully trained
    - To address overfitting, an 80-20 data split strategy is employed, where 80% of the dataset is allocated for training and 20% for testing. This approach ensures rigorous evaluation of the model's generalization ability by assessing its performance on unseen data. By separating datasets for training and testing, the model's tendency to overly adapt to training data nuances is mitigated, thereby enhancing its efficacy in handling new data.

5) Compare the results of the models and choose the best one
    - Choose 1 main metric, such as R², in which the model with the biggest R² will be considered the best model
    - RSME will be used as a tiebreaker when models have very similar R²
    - Time and complexity will also be taken into consideration (less time and less information needed is prefered)

6) Analyse the best model
    - Analyse the importance of each feature (if its not relevant, we can remove it to observe changes in the result)
    - We will perform changes with the goal of improving the R²/RSME, speed, and simplicity of the model

7) Adjust and improve the best model
    - Apply the changes made
"""

#? First we will create a function to evaluate each model. 'prediction' is the prediction made by the model, 'model_name' is the name of the type of the model, and 'y_test' is the true value of the prediction used to compare the results.
def analise_model(prediction, y_test) :
    r2 = r2_score(y_test, prediction)
    rsme = root_mean_squared_error(y_test, prediction)
    print(f"The model has an R² of {r2} and an RSME of {rsme}\n")

#? setting up the y and x variables

y, x = (main_dataframe_coded['price'], main_dataframe_coded.drop('price', axis=1))

#? Splitting the data into training and testing data

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=20)

#? Now we will test the three models mentioned previously

linear_model, random_forest_model, extra_trees_model = (LinearRegression(), RandomForestRegressor(), ExtraTreesRegressor())

models_list = ["Linear Regression", "Random Forest Regressor", "Extra Trees"]

for i, model in enumerate([linear_model, random_forest_model , extra_trees_model]):
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print(models_list[i])
    analise_model(prediction, y_test)

#? After analyzing the results of each model, the Extra Trees model was chosen to be the most effective. 
#? The linear regression model has a very low R² value (32%), and while the Extra Trees and the Random Forest model have very similar R², the Random Forest model has a higher RSME and takes one extra minute to calculate in comparison to the Extra Trees.

#! 11) ANALYZE THE BEST MODEL

#? In order to analyze how the model works, we need to observe the importance of each feature the model uses when calculating the final price.

feature_importance_dict = dict(zip(x_train.columns, extra_trees_model.feature_importances_ ))
sorted_feature_importance_dict = sorted(feature_importance_dict.items(), key=lambda x:x[1])
feature_importance_dict = dict(sorted_feature_importance_dict)

print(feature_importance_dict)

#? After observing the influence of each feature, we can observe the relevance of the localization as the longitude and latitude account for 20% of the data used in the calculations for the price. Also, the amount of ammenities bedrooms are another crucial factors in the price definition as the houses become more attractive to customers, therefore increasing its prices.

#? However, other features such as 'is_buisness_travel_ready' have no relevance when calculating the final price, therefore we will experiment removing them to test if the model becomes more efficient.


#! 12) ADJUSTING AND IMPROVING THE BEST MODEL

#? Due to the large amount of columns present in the model's analysis, we will remove all of the features that have an importance of less than 0.007. This will remove a large amount of redundant data in the model's analysis, making it considerably more efficient.

#? After the removal, there will only be one 'room_type' column (the 'room_type_Entire home/apt'). In order to add more flexibility for the user when choosing a room type, we will keep the 'room_type_Private room' column which had the second highest importance.

room_type_private_room = main_dataframe_coded['room_type_Private room']

for column in feature_importance_dict :
    if feature_importance_dict[column] < 0.007 :
        print(f"Removed {column}")
        main_dataframe_coded = main_dataframe_coded.drop(column, axis=1)

main_dataframe_coded['room_type_Private room'] = room_type_private_room

y, x = (main_dataframe_coded['price'], main_dataframe_coded.drop('price', axis=1))
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=20)

#? We will now create a new final Extra Trees model with the new data and observe its performance.

final_model = ExtraTreesRegressor()

final_model.fit(x_train, y_train)
prediction = final_model.predict(x_test)
analise_model(prediction, y_test)

#? We can see that the model's accuracy barely changed after removing said features, however its efficiency and simplicity has improved significantly (5 minutes to 2 minutes)

feature_importance_dict_final = dict(zip(x_train.columns, final_model.feature_importances_))
sorted_feature_importance_dict = sorted(feature_importance_dict_final.items(), key=lambda x:x[1])
feature_importance_dict_final = dict(sorted_feature_importance_dict)
print(feature_importance_dict_final)

#! 13) DEPLOYMENT

#* 1) Create a file of the model (joblib)
#? We will use the joblib library to save the model in a .joblib file

x["Price"] = y
x.to_csv("final_data.csv")

joblib.dump(final_model, "final_model.joblib")

#* 2) Choose the form to deploy the model (Microsite Flask, direct use Streamlit, .exe file Tkinter)

#? We will chosse Streamlit for deployment as it provides a direct and efficient solution for the deployment of the model

#* 3)  Other python file (Jupyter or PyCharm)

#? We will create a new python file 'airbnb_deploy.py' that will be in the  deployment of the model

