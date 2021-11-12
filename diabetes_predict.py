# -*- coding: utf-8 -*-
"""diabetes_predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C8eJAS2IdZ3InVrfymc5d3A_-6KvVRZ1
"""

from google.colab import drive

import pandas as pd

drive.mount('/content/gdrive')

df = pd.read_csv('/content/gdrive/My Drive/diabetes.csv')

df

df.head()

#Feature Selection
x = df.drop(columns='Outcome')
x

#target-set
y = df['Outcome']
y

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)    #train data set - 80% and test-dataset - 20%

model = DecisionTreeClassifier()
model.fit(x_train,y_train)          #Training Decision tree

#Prediction of test-data set
y_prediction = model.predict(x_test)
y_prediction

#checking for Accuracy
#Compare test value and predicted value
accuracy = accuracy_score(y_test,y_prediction)
accuracy

print("Accuracy Of Model : ",100*accuracy)

#Predict For Given Input

p = input("Enter Pregnancies Period")
g = input("Enter Glucose Levels")
b = input("Enter BP:")
s = input("Enter Skin Thickness")
i = input("Enter Insulin")
bmi = input("Enter BMI")
db = input("Enter Pedigree")
age = input("Enter Age")

pred = model.predict([[p,g,b,s,i,bmi,db,age]])
if pred[0] == 0:
  print("No Risk")
else:
  print("Diabetes Patient")

