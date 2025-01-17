# -*- coding: utf-8 -*-
"""Hill and Valley Prediction using Logistics Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12UXsxau9HHFcMV2QiTsayhLqmrdw-dDH

# **Hill and Valley Prediction using Logistics Regression**

## **Get Understanding about Data set**


> Each record represent 100 points on a two- dimentional graph. When plotted in order (from 1 through 100) as the Y coordinate, the points will create either a Hill(a "bump" in the terrain) or a Valley (a "dip" in the terrain). See the original source for some examples of these graphs


> **1-100**: Labeled "V##". Floating point values(numeric), the X-values.


> **101**: Labeled "Class". Binary(0,1) representing {valley,hill}

-------------

## **Import Library**
"""

import pandas as pd

import numpy as np

"""## **Import Data**"""

df=pd.read_csv(r'/content/Hill Valley Dataset.csv')

"""## **Describe Data**









"""

df

"""### **First Five Rows of Dataframe**"""

df.head()

"""### **Last Five Rows of Dataframe**"""

df.tail()

"""### **Dimensions of the DataFrame**"""

df.shape

"""### **Information about the DataFrame**"""

df.info()

"""### **Summary Statistics**"""

df.describe()

"""### **Get Column Names**"""

df.columns

"""##### *All columns name not printed*"""

print(df.columns.tolist())

"""### **Get Unique Values (Class or Label) in y Variable**"""

df['Class'].value_counts()

df.groupby('Class').mean()

"""## **Define Target Variable (y) and Feature Variables (X)**"""

y=df['Class']

y.shape

X = df.drop('Class', axis=1)

X.shape

X

"""## **Get Plot of First Two Rows**"""

import matplotlib.pyplot as plt

plt.plot(X.iloc[0,:])
plt.title('Valley');

plt.plot(X.iloc[1,:])
plt.title('Hill');

"""## **Get X Variables Standardized**



> Standardization of dataset is a common requirement for many machine learning estimators implemented in scilit-learn; they might behave badly if the individual features do not more or less look like standard normally distributed data; Gaussian with zero mean and unit variance.


> Next approach is go for MiniMax Scaler



"""

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X=ss.fit_transform(X)

X

X.shape

"""## **Get Train Test Split**"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, stratify=y, random_state=2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""## **Get Model Train**"""

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train, y_train)

"""## **Get Model Prediction**"""

y_pred = lr.predict(X_test)

y_pred.shape

y_pred

"""## **Get Probability of Each Predicted Class**"""

lr.predict_log_proba(X_test)

"""## **Get Model Evaluation**"""

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

"""## **Get Future Predictions**


> Let's select a random sample from existing dataset as new value


> Steps to follow


1. Extract a random row using sample function
2. Separate X and y
3. Standardize X
4. Predict







"""

X_new = df.sample(1)

X_new

X_new.shape

X_new = X_new.drop('Class', axis=1)

X_new

X_new.shape

X_new = ss.fit_transform(X_new)

y_pred_new = lr.predict(X_new)

y_pred_new

lr.predict_proba(X_new)

