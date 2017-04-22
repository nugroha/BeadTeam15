import time
import datetime
import random
import json
import os
from os.path import expanduser, join
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
#from pyspark.sql import SparkSession
#from pyspark.sql import Row

def create_human(patient_id, health):
    patient_id = patient_id
    base_heartbeat = int(random.uniform(80, 100))
    if (health == "bad" or health == "badtogood"):
        base_systolic_bp = int(random.uniform(130, 160))
        base_diastolic_bp = int(random.uniform(90, 100))
        
    elif (health == "good" or health == "goodtobad"):
        base_systolic_bp = int(random.uniform(100, 120))
        base_diastolic_bp = int(random.uniform(60, 80))
    return list([patient_id, base_heartbeat, base_systolic_bp, base_diastolic_bp, health])

def randomise_data(human,rn1,rn2,rn3):
    result = {}
    result['patient_id'] = human[0]
    result['heartbeat'] = human[1] + rn1
    result['systolic_bp'] = human[2] + rn2
    result['diastolic_bp'] = human[3] + rn3
    result["datestamp"] = str(datetime.datetime.now().date())
    result["timestamp"] = str(datetime.datetime.now().strftime("%H:%M:%S"))
    # add pill box data (open, close) 
    return json.dumps(result)
  
def exporttohdfs(local_path, hdfs_path, result):
    text_file = open(local_path, "w")
    text_file.write(result)
    text_file.close()
    out_str = "hdfs dfs -appendToFile " + local_path + " " + hdfs_path
    os.system(out_str)

	
if __name__ == "__main__":
	# Create a local StreamingContext with two working thread and batch interval of 1 second
	sc = SparkContext(appName="PythonStreamingPaitentData")
	ssc = StreamingContext(sc, 1)
	
	# warehouse_location points to the default location for managed databases and tables
	warehouse_location = 'spark-warehouse'
	
	#spark = SparkSession \
	#	.builder \
        #        .appName("Python Sqark SQL Hive Integration example") \
        #        .config("spark.sql.warehouse.dir", warehouse_location) \
        #        .enableHiveSupport() \

	iteration=0
	a=b=c=0
	end_result = []
	while iteration < 1000:
		if iteration == 0:
			human1 = create_human("73557","goodtobad")
			human2 = create_human("73558","badtogood")
			human3 = create_human("73559","good")
			human4 = create_human("73560","good")
			human5 = create_human("73561","bad")
			
		if human1[4] == "goodtobad" and iteration >= 200 and rn_temp%5 == 0:
			human1[2] = min(150,human1[2] + 1)
			human1[3] = min(110,human1[3] + 1)
		if human2[4] == "badtogood" and iteration >= 300 and rn_temp%5 == 0:
			human2[2] = max(90, human2[2] - 1)
			human2[3] = max(50, human2[3] - 1)   

		rn_temp = round(random.uniform(1, 10))
		if rn_temp%2 == 0:
			a = round(random.uniform(1, 10))
		elif rn_temp%5 == 0:
			b = round(random.uniform(1, 10))
			c = round(random.uniform(1, 10))
		
		end_result.append(randomise_data(human1[0:4],a,b,c))
		end_result.append(randomise_data(human2[0:4],a,b,c))
		end_result.append(randomise_data(human3[0:4],a,b,c))
		end_result.append(randomise_data(human4[0:4],a,b,c))
		end_result.append(randomise_data(human5[0:4],a,b,c))

		if iteration%10 == 0 and iteration != 0:
			end_result1 = ', '.join(end_result)
			patientRecordRDD = sc.parallelize(end_result1)
			patientRecord = spark.read.json(patientRecordRDD)
			patientRecord.show()
			# Use an RDD[String] to store the created stream JSON.
			##exporttohdfs("/home/training/output.txt", "/loudacre/output.txt", end_result1)	
			#ssc.textFileStream(end_result1)
			#ssc.saveAsTextFiles('out.txt')
			end_result = []
		time.sleep(2)
		iteration = iteration+1
	
	ssc.start()
    	ssc.awaitTermination()
