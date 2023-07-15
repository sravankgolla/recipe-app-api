"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Tests the calc module """

    def test_add_two_numbers(self):
        """ tests the adding of two numbers"""
        res = calc.add(5, 4)

        self.assertEqual(res, 9)

    def test_substract_numbers(self):
        """tests the substract numbers"""
        res = calc.substract(2, 1)

        self.assertEqual(res, 1)
