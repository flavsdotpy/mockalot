from mockalot.generators import CityGenerator


def test_generate_city(mocker):
    generator = CityGenerator()
    test_city = "Sao Paulo"

    mocker.patch.object(generator.faker, 'city', return_value=test_city)
    city = generator.generate()

    assert city == test_city
    generator.faker.city.assert_called_once()
