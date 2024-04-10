import pytest
from unittest.mock import patch, MagicMock

from mockalot.exceptions import DependencyNotAvailable
from mockalot.writers import PandasDataframeWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


@patch("importlib.import_module")
def test_pandas_writer_write(mock_import_module):
    mock_pd = MagicMock()
    mock_import_module.return_value = mock_pd

    dataframe_return_value = "This was mocked!"
    writer = PandasDataframeWriter()

    mock_pd.DataFrame.return_value = dataframe_return_value
    
    returned_value = writer.write(TEST_DATA)

    assert returned_value == dataframe_return_value
    mock_pd.DataFrame.assert_called_once_with(TEST_DATA)


@patch("importlib.import_module")
def test_missing_dependency(mock_import_module):
    mock_import_module.side_effect = ImportError
    with pytest.raises(DependencyNotAvailable):
        PandasDataframeWriter()
