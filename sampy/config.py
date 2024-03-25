import os
from datetime import date

from faker import Faker


FAKER = Faker()
TODAY = date.today()


class Defaults:
    SAMPLE_SIZE = os.getenv("SAMPY_SAMPLE_SIZE", 1000)
    OUTPUT_PATH = os.getenv("SAMPY_OUTPUT_PATH", "./output")
