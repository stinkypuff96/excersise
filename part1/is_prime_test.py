import unittest

from .is_prime import is_prime


class TestIsPrimeFunction(unittest.TestCase):
    def test_small_prime_numbers(self):
        """Test that small prime numbers return True"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_small_non_prime_numbers(self):
        """Test that small non-prime numbers return False"""
        self.assertFalse(is_prime(1))  # 1 is not considered a prime number
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_large_prime_numbers(self):
        """Test that large prime numbers return True"""
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(97))

    def test_large_non_prime_numbers(self):
        """Test that large non-prime numbers return False"""
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(150))
        self.assertFalse(is_prime(200))

    def test_edge_cases(self):
        """Test edge cases like negative numbers and zero"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))  # By definition, 1 is not prime

    def test_large_composite_numbers(self):
        """Test very large composite numbers"""
        self.assertFalse(is_prime(1001))
        self.assertFalse(is_prime(1024))


if __name__ == "__main__":
    unittest.main()
