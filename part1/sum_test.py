import unittest

from .sum import sum


# Define the test cases
class TestSumFunction(unittest.TestCase):
    # Test when list is empty
    def test_empty_list(self):
        self.assertEqual(sum([]), 0, "Should return 0 for an empty list")

    # Test when list has one element
    def test_single_element(self):
        self.assertEqual(
            sum([5]), 5, "Should return the element itself for a single-element list"
        )

    # Test when list has multiple positive integers
    def test_multiple_positive(self):
        self.assertEqual(
            sum([1, 2, 3]), 6, "Should return the sum of positive integers"
        )

    # Test when list has negative integers
    def test_multiple_negative(self):
        self.assertEqual(
            sum([-1, -2, -3]), -6, "Should return the sum of negative integers"
        )

    # Test when list has both positive and negative integers
    def test_mixed_values(self):
        self.assertEqual(
            sum([10, -3, 5, -2]), 10, "Should return the sum of mixed integers"
        )

    # Test when list has all zeros
    def test_all_zeros(self):
        self.assertEqual(
            sum([0, 0, 0]), 0, "Should return 0 when the list has only zeros"
        )

    # Test when list has large integers
    def test_large_integers(self):
        self.assertEqual(
            sum([1000000, 2000000, -3000000]), 0, "Should correctly sum large integers"
        )


# This allows running the tests from the command line
if __name__ == "__main__":
    unittest.main()
