import json

from unittest.mock import mock_open, call, patch

from mockalot.writers import JsonWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


@patch("builtins.open", new_callable=mock_open)
def test_json_writer_write(mock_open, tmp_path):
    writer = JsonWriter(output_filename="test", output_path=tmp_path)
    writer.write(TEST_DATA)

    mock_open.assert_called_once_with(f"{tmp_path}/test.{writer._EXTENSION}", "w")
    mock_open_handler = mock_open()
    mock_open_handler.write.assert_called_once_with(json.dumps(TEST_DATA))


@patch("builtins.open", new_callable=mock_open)
def test_json_writer_write_jsonlines(mock_open, tmp_path):
    writer = JsonWriter(output_filename="test", output_path=tmp_path, jsonlines=True)
    writer.write(TEST_DATA)

    mock_open.assert_called_once_with(f"{tmp_path}/test.{writer._EXTENSION}", "w")

    calls = list()
    for row in TEST_DATA:
        calls.append(call(json.dumps(row)))
        calls.append(call("\n"))
    mock_open_handler = mock_open()
    mock_open_handler.write.assert_has_calls(calls, any_order=True)
