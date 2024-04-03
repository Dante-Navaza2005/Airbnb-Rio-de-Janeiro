# Reducing excessive amount of columns

As there are a lot of columns, we are going to reduce the amount of columns to enhance the algorithm efficiency.

Furthermore, a rapid analysis of the data shows a significant number of redundant columns in the data for the prediction model, leading to the removal of the following columns:

1. Any collumn with unecessary data types that wont influence the final price such as images, verification methods, etc.
2. ID: these quantitative values are unnecessary and could interfere with the final results as they would also be calculated.
3. Repeated columns: the data contains many columns that are repeated or very similar to each other, such as the date, state, and country.
4. Any collumn that contains hyperlinks or free-form text: besides of not containing relevant data for the desired result, it could interfere with the prediction model.
5. If over 30% of the data is missing we will remove that collumn

After this analisis we were left with the following collumns:

```python
filtered_columns = ['host_response_time','host_response_rate','host_is_superhost','host_listings_count','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','price','security_deposit','cleaning_fee','guests_included','extra_people','minimum_nights','maximum_nights','number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','instant_bookable','is_business_travel_ready','cancellation_policy','year','month']

main_dataframe = main_dataframe.loc[:, filtered_columns]
```

A excel file with the first 900 rows was generated in order to do a quick analysis of the data.

```python
main_dataframe.head(900).to_csv('first_900_rows.csv', sep=';', index=False)
```
