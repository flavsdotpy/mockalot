from unittest.mock import mock_open, patch

from mockalot.writers import CSVWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


@patch("builtins.open", new_callable=mock_open)
@patch("csv.DictWriter")
def test_csv_writer_write(mock_dict_writer, mock_open, tmp_path):
    writer = CSVWriter(output_filename="test", output_path=tmp_path)
    writer.write(TEST_DATA)

    mock_open.assert_called_once_with(f"{tmp_path}/test.{writer._EXTENSION}", "w")
    handle = mock_open()
    mock_dict_writer.assert_called_once_with(handle, fieldnames=["name", "age"])
    writer_instance = mock_dict_writer()
    writer_instance.writeheader.assert_called_once()
    writer_instance.writerows.assert_called_once_with(TEST_DATA)
