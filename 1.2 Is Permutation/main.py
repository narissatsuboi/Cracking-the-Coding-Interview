"""
1.2 Is Permutation: Given two strings, write a method to decide if one is a
permutation of the other.
in: two strings
out: True/False
clarifying questions: case sensitive? whitespace sensitve? if not, handle.
1 brute force - nested for loop
intuition: strings of different lengths cannot be permutations of each other
2 sort and compare approach: convert strings to lists, sort the lists,
check if same
3 char counts - array of char counts (check with size of char set), record
frequency of char in one string, then iterate through the array with the
chars of the other string. subtract the count, if count < 0 -> false
hash map  - seen chars in hash map return false when char already seen
"""

import unittest
from collections import Counter


# 1 brute force
def is_permutation_brute(s1, s2):
    # confirm same len
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return False
    # iterate through each element looking for the match in the other string
    for i in range(n1):
        curr_char = s1[i]
        for j in range(n1):
            if curr_char not in s2:
                return False
    return True


# 2 sort and compare
def is_permutation_sort(s1, s2):
    # confirm same len
    if len(s1) != len(s2): return False

    # sort both O(logn)
    s1 = sorted(s1)
    s2 = sorted(s2)

    # compare each char at the same position O(n)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


# 3 check character count
def is_permutation_count(s1, s2):
    # check len
    if len(s1) != len(s2): return False

    # compare frequency tables of characters
    c1 = Counter(s1)
    c2 = Counter(s2)
    if c1 != c2: return False
    return True


class TestIsPermutation(unittest.TestCase):
    def test_is_permutation(self):
        self.assertEqual(True, is_permutation_brute("abc", "cba"))
        self.assertEqual(True, is_permutation_brute("", ""))
        self.assertEqual(False, is_permutation_brute("ab", "abb"))
        self.assertEqual(False, is_permutation_brute("abc", "bda"))

        self.assertEqual(True, is_permutation_sort("abc", "cba"))
        self.assertEqual(True, is_permutation_sort("", ""))
        self.assertEqual(False, is_permutation_sort("ab", "abb"))
        self.assertEqual(False, is_permutation_sort("abc", "bda"))

        self.assertEqual(True, is_permutation_count("abc", "cba"))
        self.assertEqual(True, is_permutation_count("", ""))
        self.assertEqual(False, is_permutation_count("ab", "abb"))
        self.assertEqual(False, is_permutation_count("abc", "bda"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main(verbosity=2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
