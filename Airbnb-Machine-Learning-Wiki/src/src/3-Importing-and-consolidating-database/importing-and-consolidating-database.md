# Importing and consolidating the database

The dataset comprises 25 databases stored in separate tables. To facilitate data processing and facilitate machine analysis, a consolidated database termed "main_dataframe" was created by integrating all these databases. This integration process involved the utilization of the Python pandas library, wherein each database, stored as a CSV file, was imported individually and appended to an initially empty list named "df_list". Subsequently, the pandas function pd.concat() was employed to concatenate all individual dataframes into a singular cohesive dataset.

Furthermore, each dataframe within the main_dataframe contains a column representing dates. However, the dates are inconsistently formatted strings. To address this inconsistency, an extraction process was implemented to isolate the month and year components from the dataframe names. These extracted components were then utilized to create corresponding columns within the main_dataframe, thus ensuring consistency and facilitating further analytical operations.



```python
dataset_folder = pathlib.Path('dataset')
months = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
df_list = []


#* concatenating all the databases into one while adding the month and year columns
for file in dataset_folder.iterdir() :
    month = months[file.name[:3]]

    year = int(file.name[-8:].replace('.csv', ''))

    df = pd.read_csv(file)
    df['month'] = month  
    df['year'] = year

    df_list.append(df)

main_dataframe = pd.concat(df_list)
```
