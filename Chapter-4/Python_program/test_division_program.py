'''
This program is used for writing the unit test.
'''
import unittest
from division_program import div

# Writing the class for unit testing.
class Testdivision(unittest.TestCase):

    # Test Case-1: Check function with valid values.
    def test_valid_value(self):
        self.assertAlmostEqual(div(6,3), 2)

    # Test Case-2: It will check the if part.
    def test_value_comparision(self):
        self.assertAlmostEqual(div(3,59), 0)

    # Test Case-3: For raising the type error.
    def test_string(self):
        self.assertRaises(TypeError, div("hi",34))