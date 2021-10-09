"""
Problem statement: Reverse a singly linked list
Approach: Reverse the linked list and compare it to the original list. Only
need to compare the first half of the list.

Modularize the code
1. is_palindrome
2. reverse and clone
3. lists are equal

Time complexity is O(N), traversing each element in head
Space complexity is O(N), storing each element in head in a new list
"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None


def is_palindrome(head):
    """
    :param head: Head of linkedlist
    :return: True if palindrome
    """
    # reverse list
    reversed = reverse_list(head)
    # compare lists
    return are_equal_lists(head, reversed)


def reverse_list(node):
    """
    :param node: Any node
    :return: Head of new linked list, reverse of original
    """
    # point new head to None
    head = None

    # traverse to the end of the given list
    while node:
        # store the value from the given node in a new node
        new_node = ListNode(node.value)
        # point the new node to the new head
        new_node.next = head
        # shift head over to n, shift given node to get more values
        head = new_node
        node = node.next

    return head


def are_equal_lists(head1, head2):
    """
    :param head1:
    :param head2:
    :return: True if lists are equal
    """
    curr1, curr2 = head1, head2  # runner pointer init
    # traverse boths lists and compare
    while curr1 and curr2:
        if curr1.value != curr2.value:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return True


if __name__ == "__main__":
    head = ListNode("1")
    head.next = ListNode("2")
    head.next.next = ListNode("1")
    # head.next.next.next = ListNode("4")

    print(is_palindrome(head))
