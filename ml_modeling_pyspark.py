"""
This program retrieve data from hdfs and perform prediction on the probability of the "Risk of heart diseases"
using OLS Regression.

Version 2: trying out with pyspark Machine learning API.

"""
spark-shell --packages com.databricks:spark-csv_2.11:1.5.0
import org.apache.spark.sql.SQLContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.regression import LinearRegression


#=============
# Main
#=======================

#Start of sql context
val sqlContext = new SQLContext(sc)

#Retrieve data from hdfs
val data = sqlContext.read.load('file:/home/training/training_materials/data/final_data3.csv',format='com.databricks.spark.csv',header='true',inferSchema='true')

#Data cleasning and feature selection
data = data.dropna()
data = data.select("Risk of heart diseases", "Smoker", "Alcoholic", "Diabetes", "Sleep", "DiastolicBP2", "BMI", "Gender", "Max heart rate").map(lambda r: LabeledPoint(r[0], [r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]])).toDF()
display(data)

#Creating model on Linear Regression.
lr = LinearRegression()
modelA = lr.fit(data, {lr.regParam:0.0})

#Prediction on the result.
predictionsA = modelA.transform(data)
display(predictionsA)

