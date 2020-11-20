import pandas as pd
import pyspark
from IPython.display import display


class DataFrame:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self._frame: pd.DataFrame = data
        elif isinstance(data, pyspark.sql.DataFrame):
            self._frame: pd.DataFrame = data.toPandas()

    def show(self, n=20, truncate=True, console=False):
        if console:
            print(self._frame.to_string(index=False, max_rows=n))
        else:
            display((self._frame,))
