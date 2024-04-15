# Removing outliers from the 'price' and 'extra_people' columns

The first outliers to be removed will be from the 'price' and 'extra_people' collumns as they have the highest relevance in calculating the final price and they are continues numerical values (can be measured). 

```python
for collumn in ['price', 'extra_people'] :
    main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, collumn)

    print(f"{amount_removed_lines} lines were removed from {collumn}")
    ###histogram(main_dataframe[collumn])
    ###box_plot(main_dataframe[collumn])
```

![1712967427666](image/README/1712967427666.png)

Nearly 10% of the lines were removed from the 'price' column

Obs: when the price collumn is a integer, the quantity of apparments increases because landlords usally put their price as a whole value.
