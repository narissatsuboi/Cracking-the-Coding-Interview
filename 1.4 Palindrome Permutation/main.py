"""
Problem Statement:
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters. The palindrome does
not need to be limited to just dictionary words.

Example:
    In: Tact Coa    Out: True (taco cat, atco cta, etc).
    In: bbaa        Out: True (abba, baab)
    In: aabaa       Out: True (baaaa, aaaab, abaaa)
Solution:
To find out if an input word was a palindrome we need to think of a property
of a palindrome that we can get from the input.
* All the counts of characters are even, except for inputs with an odd
length in which one set of character count should be odd. *

1. Find counts of each character, store
2. Check for each character that all character counts are even and at most
only 1 set of characters is odd
    -> True

Time complexity: O(N)
Space complexity: O(N)
"""

import unittest


def is_palindrome_permutation(p):
    """
    :param p: potential palindrome permutation
    :return: True if permutation of a palindrome
    """

    # make character casing uniform, remove spaces
    p = p.lower().replace(" ", "")

    # store the counts of each character
    char_frequency = {}
    for i in p:
        if i not in char_frequency:
            char_frequency[i] = 0
        char_frequency[i] += 1

    # check palindrome permutation conditions
    odd_char_count = 0  # false if greater than 1
    for counts in char_frequency.values():  # traverse values in dict
        # update odd char count if current value is odd
        if counts % 2 == 1:
            odd_char_count += 1
        # if odd char count exceeds 1, cannot be a palindrome
        if odd_char_count > 1:
            return False

    return True


class TestIsPalindromePermutation(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        self.assertEqual(True, is_palindrome_permutation("Tact coa"))
        self.assertEqual(True, is_palindrome_permutation("abba"))
        self.assertEqual(True, is_palindrome_permutation("aab"))
        self.assertEqual(True, is_palindrome_permutation("a"))

        self.assertEqual(False, is_palindrome_permutation("ab"))
        self.assertEqual(False, is_palindrome_permutation("abcbad"))


if __name__ == "__main__":
    unittest.main(verbosity=2)