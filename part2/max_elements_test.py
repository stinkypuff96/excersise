import unittest

from .max_element import max_element


class TestMaxElement(unittest.TestCase):
    # Test when list contains positive numbers
    def test_positive_numbers(self):
        self.assertEqual(max_element([1, 2, 3, 4, 5]), 5)

    # Test when list contains negative numbers
    def test_negative_numbers(self):
        self.assertEqual(max_element([-1, -2, -3, -4, -5]), -1)

    # Test when list contains both positive and negative numbers
    def test_mixed_numbers(self):
        self.assertEqual(max_element([-10, 0, 10, 5]), 10)

    # Test when list contains a single element
    def test_single_element(self):
        self.assertEqual(max_element([42]), 42)

    # Test when list contains repeated elements
    def test_repeated_elements(self):
        self.assertEqual(max_element([4, 4, 4, 4]), 4)

    # Test when list contains identical negative numbers
    def test_repeated_negative_elements(self):
        self.assertEqual(max_element([-7, -7, -7, -7]), -7)

    # Test when list contains zeros
    def test_zeros(self):
        self.assertEqual(max_element([0, 0, 0]), 0)

    # Test when list is empty (edge case)
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_element([])

if __name__ == '__main__':
    unittest.main()
