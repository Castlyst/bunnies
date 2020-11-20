from .frame import DataFrame
import pandas as pd


def createDataFrame(data, schema=None, samplingRatio=None, verifySchema=True):
    return create_data_frame(data, schema, samplingRatio, verifySchema)


def create_data_frame(data, schema=None, samplingRatio=None, verifySchema=True):
    if isinstance(data, pd.DataFrame):
        return DataFrame(data)
    frame = _from_pyspark(data)
    if frame:
        return DataFrame(frame)
    raise NotImplementedError("other data types not yet supported, only pd and pyspark ")


def _from_pyspark(data):
    try:
        import pyspark
        has_pyspark = True
    except ImportError:
        has_pyspark = False
    if has_pyspark and isinstance(data, pyspark.sql.DataFrame):
        return data.toPandas()
