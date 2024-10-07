import unittest

from .count_vowels import count_vowels


# Unit test class
class TestCountVowels(unittest.TestCase):
    # Test with a string containing all vowels
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    # Test with a string containing no vowels
    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    # Test with a mixed string (vowels and consonants)
    def test_mixed_string(self):
        self.assertEqual(count_vowels("hello world"), 3)

    # Test with an empty string
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    # Test with a string of only uppercase vowels
    def test_uppercase_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    # Test with a string of mixed case vowels and consonants
    def test_mixed_case(self):
        self.assertEqual(count_vowels("HelLo WoRLd"), 3)

    # Test with special characters and numbers
    def test_special_characters(self):
        self.assertEqual(count_vowels("123 @!#"), 0)

    # Test with a string with whitespace and vowels
    def test_whitespace_vowels(self):
        self.assertEqual(count_vowels("  aei "), 3)


# Run the tests
if __name__ == "__main__":
    unittest.main()
