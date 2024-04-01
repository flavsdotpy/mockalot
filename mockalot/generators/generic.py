import random

from ._base import Generator
from ..exceptions import InvalidParameterException


class PickFromListGenerator(Generator):

    def __init__(self, elements: list) -> None:
        self.elements = elements
        self.validate()

    def validate(self):
        if len(self.elements) == 0:
            raise InvalidParameterException("At least one element must be set!")

    def generate(self):
        return random.choice(self.elements)
