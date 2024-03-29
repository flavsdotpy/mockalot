import os
from datetime import date


class Defaults:
    FAKER_LOCALE = os.getenv("SAMPY_DEFAULTS_FAKER_LOCALE", "en_US")
    SAMPLE_SIZE = os.getenv("SAMPY_DEFAULTS_SAMPLE_SIZE", 1000)
    OUTPUT_PATH = os.getenv("SAMPY_DEFAULTS_OUTPUT_PATH", "./output")
    OUTPUT_FILENAME = os.getenv("SAMPY_DEFAULTS_OUTPUT_FILENAME", "sample_data")

TODAY = date.today()
