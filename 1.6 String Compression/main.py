"""
Problem Statement: Implement a method to perform basic string compression using
the counts of the repeated characters. If the "compressed" string would not
become smaller than original string, your method should return the original
string. You can assume the string only have uppercase and lowercase letters
(a-z).

Inputs: Original string Outputs: Original string or compressed string

Example:
    In: aabcccccaaa
    Out: a2b1c5a3

Clarifying question/assumption: Are uppercase handled different, assume yes
comparison based on unicode values.

Algorithm
    In: aa b ccccc aaa
    c = a counter 1, counter 2, c=a2
    c = a2 + counter 1, c = a2b1
    c = a2b1 + counter 1, 2, 3, 4, 5, c = a2b1c5
    c = a2b1c5 + counter 1, 2, 3, c = a2b1c3
    compare len of c and the len of s, return accordingly

    1. start at beginning of string, idx 0
    2. store current character in question and accumlator for each segment
    3. look to the next character, if that character is the same as the
    stored character, increment the accumulator until a differnt character
    is found or the end of string
    4. repeat until of the of string
    5. compare the lengths the original to the compressed string, return
    accordingly
"""


def string_compressor(s):
    """
    :param s: string of alpha characters a-z, lower and upper
    :return: compressed string of alphanumeric chars
    """

    c =""  # concatenate onto c
    idx = 0

    while idx < len(s):
        # get and store next character in compressed string
        curr_char = s[idx]
        c += curr_char
        count = 0 # reset accumulator
        while idx < len(s) and s[idx] == curr_char:
            idx += 1
            count += 1
        c += str(count)  # store count of current character at end of segment

    # return original or compressed string
    if len(c) > len(s): return s
    return c


if __name__ == "__main__":
    s = "aabcccccaaa"
    print(string_compressor(s))
