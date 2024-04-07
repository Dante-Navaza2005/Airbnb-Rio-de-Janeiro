# Removing the 'maximum_nights' column

The 'maximum_nights' column will also be diregarded from the model's analysis as not only it doesn't contribute signficiantly to a variation in the price, but also a large amount of the data is in the collumn 0, which represents that most users didn't fill out this area when searching for a residence.

```python
main_dataframe = main_dataframe.drop('maximum_nights', axis = 1)
```
