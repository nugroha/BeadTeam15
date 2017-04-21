package bigDataApp;

import java.io.Serializable;

import model.PatientDailyHealth;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.*;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.MapFunction;

public class SparkSavePatientDailyRecord implements Serializable {
	
	private static final String MYSQL_USERNAME = "ehrAdmin";
	private static final String MYSQL_PASSWORD = "admin2017";
	private static final String MYSQL_CONNECTION_URL = 
			"jdbc:mysql://192.168.112.129:3306/EHRDB?user="+MYSQL_USERNAME+"&password="+MYSQL_PASSWORD;
	
	private static final JavaSparkContext sc = new JavaSparkContext(new SparkConf().setAppName("SparkSavePatientDailyToDb").setMaster("local[*]"));
	
	
	public static void main(String[] args){
		PatientDailyHealth patientHealth = new PatientDailyHealth();
		//You can set the data for testing here.
		
		JavaRDD<PatientDailyHealth> patientHealthRDD =
	}
}
