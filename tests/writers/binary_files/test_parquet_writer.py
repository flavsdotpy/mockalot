import importlib

import pytest
from unittest.mock import patch, MagicMock

from mockalot.exceptions import DependencyNotAvailable
from mockalot.writers import ParquetWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


@patch("importlib.import_module")
def test_parquet_writer_write(mock_import_module, tmp_path):
    mock_pa = MagicMock()
    mock_pq = MagicMock()
    def import_mock(name, *args):
        if name == "pyarrow":
            return mock_pa
        elif name == "pyarrow.parquet":
            return mock_pq
        return importlib.import_module(name, *args)
    
    mock_import_module.side_effect = import_mock

    writer = ParquetWriter(output_filename="test", output_path=tmp_path)

    from_pydict_return = MagicMock()
    mock_pa.Table.from_pydict.return_value = from_pydict_return
    mock_pq.write_table.return_value = None
    
    writer.write(TEST_DATA)

    mock_pa.Table.from_pydict.assert_called_once_with({key: [d[key] for d in TEST_DATA] for key in TEST_DATA[0]})
    mock_pq.write_table.assert_called_once_with(from_pydict_return, writer.output_file)


@patch("importlib.import_module")
def test_missing_dependency(mock_import_module):
    mock_import_module.side_effect = ImportError
    with pytest.raises(DependencyNotAvailable):
        ParquetWriter()
