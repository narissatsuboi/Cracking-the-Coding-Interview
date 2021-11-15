"""
1.3 URLify
Problem Statement: Write a method to replace all spaces in a string with
"%20". You may assume that the string has sufficeint space at the end to hold
the additional characters, and that you are given the "true" length of the
string. Solve in place.

Example: 'Mr. John Smith' -> 'Mr.%20John%20Smith%20'

Solution: B/c strings are immutable in Python, we cannot solve in-place as
directed. Instead we will represent strings as a list of characters like so.
['M', 'r',  ,'.', , 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h']

We will get to as close to as "inplace" as possible by using minimal space.
Due to this modification, even though we are given the true length of the
string, we don't know how many spaces exist and thus how much extra space is
needed at the end of the list.

*1. Find the number of spaces and size the character list with extra space (
only would do this if they didn't provide the buffer)

2. Slow and fast pointer approach. The slow pointer is positioned at the
end of the list after all the empty spaces and is responsible for writing
the shifted characters to the list. The fast pointer is positioned at the
true end of the string and is responsible for reading the current character,
looking for spaces.

3a. When fast pointer does not find a space, the character at fast pointer is
copied to the index where slow pointer is pointing. Then, both pointers are
decremented, shifted left down the list one space.
3b. When the fast pointer finds a space, the character at slow pointer
prints the last letter of the URL, decrements, and prints the next letter of
the URL, and so on until the URL is written in full. Then, the fast pointer
is decremented.

Time complexity: O(N) where N is the length of the buffered list.
Space complexity: O(N) unless worse case sceneario where all letters are
spaces, it would be exponential 2 * N.
"""


def URLify(s, i):
    """
    :param s: string including buffer for extra spaces
    :param i: true string length (less the buffer spaces)
    :return: URLified string
    """

    URL = "%20"  # constant

    # in python strings are immutable, convert string to list
    s_lst = list(s)

    # position slow (writer) and fast (reader) pointers at the end of the
    # string and the end of the list respectively
    slow = len(s) - 1
    fast = i - 1

    # shift pointers from end to start of string
    while slow >= 0 and fast >= 0:
        # reader finds a non-space, shift to writer
        if s_lst[fast] != ' ':
            s_lst[slow] = s_lst[fast]
            slow -= 1
            fast -= 1
        # reader finds a space, write the URL in reverse
        else:
            for i in reversed(URL):
                s_lst[slow] = i
                slow -= 1
            fast -= 1

    return "".join(s_lst)

# creates custom size list with buffer
def urlify(s, URL):
    # calculate size of new string container, for each space, size increases
    # by 2. new size = len of string + (num spaces * 2)
    num_spaces = s.count(' ') # get number of spaces in string
    string = [' '] * (len(s) + (num_spaces * len(URL) - num_spaces))
    # print("length of url: ", len(URL))
    # print("num spaces: ", num_spaces)
    # print("true length of string: ", len(s))
    # print("length of new string = true length + num spaces*length of URL - "
    #       "num spaces")
    # print("length with buffer: ", len(string))
    # populate new container
    for i in range(len(s)):
        string[i] = s[i]
    # place pointers
    fast = len(s) - 1
    slow = len(string) - 1

    # traverse the list backward, replacing with slow ptr
    while fast >= 0:
        if string[fast] == ' ':
            for ch in reversed(URL):
                string[slow] = ch
                slow -= 1
            fast -= 1
        else:
            string[slow] = string[fast]
            fast -= 1
            slow -= 1
        print(string)

    return ' '.join(str(c) for c in string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "Mr John Smith    "
    n = 13
    print(URLify(s, n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
