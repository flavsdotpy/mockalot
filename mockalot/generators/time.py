import random
from datetime import date, timedelta

from ._base import Generator
from ..config import TODAY
from ..exceptions import InvalidParameterException

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
