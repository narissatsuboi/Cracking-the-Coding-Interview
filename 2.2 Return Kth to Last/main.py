"""
Return Kth to Last: Implement an algorithm to fnd the kth to last element
of a singly linked list.

Algorithm: The kth element to last is K-1 elements from null.
1. Initalize fast and slow pointers.
2. Move fast K+1 spaces forward while leaving slow at the first element.
3. Increment both fast and slow until fast reached None.
4. Slow is K elements behind fast
"""


class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    current = head
    while current is not None:
        print(current.value,end="->")
        current = current.next


def find_kth_node(head, K):
    # if head or head's next is null return the node
    if head is None or head.next is None:
        return head

    # assign pointers
    slow = fast = head

    # accelerate fast K+1 elements forward
    for i in range(K+1):
        fast = fast.next

    # until fast gets to null increment both
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # shift slow one time to account for fast not technially reaching null
    slow = slow.next

    return slow.value


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    print("Find 4th last element")
    print_list(head)
    print()
    print(find_kth_node(head, 4))
    print("Find 1st last element")
    print_list(head)
    print()
    print(find_kth_node(head, 1))