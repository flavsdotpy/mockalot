import re

from sampy.generators import CountryGenerator


def test_generate_country(mocker):
    generator = CountryGenerator()
    test_country = "Brazil"

    mocker.patch.object(generator.faker, 'country', return_value=test_country)
    country = generator.generate()

    assert country == test_country
    generator.faker.country.assert_called_once()
