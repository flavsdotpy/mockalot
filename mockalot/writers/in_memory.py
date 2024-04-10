import importlib

from ._base import InMemoryWriter
from ..exceptions import DependencyNotAvailable


class PythonListWriter(InMemoryWriter):
    
    def write(self, data: list[dict]):
        return data


class PandasDataframeWriter(InMemoryWriter):

    def __init__(self, *args, **kwargs):
        try:
            self.__pd = importlib.import_module("pandas")
        except ImportError:
            raise DependencyNotAvailable("Pandas dependencies are not available! You can easily install it with `pip install mockalot[pandas]`!")
        super().__init__(*args, **kwargs)
        
    def write(self, data: list[dict]):
        return self.__pd.DataFrame(data)


class PysparkDataframeWriter(InMemoryWriter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.__spark = importlib.import_module("pyspark.sql").SparkSession.builder.appName('mockalot').getOrCreate()
        except ImportError:
            raise DependencyNotAvailable("PySpark dependencies are not available! You can easily install it with `pip install mockalot[pyspark]`!")
        
    def write(self, data: list[dict]):
        return self.__spark.createDataFrame(data)

