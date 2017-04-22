spark-shell --packages com.databricks:spark-csv_2.11:1.5.0
import org.apache.spark.sql.SQLContext
val sqlContext = new SQLContext(sc)

val data = sqlContext.read.load('file:/home/training/training_materials/data/final_data3.csv',format='com.databricks.spark.csv',header='true',inferSchema='true')

from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.regression import LinearRegression

data = data.dropna()

data = data.select("Risk of heart diseases", "Smoker", "Alcoholic", "Diabetes", "Sleep", "DiastolicBP2", "BMI", "Gender", "Max heart rate").map(lambda r: LabeledPoint(r[0], [r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]])).toDF()
display(data)

lr = LinearRegression()

modelA = lr.fit(data, {lr.regParam:0.0})

predictionsA = modelA.transform(data)
display(predictionsA)

