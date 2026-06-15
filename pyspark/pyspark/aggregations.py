from pyspark.sql.functions import *

monthly_sales = df.groupBy(
    "Year",
    "Month"
).agg(
    sum("Revenue").alias("TotalRevenue")
)

country_sales = df.groupBy(
    "Country"
).agg(
    sum("Revenue").alias("Revenue")
)

product_sales = df.groupBy(
    "Description"
).agg(
    sum("Revenue").alias("Revenue")
)
