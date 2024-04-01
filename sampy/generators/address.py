from faker import Faker

from ._base import Generator
from ..config import Defaults


class CityGenerator(Generator):

    def __init__(self) -> None:
        self.faker = Faker(Defaults.FAKER_LOCALE)

    def generate(self):
        return self.faker.city()


class CountryGenerator(Generator):

    def __init__(self) -> None:
        self.faker = Faker(Defaults.FAKER_LOCALE)

    def generate(self):
        return self.faker.country()
