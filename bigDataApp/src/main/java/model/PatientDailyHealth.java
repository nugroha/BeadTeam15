package model;

import java.io.Serializable;

public class PatientDailyHealth implements Serializable{
	private String patientId;
	private int diastolicBP;
	private int systolicBP;
	private double heartRate;
	
	public String getPatientId(){
		return patientId;
	}
	
	public void setPatientId(){
		this.patientId = patientId;
	}
	
	public int getDiastolicBP(){
		return diastolicBP;
	}
	
	public void setDiastolicBP(){
		this.diastolicBP = diastolicBP;
	}
	
	public int getSystolicBP(){
		return systolicBP;
	}
	
	public void setSystolicBP(){
		this.systolicBP = systolicBP;
	}

	public double getHeartRate(){
		return heartRate;
	}
	
	public void setHeartRate(){
		this.heartRate = heartRate;
	}
}
