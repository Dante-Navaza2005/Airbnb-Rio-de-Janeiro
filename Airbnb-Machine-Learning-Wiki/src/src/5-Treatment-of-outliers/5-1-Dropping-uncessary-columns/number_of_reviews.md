# Removing the 'number_of_reviews' column

The 'number_of_reviews' column will be disregarded from the model's analysis as its goal is to analyze the price for normal users and landlords, which in most cases won't have reviews or a large number of them. Also simpler models are faster and less prone to overfitting.

```python
main_dataframe = main_dataframe.drop('number_of_reviews', axis = 1)
```
