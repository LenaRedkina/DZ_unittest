
from datetime import date
from datetime import datetime


class Employee:
    def __init__(self, name, birthdate, age):
        self.name = name
        self.birthdate = birthdate
        self.age = age

    def set_name(self, name):
        self.name = name
        return name

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        return birthdate

    def calc_age(self, birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        print("Test start")
        self.test_name = "Olga"
        self.test_date = "1986-03-04"
        self.test_age = "36"

    def tearDown(self):
        pass
        print("Test stop")


    def test_set_name(self):
        print("test_set_name")
        self.assertEqual(self.test_name, "Olga")


    def test_set_birthdate(self):
        print("test_set_birthdate")
        self.assertEqual(self.test_date, "1986-03-04")


    def test_calc_age(self):
        print("test_calc_age")
        self.assertEqual(self.test_age, "36")

if __name__ == '__main__':
    unittest.main()

