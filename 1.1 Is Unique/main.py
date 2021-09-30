"""
Is Unique: Implement an algorithm to determine if
a string has all unique characters. What if you
cannot use additional data structures?
"""

"""
clarifying question: is string ASCII or Unicode? Assume ASCII. If Unicode, 
need to increase the storage size. 
input: string output: true if all chars are unique
example: abcdefg -> true, abbcdefg -> false, " " -> true

w/ data structure
iterate over string once
if char is not already in hashmap, add it
if char is already in hashmap return false
else return true

w/o data structures (brute force) O(N*2) 
iterate over array one ele at a time, iterate again looking for duplicates

other answers
Array of all 256 characters, use as lookup table
ASCII_flag_arr = [True] * 256 

"""

import unittest


def is_unique_naive(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                return False
    return True


def is_unique(s):
    seen = {}  # holds chars that have been encountered during iteration

    for c in s:
        if c in seen:
            return False
        seen[c] = True
    return True


class TestIsUnique(unittest.TestCase):
    def test_is_unique_brute(self):
        self.assertEqual(True, is_unique("abc"))
        self.assertEqual(False, is_unique("abbc"))
        self.assertEqual(True, is_unique(""))

    def test_is_unique(self):
        self.assertEqual(True, is_unique("abc"))
        self.assertEqual(False, is_unique("abbc"))
        self.assertEqual(True, is_unique(""))


if __name__ == '__main__':
    unittest.main(verbosity=2)

