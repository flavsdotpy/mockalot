import random
import uuid
from datetime import timedelta
from string import ascii_lowercase

from sampy.config import TODAY, FAKER


class BaseGenerator:

    @staticmethod
    def generate(**params):
        raise Exception("Not yet implemented!")


class SequenceGenerator(BaseGenerator):

    _c = 1

    @staticmethod
    def generate(start=1, jump=1, **params):
        if start > SequenceGenerator._c:
            SequenceGenerator._c = start
        c = SequenceGenerator._c
        SequenceGenerator._c += jump
        return c


class FloatGenerator(BaseGenerator):

    @staticmethod
    def generate(start=1, end=1000, decimal_places=2, **params):
        return round(random.uniform(start, end), decimal_places)


class IntegerGenerator(BaseGenerator):

    @staticmethod
    def generate(start=1, end=1000, **params):
        return random.randint(start, end)


class UUIDGenerator(BaseGenerator):

    @staticmethod
    def generate(**params):
        return str(uuid.uuid4())


class DateGenerator(BaseGenerator):

    @staticmethod
    def generate(start=(TODAY - timedelta(days=365)), end=TODAY):
        if start > end:
            raise Exception("Start date should be before end date")
        time_diff = end - start
        random_days = random.randint(0, time_diff.days)
        return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")


class NameGenerator(BaseGenerator):

    @staticmethod
    def generate(last_name_only=False, first_name_only=False, **params):
        if last_name_only and first_name_only:
            raise Exception("Parameters are mutually exclusive")
        elif last_name_only:
            return FAKER.last_name()
        elif first_name_only:
            return FAKER.first_name()
        else:
            return FAKER.name()


class EmailGenerator(BaseGenerator):

    @staticmethod
    def generate(
        safe_domain=False, public_domain=True, generated_domain=False,
        anon_username=True, generated_username=False, **params
    ):
        if [safe_domain, public_domain, generated_domain].count(True) > 1 or \
           [anon_username, generated_username].count(True) > 1:
            raise Exception("Invalid parameters!")

        if anon_username:
            username = "".join(random.choices(ascii_lowercase, k=12))
        elif generated_username:
            FAKER.user_name()
        else:
            raise Exception("Invalid parameters!")

        if safe_domain:
            domain = FAKER.safe_domain_name()
        elif public_domain:
            domain = FAKER.free_email_domain()
        elif generated_domain:
            domain = FAKER.domain_name()
        else:
            raise Exception("Invalid parameters!")

        return f"{username}@{domain}"


class PickFromListGenerator(BaseGenerator):

    @staticmethod
    def generate(elements, **params):
        return random.choice(elements)


class CityGenerator(BaseGenerator):

    @staticmethod
    def generate(**params):
        return FAKER.city()


class CountryGenerator(BaseGenerator):

    @staticmethod
    def generate(**params):
        return FAKER.country()


class PhoneNumberGenerator(BaseGenerator):

    @staticmethod
    def generate(**params):
        return FAKER.phone_number()
