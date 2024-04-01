import pytest

from sampy.exceptions import InvalidParameterException
from sampy.generators import FloatGenerator


def test_generate_float():
    generator = FloatGenerator()
    integer = generator.generate()
    assert generator.min <= integer <= generator.max
    assert isinstance(integer, float)


def test_generate_float_min_set():
    test_min = 5.0
    generator = FloatGenerator(min=test_min)
    integer = generator.generate()
    assert test_min <= integer <= generator.max
    assert isinstance(integer, float)


def test_generate_float_max_set():
    test_max = 20.0
    generator = FloatGenerator(max=test_max)
    integer = generator.generate()
    assert generator.min <= integer <= test_max
    assert isinstance(integer, float)


def test_validate_fail_equal():
    test_min = 10.0
    test_max = 10.0
    with pytest.raises(InvalidParameterException):
        FloatGenerator(min=test_min, max=test_max)


def test_validate_fail_greater():
    test_min = 10.0
    test_max = 1.0
    with pytest.raises(InvalidParameterException):
        FloatGenerator(min=test_min, max=test_max)


def test_validate_fail_small_difference():
    test_min = 10.0
    test_max = 10.02
    with pytest.raises(InvalidParameterException):
        FloatGenerator(min=test_min, max=test_max)
