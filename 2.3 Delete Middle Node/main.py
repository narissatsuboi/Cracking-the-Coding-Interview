"""
Problem Statement: Implement an algorithm to delete a node in the middle (any
node but the first or last not necessarily the exact middle) of a singly linked list,
given only access to that node.

Example:
    Input: the node c from the linkedlist a-b-c-d-e-f
    Result: a-b-d-e-f

Algorithm:
    Since we know we can only move forward in a singly linked list and the
    given node only points the next node in the list, we need to be creative.
    0. Check for invalid input
    1. Replace the value in the given node with the value in the next node
    2. Delete the next node
"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def delete_middle_node(head):
    if head is None or head.next is None:
        return False   # failure

    current = head  # current node being replaced
    next = current.next
    current.value = next.value
    current.next = next.next


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end="->")
        current = current.next


if __name__ == "__main__":
    head = ListNode("a")
    head.next = ListNode("b")
    head.next.next = ListNode("c")
    print_list(head)
    print()
    delete_middle_node(head.next)
    print_list(head)
