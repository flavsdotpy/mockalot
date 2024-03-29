import pytest

from sampy.exceptions import ParametersConflictException
from sampy.generators import NameGenerator


def test_generate_name_default(mocker):
    generator = NameGenerator()
    test_first_name = "Foo"
    test_last_name = "Bar"

    mocker.patch.object(generator.faker, 'first_name', return_value=test_first_name)
    mocker.patch.object(generator.faker, 'last_name', return_value=test_last_name)
    full_name = generator.generate()

    assert full_name == f"{test_first_name} {test_last_name}"
    generator.faker.first_name.assert_called_once()
    generator.faker.last_name.assert_called_once()


def test_generate_name_first_only(mocker):
    generator = NameGenerator(first_name_only=True)
    test_first_name = "Foo"

    mocker.patch.object(generator.faker, 'first_name', return_value=test_first_name)
    first_name = generator.generate()

    assert first_name == test_first_name
    generator.faker.first_name.assert_called_once()


def test_generate_name_last_only(mocker):
    generator = NameGenerator(last_name_only=True)
    test_last_name = "Bar"

    mocker.patch.object(generator.faker, 'last_name', return_value=test_last_name)
    last_name = generator.generate()

    assert last_name == test_last_name
    generator.faker.last_name.assert_called_once()


def test_validate_fail_both_booleans_set():
    with pytest.raises(ParametersConflictException):
        NameGenerator(first_name_only= True, last_name_only=True).generate()
