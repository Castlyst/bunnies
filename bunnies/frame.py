from .cols import col, Column

import pandas as pd
import pyspark
from IPython.display import display_html


class DataFrame:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self._frame: pd.DataFrame = data
        elif isinstance(data, pyspark.sql.DataFrame):
            self._frame: pd.DataFrame = data.toPandas()

    def __getitem__(self, item):
        if isinstance(item, (str, int)):
            return col(item)
        elif isinstance(item, (list, tuple)):
            return self.select(item)
        elif isinstance(item, Column):
            return item
        else:
            raise TypeError(f"unexpected item types: {type(item)}")

    def __getattr__(self, item):
        if item not in self._frame.columns:
            raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{item}'")
        return col(item)

    def show(self, n=20, truncate=True, console=False):
        if console:
            print(self._frame.to_string(index=False, max_rows=n))
        else:
            display_html(self._frame.to_html(index=False, max_rows=n), raw=True)

    def select(self, *cols):
        if len(cols) == 1 and isinstance(cols[0], list):
            cols = cols[0]
        cols = [c if isinstance(c, str) else c.col for c in cols]
        return DataFrame(self._frame[cols])
