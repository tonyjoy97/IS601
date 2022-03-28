import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

test_data = CsvReader('/src/UnitTestAll.csv').data
pprint(test_data)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data:
            self.assertEqual(self.calculator.add(row['addvalue2'], row['addvalue1']), int(row['addresult']))
            self.assertEqual(self.calculator.result, int(row['addresult']))

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['subvalue2'], row['subvalue1']), int(row['subresult']))
            self.assertEqual(self.calculator.result, int(row['subresult']))

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['multiplyvalue2'], row['multiplyvalue1']), int(row['multiplyresult']))
            self.assertEqual(self.calculator.result, int(row['multiplyresult']))

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

        for row in test_data:
            self.assertEqual(self.calculator.divide(row['dividevalue2'], row['dividevalue1']), round(float(row['divideresult']), 9))
            self.assertEqual(self.calculator.result, float(row['divideresult']))

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

        for row in test_data:
            self.assertEqual(self.calculator.square(row['sqvalue1']), int(row['sqresult']))
            self.assertEqual(self.calculator.result, int(row['sqresult']))

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.squareroot(4), 2)
        self.assertEqual(self.calculator.result, 2)

        for row in test_data:
            self.assertEqual(self.calculator.squareroot(row['sqrootvalue1']), round(float(row['sqrootresult']), 8))
            self.assertEqual(self.calculator.result, round(float(row['sqrootresult']),8))


if __name__ == '__main__':
    unittest.main()
