# Exporting model as joblib

First we will export the model itself using the joblib library to save it inside a .joblib file. We will add the "price" collumn as we had previously removed it during the training process. The joblib file requires the x values as well as the y values.

```python
x["Price"] = y
x.to_csv("final_data.csv")

joblib.dump(final_model, "final_model.joblib", compress = 3)
```


**Obs:** We added a compress level of 3 inside the joblib.dump parameters in order to reduce the size of the file from approximadetly **2 GB** down to **400 MB**, however, the model gets **slower** each time the **compress level increases**.
