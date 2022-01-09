"""
3.1 Three in One
Describe how you could use a single array to implement three stacks.

Solution 1 - Fixed Stack Size
Partition the array into 3 even sections, where the index before the next
parititon is each section's top. Set a size K.

May want the storage sizes to be more flexible. Use a circular array.
"""
from queue import Empty


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
        # Number of stacks to be contained in the single list _data
        self._NUM_STACKS = 3
        # Capacity of a single stack
        self._stack_capacity = stack_size
        # Array of size stack_size * num_stacks
        self._data = [None] * (num_stacks * self._stack_capacity)
        # Array of size num_stacks stores each stack's curr size
        self._sizes = [0] * (num_stacks + 1)
        # Array holds top indices for each stack
        self._tops = []

    def push(self, stack_num, value):
        """
        Adds the given value to the indicated stack. If stack is full,
        raises exception. Does not resize.

        :param stack_num: 1, 2, or 3
        :param value: int data to be stored
        :raises Exception
        """
        # Check that there is space to push an element.
        if self.is_full(stack_num):
            raise Exception("Stack is full")

        # Increment size of stack and then update the value at Top
        self._sizes[stack_num] += 1
        self._data[self.get_top_index(stack_num)] = value

    def pop(self, stack_num):
        """
        Removes and returns the value at the top of the given stack. If empty
        raises exception.

        :param stack_num: 1, 2, or 3
        :return: Exception
        """
        # Check if stack is empty
        if self.is_empty(stack_num):
            raise Empty('Stack is empty cannot pop')

        # Store top value and then overwrite it, decrement stack size
        top_val = self._data[self.get_top_index(stack_num)]
        self._data[self.get_top_index(stack_num)] = None
        self._sizes[stack_num] -= 1

        return top_val

    def peek(self, stack_num):
        """
        Returns the value at the top of the given stack. If empty
        raises exception.

        :param stack_num: 1, 2, or 3
        :return: Exception
        """
        # Check if stack is empty
        if self.is_empty(stack_num):
            raise Empty('Stack is empty cannot peek')

        # Store top value
        top_val = self._data[self.get_top_index(stack_num)]
        return top_val

    def show(self):
        print(self._data)
        print(self._sizes)

    def is_full(self, stack_num):
        """Return True if stack size equals stack capacity"""
        # Validate stack_num input
        if not 0 < stack_num <= self._NUM_STACKS:
            raise ValueError("Number of stacks must be between 1 and 3")
        return self._stack_capacity == self._sizes[stack_num]

    def is_empty(self, stack_num):
        """Return True if stack size equals stack capacity"""
        # Validate stack_num input
        if not 0 < stack_num <= self._NUM_STACKS:
            raise ValueError("Number of stacks must be between 1 and 3")

        if self._sizes[stack_num] != 0:
            return False

        return True

    def get_top_index(self, stack_num):
        """
        Returns the index of the current stop of a given stack.
        :param stack_num: 1, 2, or 3
        :return: int index
        """
        # Validate stack_num input
        if not 0 < stack_num <= self._NUM_STACKS:
            raise ValueError("Number of stacks must be between 1 and 3")
        # Calculate the index of the current top
        offset = stack_num * self._stack_capacity
        size = self._sizes[stack_num]
        return offset - size


if __name__ == "__main__":
    print('Multistack')
    myMultiStack = FixedMultiStack(3, 3)
    myMultiStack.show()
    myMultiStack.push(1, 1)
    myMultiStack.show()
    myMultiStack.push(1, 1)
    myMultiStack.show()
    myMultiStack.push(1, 1)
    myMultiStack.show()
    myMultiStack.pop(1)
    myMultiStack.pop(1)
    myMultiStack.show()





