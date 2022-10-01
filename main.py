from unittest import main, TestCase


class Employee():
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def give_raise(self, amount=5000):
        self.salary += amount


class TestEmployee(TestCase):
    def setUp(self):
        self.employee = Employee('Olga', 1986-04-03)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(8500, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(500)
        self.assertEqual(4000, self.employee.salary)


if __name__ == '__main__':
    main()



