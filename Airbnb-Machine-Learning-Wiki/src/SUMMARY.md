# Summary

# Explanation

---

- [Introduction](src\1-Introduction\README.md)
  - [Context and objective](src\1-Introduction\objective.md)

---

# Getting Started

* [Importing and installing libraries](src\2-Importing-and-installing-libraries\README.md)
* [Importing and the consolidating databse](src\3-Importing-and-consolidating-database\importing-and-consolidating-database.md)

---

# Treating database

* [Steps underwent in treating the data](src\4-Reduce-excessive-columns\README.MD)

  * [Reducing excessive amount of columns](src\4-Reduce-excessive-columns\reduce-excessive-collumns.md)
  * [Treating missing values](src\4-Reduce-excessive-columns\treating-missing-values.md)
  * [Verifying data types of each collumn](src\4-Reduce-excessive-columns\verify-data-types.md)
* [Treatment of outliers](src\5-Treatment-of-outliers\README.md)

  * [Analyzing heatmap](src\5-Treatment-of-outliers\analyzing-heatmap.md)
  * [Calculating limits](src\5-Treatment-of-outliers\calculating-limits.md)
  * [Creating graphs](src\5-Treatment-of-outliers\creating-graphs.md)
  * [Dropping unecessary columns](src\5-Treatment-of-outliers\5-1-Dropping-uncessary-columns\README.md)
    * [&#39;guests_included&#39;](src\5-Treatment-of-outliers\5-1-Dropping-uncessary-columns\guests_included.md)
    * [&#39;number_of_reviews&#39;](src\5-Treatment-of-outliers\5-1-Dropping-uncessary-columns\number_of_reviews.md)
    * [&#39;maximum_nights&#39;](src\5-Treatment-of-outliers\5-1-Dropping-uncessary-columns\maximum_nights.md)
  * Outlier function
  * Removing outliers from the 'price' and 'extra_people' columns
  * Removing outliers of discrete numerical columns
* Treating non numerical values

  * Group_categories function
    * group 'property_type'
    * group 'bed_type'
    * group 'cancellation_policty'
  * Treating 'ammenities' collumn

---

# Visualizing map

* Reducing visualized data
* Loading it into the browser

---

# Encoding

* Explanation
* Encoding booleans
* Encoding text columns (dummy encoding)

---

# Prediction models

* 7 steps to build a prediction model
  * Define if it is classification or regression problem
  * Choose the metrics to evaluate the model
  * Choose which models we are going to use
  * Train the models and test
  * Compare the results of the models and choose the best one
  * Analyse the best model
  * Adjust and improve the best model
* Analise model function
* Splitting the data
* Testing the three models

---

# Final model

* Analyzing the best model
* Adjusting an improving the best model
* Applying the final changes

---

# Deployment (streamlit)

* Deployment forms
* Exporting model as joblib
* airbnb_deploy file
  * Importing streamlit and creating the buttons
  * Dummy variable buttons
* Attributing the values as inputs
* Creating the preview value button
* Finalizing
