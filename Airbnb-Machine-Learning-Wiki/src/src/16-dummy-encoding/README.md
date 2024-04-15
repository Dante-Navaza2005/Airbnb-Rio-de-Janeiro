# Encoding text columns (dummy encoding)

After  having encoded the boolean columns, all that is left is to convert the text column via dummy encoding.

```python
#* Encoding text columns with dummy encoding
main_dataframe_coded = pd.get_dummies(data = main_dataframe_coded, columns = ['property_type', 'room_type', 'bed_type', 'cancellation_policy'])
```
