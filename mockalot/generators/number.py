import random

from ._base import Generator
from ..exceptions import InvalidParameterException


class SequenceGenerator(Generator):

    def __init__(self, start: int = 1, jump: int = 1, **params):
        self.start = start
        self.jump = jump
        self.current = start - jump

    def generate(self) -> int:
        self.current += self.jump
        return self.current


class FloatGenerator(Generator):

    def __init__(self, min: float = 1.0, max: float = 1000.0, decimal_places: int = 2, **params):
        self.min = min
        self.max = max
        self.decimal_places = int(decimal_places)
        self.validate()

    def validate(self):
        if self.min >= self.max:
            raise InvalidParameterException("Min should be lower than max!")
        if (self.max - self.min) < .1:
            raise InvalidParameterException("Difference between numbers must be at least 0.1")

    def generate(self):
        return round(random.uniform(self.min, self.max), self.decimal_places)


class IntegerGenerator(Generator):

    def __init__(self, min: int = 1, max: int = 1000, **params) -> None:
        self.min = min
        self.max = max
        self.validate()

    def validate(self):
        if self.min >= self.max:
            raise InvalidParameterException("Min should be lower than max!")

    def generate(self):
        return random.randint(self.min, self.max)
