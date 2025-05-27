import unittest
from pymath.lib.math import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_string_palindromes(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("No lemon no melon"))

    def test_string_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_integer_palindromes(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(7))

    def test_integer_non_palindromes(self):
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(4567))

    def test_string_with_spaces_and_capitalization(self):
        self.assertTrue(is_palindrome("Race Car"))
        self.assertTrue(is_palindrome("No Lemon No Melon"))
        self.assertTrue(is_palindrome("Kayak"))
        self.assertTrue(is_palindrome("Step on no pets"))

    def test_negative_integers(self):
        self.assertFalse(is_palindrome(-121)) # "-121" is not a palindrome
        self.assertTrue(is_palindrome(121))   # "121" is a palindrome
        self.assertFalse(is_palindrome(-10))  # "-10" is not a palindrome

if __name__ == '__main__':
    unittest.main()
