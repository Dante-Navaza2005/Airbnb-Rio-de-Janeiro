# Group_categories function

First, we will create a function to group specific categories of a given collumn in case said collumn contains a significant amount of categories with small values (value determined by the 'amount' parameter)

```python
def group_categories(collumn, grouped_category_name, amount) :
    series_category = main_dataframe[collumn].value_counts()

    for category_type in series_category.index :
        if series_category[category_type] < amount :
            main_dataframe.loc[main_dataframe[collumn] == category_type, collumn] = grouped_category_name
```

The main filter occurs in the for loop that iterates throught each different category inside a column and if the amount of values of said categories is smaller than the specified amount passed on the parameters, they will all be grouped into a new category, 'grouped_category_name' whose name is also passed as a parameter of the function.
