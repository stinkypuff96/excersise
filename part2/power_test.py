import unittest

from .power import power


class TestPower(unittest.TestCase):
    # Test when both base and exponent are positive
    def test_positive_base_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)  # 2^3 = 8

    # Test when base is zero and exponent is positive
    def test_zero_base_positive_exponent(self):
        self.assertEqual(power(0, 5), 0)  # 0^5 = 0

    # Test when base is positive and exponent is zero
    def test_positive_base_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)  # 5^0 = 1

    # Test when base is zero and exponent is zero
    def test_zero_base_zero_exponent(self):
        self.assertEqual(power(0, 0), 1)  # 0^0 is commonly defined as 1

    # Test when base is negative and exponent is even
    def test_negative_base_even_exponent(self):
        self.assertEqual(power(-2, 4), 16)  # (-2)^4 = 16

    # Test when base is negative and exponent is odd
    def test_negative_base_odd_exponent(self):
        self.assertEqual(power(-2, 3), -8)  # (-2)^3 = -8

    # Test when exponent is negative
    def test_positive_base_negative_exponent(self):
        self.assertEqual(power(2, -3), 0.125)  # 2^-3 = 1/8 = 0.125

if __name__ == '__main__':
    unittest.main()
