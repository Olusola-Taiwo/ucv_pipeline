from pyspark.sql import SparkSession

def get_spark(app_name="UCV"):
    return (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.shuffle.partitions", "200")
        .getOrCreate()
    )
