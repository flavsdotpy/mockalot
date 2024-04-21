import random
import uuid

from ._base import Generator
from ..exceptions import InvalidParameterException


class PickFromListGenerator(Generator):

    def __init__(self, elements: list) -> None:
        self.elements = elements
        self.validate()

    def validate(self):
        if len(self.elements) <= 1:
            raise InvalidParameterException("At least one element must be set!")

    def generate(self):
        return random.choice(self.elements)


class UUIDGenerator(Generator):
    def generate(self):
        return str(uuid.uuid4())
