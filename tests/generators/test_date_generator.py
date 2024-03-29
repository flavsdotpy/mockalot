from datetime import date as _date

import pytest

from sampy.exceptions import InvalidParametersException
from sampy.generators import DateGenerator


def test_generate_date():
    generator = DateGenerator()

    date = generator.generate()

    assert generator.min <= _date.fromisoformat(date) <= generator.max
    assert isinstance(date, str)


def test_generate_date_min_set():
    test_min_date = _date.fromisoformat("2024-03-01")
    generator = DateGenerator(min=test_min_date)

    date = generator.generate()

    assert test_min_date <= _date.fromisoformat(date)<= generator.max
    assert isinstance(date, str)


def test_generate_date_max_set():
    test_max_date = _date.fromisoformat("2024-03-01")
    generator = DateGenerator(max=test_max_date)

    date = generator.generate()

    assert generator.min <= _date.fromisoformat(date)<= test_max_date
    assert isinstance(date, str)


def test_generate_date_minmax_set():
    test_min_date = _date.fromisoformat("2024-01-01")
    test_max_date = _date.fromisoformat("2024-03-01")
    generator = DateGenerator(min=test_min_date, max=test_max_date)

    date = generator.generate()

    assert test_min_date <= _date.fromisoformat(date)<= test_max_date
    assert isinstance(date, str)


def test_validate_fail_equal():
    test_min_date = _date.fromisoformat("2024-01-01")
    test_max_date = _date.fromisoformat("2024-01-01")

    with pytest.raises(InvalidParametersException):
        DateGenerator(min=test_min_date, max=test_max_date)


def test_validate_fail_greater():
    test_min_date = _date.fromisoformat("2024-02-01")
    test_max_date = _date.fromisoformat("2024-01-01")

    with pytest.raises(InvalidParametersException):
        DateGenerator(min=test_min_date, max=test_max_date)
