"""
Sum Lists: You have two numbers represented by a linked list,
where each node contains a single digit. The digits are stored in reverse
order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.

Algorithm
1. Store elements of each list in a stack
2. Empty each stack and store as integer
3. Add integers
4. Convert integer to same format as input linked list

CTCI Algorithm
1. Add the ones place (first digits in lls), store the carry over and insert the
non cary over into a new node in the result list
2. Repeat for length of list
Edge cases:
- when one or both of the lists reaches null what do you do? set the values
pulled from to zero
- how do you handle carry over?
    45 + 6 -> 4 + (11)
    4 + (11//10) + (carry = 11/10)
    (4 + carry) + 1
    5 + 1
- how do you handle both pointers reaching null but there being # left  in
the carry over? Continue while both are not null OR carry is not null.
"""


class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None


def sum_lists(l1, l2):
    result = current = ListNode(0)  # initialize empty list to store result
    carry = 0  # holds carryover value (val//10 since must always be > 10)

    # continue while theres anything left in carry even if the lists have
    # run out
    while l1 or l2 or carry:
        # initialize pointers to each list which grab their values
        # handle case of pointers being at null and adding 0s instead of None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # add digits at each pointer
        val = val1 + val2 + carry  # add the carry from prev iteration
        # handle carry over case
        carry = val // 10  # generate carry for next iteration
        val %= 10  # get the digit only

        # add to list
        current.next = ListNode(val)

        # update pointers - they could go to None
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next



