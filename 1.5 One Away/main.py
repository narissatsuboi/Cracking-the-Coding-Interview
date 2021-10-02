"""
Problem Statement:
There three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away.

Example:
    pale, ple -> True  +1 insert or replace
    pales, pale -> True +1 remove
    pale, bale -> True +1 replace
    pale, bake -> False +1 replace +1 replace

Solution:
At least one operation will be expended first if the
lengths are not the same. If the lengths aren't the same we know that even if
all the letters match, one letter would need to inserted into the shorter
string or removed from the longer string (+1 operation).

For the case where the lengths are off by 1, we can default to inserting the
letter that's in the longer string but not in the shorter string to even out
the lengths.

Now we should check that the other letters are all the same and in the space
index.

0. If ever the operation counter is greater than 1 return False.
1. Compare lengths. If diff b/w lengths is more than 1 letter, return False.
2. Use two pointer traversals to find insertion point.
    -> Insertion search function
3. Use two pointer traversals to find replacement point.
    -> Replacement search function
"""


def is_one_away(s1, s2):
    """
    :param s1, s2: strings
    :return: True if one operation away from being the same string
    """
    global is_one
    n1, n2 = len(s1), len(s2)
    print("n1:", n1, "n2:", n2)

    # Check if lengths differ by more than one character
    if abs(n1 - n2) > 1:
        return False

    # Confirm no more insertions are needed than 1
    if abs(n1 - n2) == 1:
        return insertion_search(s1, s2)

    # Check if strings are the same length. If so, skip to searching for a
    # single replacement. More than one replacement found is yields a False.
    # if abs(n1 - n2) == 0:
    return replacement_search(s1, s2)


def replacement_search(s1, s2):
    """
    :param l1, s2: list representation of strings of equal length
    :return: True if less than 2 replacements were found
    """
    count = 0
    n = len(s1)
    idx1, idx2 = 0, 0

    while idx1 < n and idx2 < n:
        # check for inequality of characters
        if s1[idx1] != s2[idx2]:
            count += 1
        # increment pointers
        idx1 += 1
        idx2 += 1

    if count < 2:
        return True
    return False


def insertion_search(s1, s2):
    """
    Counts the insertions required to make the lists equal.
    :param s1, s2: strings of len diff = 1
    :return: True if exactly 1 insertion is required.
    """

    n1, n2 = len(s1), len(s2)
    idx1, idx2 = 0, 0
    count = 0

    while idx1 < n1 and idx2 < n2:
        # insertion required, +1 operation expended
        if s1[idx1] != s2[idx2]:
            count += 1
            if count > 1:  # check if operation limit exceeded
                return False

            # the pointer for the longer string shifts forward one and the
            # other pointer remains, imagine an assert occured and evened
            # the lengths out
            if n1 > n2:
                idx1 += 1
            else:  # n1 < n2
                idx2 += 1
        else:  # characters match, continue iteration
            idx1 += 1
            idx2 += 1

    return True


if __name__ == "__main__":
    s1 = "boil"
    s2 = "boils"
    print(is_one_away(s1, s2))
