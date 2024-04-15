# Outlier Function

Now we will create the 'exclude_outliers' function, that will recieve the main dataframe and the collumn that it will remove the outliers from. Usally, outliers above the upper limit represent luxury properties, which are not considered for the prediction model who's objective is to analyze common apparments, and thus should be removed.

```python
def exclude_outliers(main_df, collumn) :
    amount_lines = main_df.shape[0]
    lower_limit, upper_limit = calculate_limits(main_df[collumn])
    main_df = main_df.loc[(main_df[collumn] >= lower_limit) & (main_df[collumn] <= upper_limit), :]
    return main_df, amount_lines - main_df.shape[0]
```

In this code the use of the .loc function  with the condition `[(main_df[column] >= lower_limit) & (main_df[column] <= upper_limit)]`  inside constructs a boolean array that selects rows where the values in the specified column (`column`) are greater than or equal to `lower_limit` AND less than or equal to `upper_limit`.

So, essentially, this line filters the DataFrame `main_df` to include only the rows where the values in the specified column (`column`) fall within the range defined by `lower_limit` and `upper_limit`.
