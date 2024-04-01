import pytest
from unittest.mock import MagicMock, call, patch

from mockalot import Mockalot
from mockalot.config import Defaults
from mockalot.exceptions import InvalidParameterException
from mockalot.generators import IntegerGenerator, FloatGenerator
from mockalot.writers import CSVWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


def test_init():
    mockalot = Mockalot()
    assert mockalot.get_config("sample_size") == Defaults.SAMPLE_SIZE
    assert mockalot.get_writer() is None
    assert len(mockalot.get_columns()) == 0


def test_set_writer():
    mockalot = Mockalot()
    mockalot.set_writer(CSVWriter, {})
    assert isinstance(mockalot.get_writer(), CSVWriter)


def test_set_config():
    test_config_value = 10000
    mockalot = Mockalot()
    mockalot.set_config("sample_size", test_config_value)
    assert mockalot.get_config("sample_size") == test_config_value


def test_set_config_fails():
    test_non_existent_config = "test"
    test_config_value = 10000
    mockalot = Mockalot()
    with pytest.raises(InvalidParameterException):
        mockalot.set_config(test_non_existent_config, test_config_value)


def test_get_config_fails():
    test_non_existent_config = "test"
    mockalot = Mockalot()
    with pytest.raises(InvalidParameterException):
        mockalot.get_config(test_non_existent_config)


def test_set_column():
    test_column = "test"
    test_generator = IntegerGenerator
    mockalot = Mockalot()
    mockalot.set_column(test_column, test_generator, {})
    assert isinstance(mockalot.get_column(test_column), IntegerGenerator)


def test_get_column_fails():
    test_column = "test"
    mockalot = Mockalot()
    with pytest.raises(InvalidParameterException):
        mockalot.get_column(test_column)


def test_get_columns():
    mockalot = Mockalot()
    test_column_a = "test_a"
    test_generator_a = IntegerGenerator
    test_column_b = "test_b"
    test_generator_b = FloatGenerator

    mockalot = Mockalot()
    mockalot.set_column(test_column_a, test_generator_a, {})
    mockalot.set_column(test_column_b, test_generator_b, {})

    test_columns = mockalot.get_columns()
    assert isinstance(test_columns[test_column_a], test_generator_a)
    assert isinstance(test_columns[test_column_b], test_generator_b)


def test_get_columns_name_only():
    mockalot = Mockalot()
    test_column_a = "test_a"
    test_generator_a = IntegerGenerator
    test_column_b = "test_b"
    test_generator_b = FloatGenerator

    mockalot = Mockalot()
    mockalot.set_column(test_column_a, test_generator_a, {})
    mockalot.set_column(test_column_b, test_generator_b, {})

    assert mockalot.get_columns(name_only=True) == [test_column_a, test_column_b]


def test_run(mocker):
    mocker.patch('mockalot.get_logger')

    test_column_a = "test_a"
    test_sample_size = 10

    mockalot = Mockalot()
    mockalot.set_config("sample_size", test_sample_size)
    mockalot.set_column(test_column_a, MagicMock, {})
    mockalot.set_writer(MagicMock, {})

    mockalot.run()

    generator_mock = mockalot.get_column(test_column_a)
    writer_mock = mockalot.get_writer()

    generator_mock.generate.assert_has_calls([call() for _ in range(test_sample_size)])
    writer_mock.write.assert_called_once()

    mockalot = Mockalot()
    mockalot.data = TEST_DATA


def test_run_multi_generator(mocker):
    mocker.patch('mockalot.get_logger')

    test_column_a = "test_a"
    test_column_b = "test_b"
    test_sample_size = 100

    mockalot = Mockalot()
    mockalot.set_config("sample_size", test_sample_size)
    mockalot.set_column(test_column_a, MagicMock, {})
    mockalot.set_column(test_column_b, MagicMock, {})
    mockalot.set_writer(MagicMock, {})

    mockalot.run()

    generator_a_mock = mockalot.get_column(test_column_a)
    generator_b_mock = mockalot.get_column(test_column_b)
    writer_mock = mockalot.get_writer()

    generator_a_mock.generate.assert_has_calls([call() for _ in range(test_sample_size)])
    generator_b_mock.generate.assert_has_calls([call() for _ in range(test_sample_size)])
    writer_mock.write.assert_called_once()

    mockalot = Mockalot()
    mockalot.data = TEST_DATA
