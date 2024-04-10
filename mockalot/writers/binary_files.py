import importlib

from ._base import FileWriter
from ..exceptions import DependencyNotAvailable


class ParquetWriter(FileWriter):

    _EXTENSION = "parquet"

    def __init__(self, *args, **kwargs):
        try:
            self.__pa = importlib.import_module("pyarrow")
            self.__pq = importlib.import_module("pyarrow.parquet")
        except ImportError:
            raise DependencyNotAvailable("Parquet dependencies are not available! You can easily install it with `pip install mockalot[parquet]`!")
        super().__init__(*args, **kwargs)


    def write(self, data: list[dict]):
        table = self.__pa.Table.from_pydict({key: [d[key] for d in data] for key in data[0]})
        self.__pq.write_table(table, self.output_file)
