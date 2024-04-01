import random
import uuid
from datetime import date, timedelta
from string import ascii_lowercase
from typing import Any

from faker import Faker

from sampy.config import TODAY, Defaults
from sampy.exceptions import InvalidParameterException, FunctionNotImplementedException, ParameterConflictException
from sampy.log import get_logger


class Generator:

    def __init__(self):
        if type(self) == Generator:
            raise TypeError("Cannot instantiate SuperClass directly")

    def generate(self) -> Any:
        raise FunctionNotImplementedException("generate() not implemented!")


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

    def __init__(self, min: int = 1, max: int = 10, **params) -> None:
        self.min = min
        self.max = max
        self.validate()

    def validate(self):
        if self.min >= self.max:
            raise InvalidParameterException("Min should be lower than max!")

    def generate(self):
        return random.randint(self.min, self.max)


class UUIDGenerator(Generator):
    def generate(self):
        return str(uuid.uuid4())


class DateGenerator(Generator):

    def __init__(self, min: date = (TODAY - timedelta(days=365)), max: date = TODAY, **params) -> None:
        self.min = min
        self.max = max
        self.validate()

    def validate(self):
        if self.min >= self.max:
            raise InvalidParameterException("Min date should be lower than max date")

    def generate(self):
        time_diff = self.max - self.min
        random_days = random.randint(0, time_diff.days)
        return (self.min + timedelta(days=random_days)).isoformat()


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


class EmailGenerator(Generator):

    def __init__(
        self, safe_domain: bool = False, public_domain: bool = False, anon_username: bool = False, **params
    ) -> None:
        self.faker = Faker(Defaults.FAKER_LOCALE)
        self.safe_domain = safe_domain
        self.public_domain = public_domain
        self.anon_username = anon_username
        self.validate()

    def validate(self):
        if self.safe_domain and self.public_domain:
            raise ParameterConflictException("Domain parameters are mutually exclusive!")

    def generate(self):
        if self.anon_username:
            username = "".join(random.choices(ascii_lowercase, k=12))
        else:
            username = self.faker.user_name()

        if self.safe_domain:
            domain = self.faker.safe_domain_name()
        elif self.public_domain:
            domain = self.faker.free_email_domain()
        else:
            domain = self.faker.domain_name()

        return f"{username}@{domain}"


class PickFromListGenerator(Generator):

    def __init__(self, elements: list) -> None:
        self.elements = elements
        self.validate()

    def validate(self):
        if len(self.elements) == 0:
            raise InvalidParameterException("At least one element must be set!")

    def generate(self):
        return random.choice(self.elements)


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


class PhoneNumberGenerator(Generator):

    def __init__(self) -> None:
        self.faker = Faker(Defaults.FAKER_LOCALE)

    def generate(self):
        return self.faker.basic_phone_number()
