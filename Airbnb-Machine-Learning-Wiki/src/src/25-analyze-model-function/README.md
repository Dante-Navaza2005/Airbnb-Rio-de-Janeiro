# 'analyze_model' function

Now we will implement all the steps mentioned previously on our code. 

First we will create a function to evaluate each model. The parameter 'prediction' is the prediction made by the model  and 'y_test' is the true value of the price used to compare the results.

```python
def analyze_model(prediction, y_test) :
    r2 = r2_score(y_test, prediction)
    rsme = root_mean_squared_error(y_test, prediction)
    print(f"The model has an R² of {r2} and an RSME of {rsme}\n")
```
