from django.test import TestCase
from mainapp.utils.week_counter import get_week_number


class WeekCounterTestCase(TestCase):
    def test_converting(self):
        weeks_amount = get_week_number(day=6, month=1, year=2019)
        self.assertEqual(weeks_amount, 2)

    def test_type(self):
        weeks_amount = get_week_number(day=6, month=1, year=2019)
        self.assertEqual(isinstance(weeks_amount, int), True)


