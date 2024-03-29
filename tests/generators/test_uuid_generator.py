import re

from sampy.generators import uuid as _uuid, UUIDGenerator


def test_generate_uuid(mocker):
    test_uuid = "63d2e78e-a165-4ae9-b6bb-9ab12df8fdbf"
    generator = UUIDGenerator()

    mocker.patch("sampy.generators.uuid.uuid4", return_value=test_uuid)
    uuid = generator.generate()

    assert uuid == test_uuid
    _uuid.uuid4.assert_called_once()



