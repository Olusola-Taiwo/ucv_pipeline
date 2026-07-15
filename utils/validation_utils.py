from pyspark.sql.functions import col

def not_null(df, col_name):
    return df.filter(col(col_name).isNotNull())

def all_not_null(df, cols):
    cond = None
    for c in cols:
        expr = col(c).isNotNull()
        cond = expr if cond is None else (cond & expr)
    return df.filter(cond)
