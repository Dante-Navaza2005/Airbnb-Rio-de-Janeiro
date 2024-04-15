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
  * [Outlier function](src\6-Outlier-function\README.md)
  * [Removing outliers from the &#39;price&#39; and &#39;extra_people&#39; columns](src\7-Removing-outliers-price-extra-people\README.md)
  * [Removing outliers of discrete numerical columns](src\8-outliers-discrete-numerical-columns\README.md)
* [Treating non numerical values](src\9-Treating-non-numerical-values\README.md)

  * [Group_categories function](src\10-Group_categories-function\README.md)
    * [group property_type](src\10-Group_categories-function\10-1-group-property_type\README.md)
    * [group bed_type](src\10-Group_categories-function\10-2-group-bed_type\README.md)
    * [group cancellation_policy](src\10-Group_categories-function\10-3-group-cancellation-policy\README.md)
    * [group room_type](src\10-Group_categories-function\10-4-group-room_type\README.md)
  * [Treating &#39;ammenities&#39; collumn](src\11-Treating-ammenities-collumn\README.md)

---

# Visualizing map

* [Reducing visualized data](src\12-reducing-visualized-data\README.md)
* [Loading the map into the browser](src\13-loading-map-to-browser\README.md)

---

# Encoding

* [Encoding explanation](src\14-Encoding-explanation\README.md)
* [Encoding booleans](src\15-Encoding-booleans\README.md)
* [Encoding text columns (dummy encoding)](src\16-dummy-encoding\README.md)

---

# Prediction models

* [7 steps to build a prediction model](src\17-steps-to-build-model\README.md)
  * [Defining if it is classification or regression problem](src\18-define-classification-regression-problem\README.md)
  * [Choosing the metrics to evaluate the model](src\19-Choosing-evaluation-metrics\README.md)
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