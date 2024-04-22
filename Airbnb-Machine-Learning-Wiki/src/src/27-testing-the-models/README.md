# Testing the three models

Now we will **train** and **test** each of the three models:

1. Linear Regression
2. Random Forest Regressor
3. Extra Trees

```python
#? Now we will test the three models mentioned previously

linear_model, random_forest_model, extra_trees_model = (LinearRegression(), RandomForestRegressor(), ExtraTreesRegressor())

models_list = ["Linear Regression", "Random Forest Regressor", "Extra Trees"]

for i, model in enumerate([linear_model, random_forest_model , extra_trees_model]):
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    print(models_list[i])
    analyze_model(prediction, y_test)
```

The results of each model are shown below:

![1713737881970](image/README/1713737881970.png)
