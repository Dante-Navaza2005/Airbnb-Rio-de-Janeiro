# Splitting the data

Now, we will randomly split the 80% of the data into **training data** and 20% into **testing data**

* **y** variables will be the 'price' collumn
* **x** variables will be the features of each property

```python
#? setting up the y and x variables

y, x = (main_dataframe_coded['price'], main_dataframe_coded.drop('price', axis=1))

#? Splitting the data into training and testing data

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=20)
```
