from datetime import datetime
from django.conf import settings


def get_week_number(day, month, year):
    """
        Args:
            day (int): days value
            month (int): months value
            year (int): years value

        Returns:
            int: number of week

    """
    current_date = datetime(year=year, month=month, day=day)  # creating datetime obj
    delta = current_date - settings.START_DATE  # calculating difference

    return delta.days // 7 + 1
