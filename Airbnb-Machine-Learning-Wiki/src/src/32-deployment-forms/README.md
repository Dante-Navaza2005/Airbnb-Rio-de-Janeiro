# Deployment forms

There are various ways to deploy a machine learning project such as:

* Host it on a website utilizing django/flask
* Transform it into a app with Tkinter
* Convert the project into a .exe file
* Deploying it with Streamlit

In this project, we're opting to deploy the machine learning model through a Streamlit-based web application, which will be accessible via a standalone executable (.exe) file. This deployment method was selected because the model's size is substantial, leading to hosting constraints on many platforms. Given the file size limitations imposed by various hosting providers, deploying through an executable Streamlit application offers a practical solution for accommodating large-scale machine learning models.
