from pyspark.sql.functions import lit

def rename(df, old, new):
    return df.withColumnRenamed(old, new)

def select_columns(df, cols):
    return df.select(*cols)

def add_constant(df, col_name, value):
    return df.withColumn(col_name, lit(value))
