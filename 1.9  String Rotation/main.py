"""
String Rotation:Assume you have a method isSubstring which checks if one
word is a substring of another. Given two strings, sl and s2, write code to
check if s2 is a rotation of sl using only one call to isSubstring
(e.g., "waterbottle" is a rotation of"erbottlewat").

Algorithm
1. Check s1 and s2 are the same length
2. Concatentate s2 and s2
3. If s1 exists in s2, return True
"""


def isSubstring(s1, s2):
    # Check if s1 and s2 are the same length
    if len(s1) != len(s2):
        return False

    # Concat s2 and s2
    s22 = s2 * 2

    p1 = p2 = 0  # point to start of s1 and s22
    # See if s1 exists in s22
    matches = 1

    while p1 < len(s1) and p2 < len(s22):
        while p1 < len(s1) and p2 < len(s22) and s22[p2] != s1[p1]:
            p2 += 1
        while p1 < len(s1) and p2 < len(s22) and s22[p2] == s1[p1]:
            p2 += 1
            p1 += 1
            matches += 1
            if matches == len(s1):
                return True
        p1 = 0
        p2 += 1
        matches = 1
    return False


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(isSubstring(s1, s2))
