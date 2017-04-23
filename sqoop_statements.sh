/*  This program will extract patient data from mysql database and ingest into HDFS
*   and converted to HIVE.
*   
*   History:
*/

#####################
# data ingestion from mysql via Sqoop into hdfs
# do be used by Spark or other tools to perform further ETL or apps.
#####################
sqoop import --connect jdbc:mysql://ussclpddbmgp001.autodesk.com:3306/db --username beaduser --password beaduser --query 'SELECT q.SEQN, q.SMD460 as SmokerH, q.SMQ040 as Smoker, q.ALQ101 as Alcoholic, q.DIQ010 as Diabetes, q.SLD010H as Sleep, e.BPXSY1 as SystolicBP1, e.BPXDI1 as DiastolicBP1, e.BPXSY2 as SystolicBP2, e.BPXDI2 as DiastolicBP2, e.BPXDI3 as SystolicBP3, e.BPXDI3 as DiastolicBP3, e.BMXWT as Weight, e.BMXHT as Height, e.BMXBMI as BMI, d.RIAGENDR as Gender, d.RIDAGEYR as Age, d.INDFMPIR as IncomePoverty FROM Demographic d LEFT JOIN Diet dt on d.SEQN = dt.SEQN LEFT JOIN Examination e on  d.SEQN = e.SEQN LEFT JOIN Labs l on d.SEQN = l.SEQN LEFT JOIN Questionnaire q on d.SEQN = q.SEQN where $CONDITION' --split-by q.SEQN --target-dir /user/beadteam15/beaddata

#####################
# data ingestion from mysql via sqoop into hive. (also stored into hdfs)
# do allow querying of dataset through HIVE GUI and easy pulling of records to perform data exploration on dashboard(eg. Tableau)
#####################
sqoop import --connect jdbc:mysql://ussclpddbmgp001.autodesk.com:3306/beaddata --username beaduser --password beaduser --query 'SELECT SEQN as SEQN, MAXHR as MaxHeartRate, RISKHD as HeartDiseaseRisk FROM Scores where $CONDITIONS' --split-by SEQN --target-dir /user/beadteam15/beaddata-score-hive --hive-import --hive-table beaddata.score
