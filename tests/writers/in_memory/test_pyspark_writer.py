import pytest
from unittest.mock import patch, MagicMock

from mockalot.exceptions import DependencyNotAvailable
from mockalot.writers import PysparkDataframeWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


@patch("importlib.import_module")
def test_pyspark_writer_write(mock_import_module):
    mock_spark_sql = MagicMock()
    mock_spark = MagicMock()
    mock_import_module.return_value = mock_spark_sql
    mock_spark_sql.SparkSession.builder.appName.return_value.getOrCreate.return_value = mock_spark

    dataframe_return_value = "This was mocked!"

    writer = PysparkDataframeWriter()

    mock_spark.createDataFrame.return_value = dataframe_return_value
    
    returned_value = writer.write(TEST_DATA)

    assert returned_value == dataframe_return_value
    mock_spark.createDataFrame.assert_called_once_with(TEST_DATA)


@patch("importlib.import_module")
def test_missing_dependency(mock_import_module):
    mock_import_module.side_effect = ImportError
    with pytest.raises(DependencyNotAvailable):
        PysparkDataframeWriter()
