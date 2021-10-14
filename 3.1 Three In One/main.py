"""
3.1 Three in One
Describe how you could use a single array to implement three stacks.

Solution 1 - Fixed Stack Size
Partition the array into 3 even sections, where the index before the next
parititon is each section's top. Set a size K.

May want the storage sizes to be more flexible. Use a circular array.
"""


class FixedMultiStack:
    """
    Divide the array into three equal parts and allow the individual stack
    to grow in the preset space. [ == inclusive, ( == exclusive
    Stack 1 [0, n/3)
    Stack 2 [n/3, 2n/3)
    Stack 3 [2n/3, n)
    """

    # creates an empty multistack of stacks of stack_size
    def __init__(self, stack_size, num_stacks):
        self.stack_capacity = stack_size
        self.num_stacks = num_stacks

        # Empty array of size stack_size * num_stacks
        self._theItems = [None] * (self.num_stacks * self.stack_capacity)
