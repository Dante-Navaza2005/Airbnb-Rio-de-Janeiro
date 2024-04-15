# Removing outliers of discrete numerical columns

Now we will undergo the same procedure removing the outliers of the discrete numerical columns:

```python
for collumn in ['host_listings_count','accommodates', 'bathrooms', 'beds','bedrooms', 'minimum_nights'] :
    main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, collumn)
    print(f"{amount_removed_lines} lines were removed from {collumn}")
    ###box_plot(main_dataframe[collumn])
    ###bar_graph(main_dataframe[collumn])
```
