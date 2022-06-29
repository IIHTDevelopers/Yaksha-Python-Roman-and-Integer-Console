import unittest
from integer_to_roman import Roman
from roman_to_integer import Integer
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_single_digit_result(self):
        test_obj = TestUtils()
        result=Roman().int_to_roman(5)
        if result=='V':
            test_obj.yakshaAssert("TestSingleDigitResult", True, "functional")
            print("TestSingleDigitResult = Passed")
        else:
            test_obj.yakshaAssert("TestSingleDigitResult", False, "functional")
            print("TestSingleDigitResult = Failed")

    def test_two_digit_result(self):
        test_obj = TestUtils()
        result=Roman().int_to_roman(12)
        if result=='XII':
            test_obj.yakshaAssert("TestTwoDigitResult", True, "functional")
            print("TestTwoDigitResult = Passed")
        else:
            test_obj.yakshaAssert("TestTwoDigitResult", False, "functional")
            print("TestTwoDigitResult = Failed")

    def test_three_digit_result(self):
        test_obj = TestUtils()
        result=Roman().int_to_roman(143)
        if result=='CXLIII':
            test_obj.yakshaAssert("TestThreeDigitResult", True, "functional")
            print("TestThreeDigitResult = Passed")
        else:
            test_obj.yakshaAssert("TestThreeDigitResult", False, "functional")
            print("TestThreeDigitResult = Failed")

    def test_500_result(self):
        test_obj = TestUtils()
        result=Roman().int_to_roman(500)
        if result=='D':
            test_obj.yakshaAssert("Test500Result", True, "functional")
            print("Test500Result = Passed")
        else:
            test_obj.yakshaAssert("Test500Result", False, "functional")
            print("Test500Result = Failed")

    def test_1000_result(self):
        test_obj = TestUtils()
        result=Roman().int_to_roman(1000)
        if result=='M':
            test_obj.yakshaAssert("Test1000Result", True, "functional")
            print("Test1000Result = Passed")
        else:
            test_obj.yakshaAssert("Test1000Result", False, "functional")
            print("Test1000Result = Failed")

    def test_single_char_result(self):
        test_obj = TestUtils()
        result=Integer().roman_to_int('V')
        if result==5:
            test_obj.yakshaAssert("TestSingleCharResult", True, "functional")
            print("TestSingleCharResult = Passed")
        else:
            test_obj.yakshaAssert("TestSingleCharResult", False, "functional")
            print("TestSingleCharResult = Failed")

    def test_xv_result(self):
        test_obj = TestUtils()
        result=Integer().roman_to_int('XV')
        if result==15:
            test_obj.yakshaAssert("TestXVResult", True, "functional")
            print("TestXVResult = Passed")
        else:
            test_obj.yakshaAssert("TestXVResult", False, "functional")
            print("TestXVResult = Failed")

    def test_CXLIII_result(self):
        test_obj = TestUtils()
        result=Integer().roman_to_int('CXLIII')
        if result==143:
            test_obj.yakshaAssert("TestCXLIIIResult", True, "functional")
            print("TestCXLIIIResult = Passed")
        else:
            test_obj.yakshaAssert("TestCXLIIIResult", False, "functional")
            print("TestCXLIIIResult = Failed")

    def test_D_result(self):
        test_obj = TestUtils()
        result=Integer().roman_to_int('D')
        if result==500:
            test_obj.yakshaAssert("TestDResult", True, "functional")
            print("TestDResult = Passed")
        else:
            test_obj.yakshaAssert("TestDResult", False, "functional")
            print("TestDResult = Failed")

    def test_M_result(self):
        test_obj = TestUtils()
        result=Integer().roman_to_int('M')
        if result==1000:
            test_obj.yakshaAssert("TestMResult", True, "functional")
            print("TestMResult = Passed")
        else:
            test_obj.yakshaAssert("TestMResult", False, "functional")
            print("TestMResult = Failed")
