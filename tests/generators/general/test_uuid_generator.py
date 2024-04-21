from mockalot.generators import UUIDGenerator


def test_generate_uuid(mocker):
    test_uuid = "63d2e78e-a165-4ae9-b6bb-9ab12df8fdbf"
    generator = UUIDGenerator()

    uuid4_mock = mocker.patch("mockalot.generators.general.uuid.uuid4", return_value=test_uuid)
    uuid = generator.generate()

    assert uuid == test_uuid
    uuid4_mock.assert_called_once()
