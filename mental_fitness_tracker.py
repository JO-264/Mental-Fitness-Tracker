# -*- coding: utf-8 -*-
"""Mental Fitness Tracker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LAqBEKp5rOWpcCaiqb4OgyyAU-OGT7yM

# **AI Mental Fitness Tracker**

*   This notebook deals with the 'Mental Fitness' using different Machine Learning Algorithms

# About the Data

*   Data Overview: This is a 'Mental Health' . csv data

# Import required libraries
"""

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

from google.colab import drive

drive.mount('/content/drive')

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

"""# Exploratory Data Analysis

Load and Prepare Data
"""

df1 = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Mental Fitness/prevalence-by-mental-and-substance-use-disorder _AI.csv")

df2 = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Mental Fitness/mental-and-substance-use-as-share-of-disease -AI.csv")

df1.head()

df2.head(10)

data = pd.merge(df1,df2)
data.head(10)

"""Data Cleaning"""

data.isnull().sum()

data.drop('Code',axis = 1 , inplace = True)

data.head(10)

data.size,data.shape

data.set_axis(['Country','Year','Schizophrenia','Bipolar_disorder','Eating_disorder','Anxiety','drug_usage','depression','alcohol','mental_fitness'],axis = 'columns',inplace = True)

data.head()

"""Visualiation"""

plt.figure(figsize=(12,6))
sns.heatmap(data.corr(),annot = True,cmap = 'Blues')
plt.plot()

"""Takeaway Points:


*   Eating_disorder is positively correlated to mental_fitness and vice-versa as our eating choice affect our mental health


"""

sns.pairplot(data,corner=True)
plt.show()

mean = data['mental_fitness'].mean()
mean

fig = px.pie(data,values = 'mental_fitness',names = 'Year')
fig.show()

fig = px.line(data,x="Year",y="mental_fitness",color = 'Country',markers = True,color_discrete_sequence=['red','blue'],template='plotly_dark')
fig.show()

df = data
df.head(10)

df.info()

from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
for i in df.columns:
  if df[i].dtype == 'object':
    df[i]=l.fit_transform(df[i])

df.shape

"""# Spilt Data - (6840,10)"""

x = df.drop('mental_fitness',axis=1)
y = df['mental_fitness']

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = .20 , random_state = 2)

#Training (6840,10)
#6840*80/100 = 5472
#6840*20/100 = 1368
print("xtrain : ",xtrain.shape)
print("xtest : ",xtest.shape)
print("\n")
print("ytrain : ",ytrain.shape)
print("ytest : ",ytest.shape)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
lr = LinearRegression()
lr.fit(xtrain,ytrain)

ytrain_pred = lr.predict(xtrain)
mse = mean_squared_error(ytrain,ytrain_pred)
rmse = (np.sqrt(mse))
r2 = r2_score(ytrain , ytrain_pred)

print("The Linear Regression model performance for training set")
print("--------------------------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(xtrain,ytrain)

ytrain_pred = rf.predict(xtrain)
mse = mean_squared_error(ytrain,ytrain_pred)
rmse = (np.sqrt(mse))
r2 = r2_score(ytrain,ytrain_pred)

print("The Linear Regression model performance for training set")
print("--------------------------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

"""# Evaluation

*   In this part, we will compare the scores of the above two models

"""

#linear Regression model evaluation for testing set
ytest_pred = lr.predict(xtest)
mse = mean_squared_error(ytest,ytest_pred)
rmse = (np.sqrt(mse))
r2 = r2_score(ytest,ytest_pred)

print("The Linear Regression model performance for training set")
print("--------------------------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

#Random Forest Regression model evaluation for testing set
ytest_pred = rf.predict(xtest)
mse = mean_squared_error(ytest,ytest_pred)
rmse = (np.sqrt(mse))
r2 = r2_score(ytest,ytest_pred)

print("The Linear Regression model performance for training set")
print("--------------------------------------------------------")
print('MSE is {}'.format(mse))
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))