from pyspark.sql.functions import *

df = df.withColumn(
    "InvoiceDate",
    to_timestamp("InvoiceDate", "dd-MM-yyyy HH:mm")
)

df = df.withColumn("Year", year("InvoiceDate")) \
       .withColumn("Month", month("InvoiceDate")) \
       .withColumn("Day", dayofmonth("InvoiceDate")) \
       .withColumn("Hour", hour("InvoiceDate"))
