from datetime import datetime
from django.conf import settings


def get_week_number(day: int, month: int, year: int) -> int:
    current_date = datetime(year=year, month=month, day=day)
    delta = current_date - settings.START_DATE
    return delta.days // 7 + 1







