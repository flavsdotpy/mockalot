from sampy.generators import PhoneNumberGenerator


def test_generate_phone_number(mocker):
    generator = PhoneNumberGenerator()
    test_phone_number = "123-555-7890"

    mocker.patch.object(generator.faker, 'basic_phone_number', return_value=test_phone_number)
    phone_number = generator.generate()

    assert phone_number == test_phone_number
    generator.faker.basic_phone_number.assert_called_once()
