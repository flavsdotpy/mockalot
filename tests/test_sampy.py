import pytest
from unittest.mock import MagicMock, call, patch

from sampy import Sampy
from sampy.config import Defaults
from sampy.exceptions import InvalidParameterException
from sampy.generators import IntegerGenerator, FloatGenerator
from sampy.writers import CSVWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


def test_init():
    sampy = Sampy()
    assert sampy.get_config("sample_size") == Defaults.SAMPLE_SIZE
    assert sampy.get_writer() is None
    assert len(sampy.get_columns()) == 0


def test_set_writer():
    sampy = Sampy()
    sampy.set_writer(CSVWriter, {})
    assert isinstance(sampy.get_writer(), CSVWriter)


def test_set_config():
    test_config_value = 10000
    sampy = Sampy()
    sampy.set_config("sample_size", test_config_value)
    assert sampy.get_config("sample_size") == test_config_value


def test_set_config_fails():
    test_non_existent_config = "test"
    test_config_value = 10000
    sampy = Sampy()
    with pytest.raises(InvalidParameterException):
        sampy.set_config(test_non_existent_config, test_config_value)


def test_get_config_fails():
    test_non_existent_config = "test"
    sampy = Sampy()
    with pytest.raises(InvalidParameterException):
        sampy.get_config(test_non_existent_config)


def test_set_column():
    test_column = "test"
    test_generator = IntegerGenerator
    sampy = Sampy()
    sampy.set_column(test_column, test_generator, {})
    assert isinstance(sampy.get_column(test_column), IntegerGenerator)


def test_get_column_fails():
    test_column = "test"
    sampy = Sampy()
    with pytest.raises(InvalidParameterException):
        sampy.get_column(test_column)


def test_get_columns():
    sampy = Sampy()
    test_column_a = "test_a"
    test_generator_a = IntegerGenerator
    test_column_b = "test_b"
    test_generator_b = FloatGenerator

    sampy = Sampy()
    sampy.set_column(test_column_a, test_generator_a, {})
    sampy.set_column(test_column_b, test_generator_b, {})

    test_columns = sampy.get_columns()
    assert isinstance(test_columns[test_column_a], test_generator_a)
    assert isinstance(test_columns[test_column_b], test_generator_b)


def test_get_columns_name_only():
    sampy = Sampy()
    test_column_a = "test_a"
    test_generator_a = IntegerGenerator
    test_column_b = "test_b"
    test_generator_b = FloatGenerator

    sampy = Sampy()
    sampy.set_column(test_column_a, test_generator_a, {})
    sampy.set_column(test_column_b, test_generator_b, {})

    assert sampy.get_columns(name_only=True) == [test_column_a, test_column_b]


def test_run(mocker):
    mocker.patch('sampy.get_logger')

    test_column_a = "test_a"
    test_sample_size = 10

    sampy = Sampy()
    sampy.set_config("sample_size", test_sample_size)
    sampy.set_column(test_column_a, MagicMock, {})
    sampy.set_writer(MagicMock, {})

    sampy.run()

    generator_mock = sampy.get_column(test_column_a)
    writer_mock = sampy.get_writer()

    generator_mock.generate.assert_has_calls([call() for _ in range(test_sample_size)])
    writer_mock.write.assert_called_once()

    sampy = Sampy()
    sampy.data = TEST_DATA


def test_run_multi_generator(mocker):
    mocker.patch('sampy.get_logger')

    test_column_a = "test_a"
    test_column_b = "test_b"
    test_sample_size = 100

    sampy = Sampy()
    sampy.set_config("sample_size", test_sample_size)
    sampy.set_column(test_column_a, MagicMock, {})
    sampy.set_column(test_column_b, MagicMock, {})
    sampy.set_writer(MagicMock, {})

    sampy.run()

    generator_a_mock = sampy.get_column(test_column_a)
    generator_b_mock = sampy.get_column(test_column_b)
    writer_mock = sampy.get_writer()

    generator_a_mock.generate.assert_has_calls([call() for _ in range(test_sample_size)])
    generator_b_mock.generate.assert_has_calls([call() for _ in range(test_sample_size)])
    writer_mock.write.assert_called_once()

    sampy = Sampy()
    sampy.data = TEST_DATA
