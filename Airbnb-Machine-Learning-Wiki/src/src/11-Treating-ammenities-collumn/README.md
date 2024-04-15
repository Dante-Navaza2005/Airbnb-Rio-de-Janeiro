# Treating 'amenities' collumn

Now we will treat the 'amenities' collumn. Since analyzing each amenity would require excessive complexity and computing power, we will instead analyze the length of each amenity array (the higher the length the higher the final price will be)

The code below creates a new collumn on the main dataframe consisting of the length of each amenity array and removes the original  collumn containing the lists.

```python
main_dataframe["Amount amenities"] = main_dataframe['amenities'].str.split(',').apply(len)
main_dataframe = main_dataframe.drop('amenities', axis = 1)
```

Now we will remove the outliers:

```python
#* removing outliers
main_dataframe, amount_removed_lines = exclude_outliers(main_dataframe, 'Amount amenities')
print(f"{amount_removed_lines} lines were removed from Amount amenities")
```
