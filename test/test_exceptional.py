import unittest
from integer_to_roman import Roman
from roman_to_integer import Integer
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_for_int_to_roman(self):
        test_obj = TestUtils()
        try:
            Roman().int_to_roman("15")
            test_obj.yakshaAssert("TestTypeErrorForIntToRoman", False, "exception")
            print("TestTypeErrorForIntToRoman = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForIntToRoman", True, "exception")
            print("TestTypeErrorForIntToRoman = Passed")

    def test_key_error_for_roman_to_int(self):
        test_obj = TestUtils()
        try:
            Integer().roman_to_int('5')
            test_obj.yakshaAssert("TestKeyErrorForRomanToInt", False, "exception")
            print("TestKeyErrorForRomanToInt = Failed")
        except KeyError:
            test_obj.yakshaAssert("TestKeyErrorForRomanToInt", True, "exception")
            print("TestKeyErrorForRomanToInt = Passed")
