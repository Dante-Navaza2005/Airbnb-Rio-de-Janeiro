# 7 steps to build a prediction model

Firstly, it is necessary to comprehend the details of machine learning and its predictive modeling mechanics. As delineated in the introduction, our selection entails the utilization of a supervised learning model. Yet, within this domain resides a myriad of machine learning models, each distinguished by diverse techniques and methodologies for varied task execution, such as regression and classification.

Regression models are used in tasks that require a large numerical analysis that requires the prediction of a continuous numerical value, for example, the price of a household. Each model utilizes a unique regression technique such as the Linear Regression that works by fitting a straight line to a set of data points in such a way that the errors between the observed and predicted values are minimized.

It utilizes the equation **Y = a * x1 + b *x 2 + c * x3 + d * x4 ... + z** where

* **Y** is the predicted price of the house.
* **x1,x2,x3**… are the independent variables (number of rooms, number of bathrooms, size of the lot, etc.).
* **a,b,c,d..** are the coefficients representing the impact of each independent variable on the predicted price.
* **z** is the intercept term.

During the training process, the model learns the values of the coefficients **(a,b,c,d...)** that minimize the errors between the predicted and actual prices in the training data. These coefficients capture the relationships between the independent variables and the dependent variable **Y**, allowing you to analyze the impact of various factors on the price of the house.

This linear regression model is one of the three models that were analyzed, with the other two being the Random Forest Regressor and Extra Trees (these three especifically were selected due to their wide use and effectivness in most cases), which will be explained in the third section (selection).

Then there are other models which are revolved around solving classification problems that require a prediction of a discrete category or class label. A example of this would be a model that predicts if a email is SPAM or not. It uses algorithms to categorize input data into one or more discrete classes or categories.

The construction of a prediction model is sperated into seven steps that we will follow:

1. Define if it is classification or regression problem
2. Choose the metrics to evaluate the model
3. Choose which models we are going to use
4. Train the models and test
5. Compare the results of the models and choose the best one
6. Analyse the best model
7. Adjust and improve the best model
