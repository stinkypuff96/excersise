import unittest

from .reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    # Test reversing a regular string
    def test_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")  # Reversing a normal string

    # Test reversing an empty string
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")  # Reversing an empty string should return an empty string

    # Test reversing a single character string
    def test_single_char_string(self):
        self.assertEqual(reverse_string("a"), "a")  # Reversing a single character should return the same character

    # Test reversing a string with spaces
    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")  # Reversing a string with spaces

    # Test reversing a string with special characters
    def test_string_with_special_chars(self):
        self.assertEqual(reverse_string("!@# hello"), "olleh #@!")  # Reversing a string with special characters

    # Test reversing a palindrome string
    def test_palindrome_string(self):
        self.assertEqual(reverse_string("madam"), "madam")  # Reversing a palindrome should return the same string

if __name__ == '__main__':
    unittest.main()
