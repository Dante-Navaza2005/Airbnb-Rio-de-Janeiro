# Calculating limits

We will create a function called 'calculate_limits' that will recieve a collumn from the main_dataframe as a parameter and it will return to us the outliers below the first quartile and those above the third quartile as mentioned in the [second step of how to locate outliers](README.md)

```python
def calculate_limits(collumn) :
    q1 = collumn.quantile(0.25)
    q3 = collumn.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr

# print(calculate_limits(main_dataframe['price']))
```
