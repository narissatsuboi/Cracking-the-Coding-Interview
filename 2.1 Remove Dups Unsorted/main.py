"""
Remove duplicates from unsorted linked list. Assume given nonempty list.

Algorithm:
1.  Initialize set to store elements as they're seen, previous, and current
pointers.
2. While current is not null
    2a. If the element at the current node is already in the set, delete that
    element from the linked list
    2b. If the element at the current node is not already in the set, store
    that element in the set and increment the previous pointer to meet the
    current pointer
3. Increment the current pointer and repeat the loop

Time Complexity: O(n) time and O(n) space

In Place Algorithm: CTCI asks how we would do this problem IN PLACE. In
place would be a two pointer approach moving one element at a time and
looking for occurances of that element and deleting them. Time complexity
would be O(n2) and O(1) space.
"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeDups(head):
    """
    Removes duplicate elements of an unsorted linked list.
    :param head:
    :return:
    """
    # store counter of elements in a single pass, if count is ever greater
    # than 1, delete it from the linked list

    element_set = set()  # set to store previously seen elements
    previous = None      # previous pointer, keep to allow for deletions
    current = head

    while current is not None:
        # check for duplicate
        if current.value in element_set:
            # point previous to current's next to delete current ele from list
            previous.next = current.next
        # haven't seen this element before
        else:
            # add element to set
            element_set.add(current.value)
            # point previous to current
            previous = current
        # increment current
        current = current.next


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end="->")
        current = current.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    print("remove duplicates")
    print_list(head)

    removeDups(head)
    print()
    print()

    print_list(head)
