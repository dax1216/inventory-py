import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def year_choices():
    return [(r,r) for r in range(2010, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
