"""
Implement a function to check if a linked list is a palindrome.

Assumptions: lowercase and upcase should be treated the same

Approach: In Place, no extra memory
Get size, situate a pointer at the halfway point. Reverse one side,
iterate over each side. The letters should be the same at each pointer.
Odd number length case
m -> o ->m
     ^
     |
     midpoint
split at o and flip 2nd half
m -> o -> m compare with a pointer at m and pointer at the second m

Even number length case
m -> o -> o -> m

"""


def reverse_list(head):
    prev = None  # keeps track of where head points to next
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def print_list(head):
    runner = head
    while runner:
        print(runner.value, end="->")
        runner = runner.next
    print()


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    head = ListNode("1")
    head.next = ListNode("2")
    head.next.next = ListNode("3")
    head.next.next.next = ListNode("4")

    # print(is_palindrome2(head))

    print_list(head)
    head = reverse_list(head)
    print_list(head)
