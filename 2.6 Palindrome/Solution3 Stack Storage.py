"""
Approach 1: Extra data structure
Algorithm: A palindrome is a word that is the same when read forwards and
backwards. You know a word is a palindrome when its reversed and its the
same word. Can we reverse this linkedlist and check if they're the same?
1. We could create a copy and reverse this linked list with poiner
manipulation but a faster way is to traverse the linkedlist.
2. Add each value to a stack which is first in last out.
3. So when we pop from the stack we compare that element to the first
element in the linkedlist, while they are the same.
4. If they're the same until null its a palindrome.

Note: Which Python stack data structure should I use? Lists have stack
operations but are not efficient for large data sets. This problem doesn't
give us a limit of linked list length so assume a large data set. There is
also the Python LIFOQueue which has push and pop operations needed
for this.
"""
import queue  # for LIFOQueue


def is_palindrome1(head):
    """
    Determines if the values stored in a linked list are a palindrome
    :param head: head of linked list
    :return: True if palindrome
    """

    # Check for empty head or head's next, invalid
    if not head or not head.next:
        return True  # empty is technically a palindrome

    stack = queue.LifoQueue()  # stack init
    current = head  # pointer init

    # Traverse the linkedlist and push values onto the stack
    while current:
        stack.put(current.value)  # store value in stack
        current = current.next  # move to next node

    # Traverse the linkedlist again and pop from the stack.
    current = head  # reposition current pointer

    # Compare while the values are the same.
    for i in range(stack.qsize()):
        if current.value != stack.get(i):
            return False
        current = current.next

    return True
