from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PartitionDemo").getOrCreate()

df = spark.range(5000000)

print("Initial Partitions:", df.rdd.getNumPartitions())

df_repartitioned = df.repartition(12)
print("After Repartition(12):", df_repartitioned.rdd.getNumPartitions())

df_coalesced = df_repartitioned.coalesce(3)
print("After Coalesce(3):", df_coalesced.rdd.getNumPartitions())

spark.stop()