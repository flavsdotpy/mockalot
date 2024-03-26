import os
from datetime import date

from faker import Faker


FAKER = Faker()
TODAY = date.today()


class Defaults:
    SAMPLE_SIZE = os.getenv("SAMPY_DEFAULTS_SAMPLE_SIZE", 1000)
    OUTPUT_PATH = os.getenv("SAMPY_DEFAULTS_OUTPUT_PATH", "./output")
    OUTPUT_FILENAME = os.getenv("SAMPY_DEFAULTS_OUTPUT_FILENAME", "sample_data")
