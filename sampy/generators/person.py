from faker import Faker

from ._base import Generator
from ..config import Defaults
from ..exceptions import ParameterConflictException


class NameGenerator(Generator):

    def __init__(self, last_name_only: bool = False, first_name_only: bool = False, **params):
        self.faker = Faker(Defaults.FAKER_LOCALE)
        self.first_name_only = first_name_only
        self.last_name_only = last_name_only
        self.validate()

    def validate(self):
        if self.last_name_only and self.first_name_only:
            raise ParameterConflictException("Parameters are mutually exclusive")

    def generate(self) -> str:
        if self.last_name_only:
            return self.faker.last_name()
        elif self.first_name_only:
            return self.faker.first_name()
        else:
            return f"{self.faker.first_name()} {self.faker.last_name()}"


class PhoneNumberGenerator(Generator):

    def __init__(self) -> None:
        self.faker = Faker(Defaults.FAKER_LOCALE)

    def generate(self):
        return self.faker.basic_phone_number()
