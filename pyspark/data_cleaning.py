from pyspark.sql.functions import *

df = spark.read.csv(
    "/Volumes/retaildatabricks/retail/raw_data/Online Retail.csv",
    header=True,
    inferSchema=True
)

df = df.dropDuplicates()

df = df.withColumn(
    "Revenue",
    col("Quantity") * col("UnitPrice")
)
