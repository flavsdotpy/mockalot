import pytest

from mockalot.exceptions import InvalidParameterException
from mockalot.generators import IntegerGenerator


def test_generate_integer():
    generator = IntegerGenerator()
    integer = generator.generate()
    assert generator.min <= integer <= generator.max


def test_generate_integer_min_set():
    test_min = 5
    generator = IntegerGenerator(min=test_min)
    integer = generator.generate()
    assert test_min <= integer <= generator.max


def test_generate_integer_max_set():
    test_max = 20
    generator = IntegerGenerator(max=test_max)
    integer = generator.generate()
    assert generator.min <= integer <= test_max


def test_validate_fail_equal():
    test_min = 10
    test_max = 10
    with pytest.raises(InvalidParameterException):
        IntegerGenerator(min=test_min, max=test_max)


def test_validate_fail_greater():
    test_min = 10
    test_max = 1
    with pytest.raises(InvalidParameterException):
        IntegerGenerator(min=test_min, max=test_max)
