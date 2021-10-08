"""
Problem Statement: Implement a method to perform basic string compression using
the counts of the repeated characters. If the "compressed" string would not
become smaller than original string, your method should return the original
string. You can assume the string only have uppercase and lowercase letters
(a-z).

Example:
    In: aabcccccaaa
    Out: a2b1c5a3


"""


def string_compressor(s):
    """
    :param s: string of alpha characters a-z, lower and upper
    :return: compressed string of alphanumeric chars
    """
    result = []  # compressed string
    counter = 1

    prev = 0



if __name__ == "__main__":
    s = "ab"

    print(string_compressor(s))
