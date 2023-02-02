from pyspark.sql import DataFrame


def load_csv(data: DataFrame) -> DataFrame:
    return data


def identity(data: DataFrame) -> DataFrame:
    return data
