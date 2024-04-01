import uuid

from ._base import Generator


class UUIDGenerator(Generator):
    def generate(self):
        return str(uuid.uuid4())
