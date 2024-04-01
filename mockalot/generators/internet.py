import random
from string import ascii_lowercase

from faker import Faker

from ._base import Generator
from ..config import Defaults
from ..exceptions import ParameterConflictException


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
