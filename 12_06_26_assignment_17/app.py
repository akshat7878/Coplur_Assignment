from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc

spark = SparkSession.builder.appName("SalesDataFrameAnalysis").getOrCreate()

# Read CSV
df = spark.read.csv("sales.csv", header = True, inferSchema = True)

print("\nsort all products by sales in descending order")

sorted_products = df.orderBy(desc("sales"))
sorted_products.show()

print("\ndisplay the top 3 products with the highest sales values")

top_3 = df.orderBy(desc("sales")).limit(3)
top_3.show()

print("\nfilter products with sales greater than 80,000 and save the output as a CSV file")

high_sales = df.filter(col("sales") > 80000)
high_sales.show()

# Save output
high_sales.write.mode("overwrite").csv("output/high_sales_products", header= True)

spark.stop()