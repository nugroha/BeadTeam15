# -*- coding: utf-8 -*-
"""
This program retrieve data from hdfs and perform prediction on the probability of the "Risk of heart diseases"
using OLS Regression.

Created on Fri Apr 21 20:59:42 2017

@author: ongby
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import sklearn

#=========================
# Main
#=========================
data = pd.read_csv("C:\Users\Andy\Google Drive\School\EB5001 Big Data Engineering for Analytics\Project 2\Datasets\final_data3.csv")

data = data.fillna(0)
A = data.columns
A =  A.drop("Risk of heart diseases")
A =  A.drop("SEQN")
X = data[A]
y = data["Risk of heart diseases"]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

mod = sm.OLS(y_train,X_train)

results = mod.fit()
print(results.summary())

sm.add_constant(X_test)


