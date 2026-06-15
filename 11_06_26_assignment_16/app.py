from pyspark.sql import SparkSession
from pyspark.sql.functions import  desc,  sum

spark = SparkSession.builder.appName("EmployeeRDDAnalysis").getOrCreate()

rdd = spark.read.csv("employee.csv", header = True, inferSchema = True)

#sort all employees by salary in descending order and display the results on the console
sorted_emp = rdd.orderBy(desc("salary"))
sorted_emp.show()

#calculate the total salary paid in each department and print the department-wise totals
dept_agg_salary = rdd.groupBy("department").agg(sum("salary").alias("Total_Salary"))
dept_agg_salary.show()

#identify the top three highest-paid employees and save the output to a file
top_3_highest_paid = rdd.orderBy(desc("salary")).limit(3)
top_3_highest_paid.show()

top_3_highest_paid.write.mode("overwrite").csv("output/top_emp.csv", header=True)