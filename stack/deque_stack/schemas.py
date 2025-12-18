"""
------------------------------------------------------------------------------------
Module Name: deque_stack
------------------------------------------------------------------------------------

This module defines a stack implementation backed by `collections.deque`
and its public interface.

It provides:
- a DequeStack container backed by Python’s `collections.deque`
- a clean, minimal stack API following strict LIFO semantics
- delegation of all operational logic to a dedicated operations module

The design enforces a strict separation of concerns:
- the DequeStack class exposes the public interface only
- all core stack logic is implemented in the deque_stack_operations module
- internal state is maintained exclusively via a single deque instance

------------------------------------------------------------------------------------
Data Structure
------------------------------------------------------------------------------------
- DequeStack -> Stack abstraction implemented using collections.deque

------------------------------------------------------------------------------------
Core Stack Operations
------------------------------------------------------------------------------------
- push -> Insert an element at the top of the stack
- pop -> Remove and return the top element of the stack
- peek -> Return the top element without removing it
- is_empty -> Check whether the stack is empty
- size -> Return the number of elements in the stack
- clear -> Remove all elements from the stack

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_stack -> Print stack contents from bottom to top

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- The stack follows strict LIFO (Last-In-First-Out) behavior
- `collections.deque` is chosen for O(1) append and pop operations
- No stack logic is implemented directly in the DequeStack class
- All operations are delegated to the operations layer for consistency
- The underlying deque is treated as a protected internal structure
- The implementation favors performance, clarity, and correctness

------------------------------------------------------------------------------------
"""

from collections import deque
from stack.deque_stack.operations import deque_stack_operations


class DequeStack:
    """
    DequeStack implements a stack abstraction using `collections.deque`
    as the underlying storage container.

    The class exposes a minimal public API that follows strict
    LIFO (Last-In-First-Out) semantics while delegating all operational
    logic to the `deque_stack_operations` module.

    This design keeps the container lightweight and ensures a clean
    separation between interface and implementation.
    """

    def __init__(self):
        """
        Initialize an empty stack backed by a deque.

        A new deque instance is created for every DequeStack object,
        ensuring no shared state between stack instances.
        """
        self.stack = deque()

    # ----------- stack operations --------------------------------------------

    def push(self, data) -> bool:
        """
        Push a data element onto the top of the stack.

        :param data: Data element to be pushed
        :return: True if the push operation succeeds, False otherwise
        """
        return deque_stack_operations.push(self, data)

    def pop(self):
        """
        Remove and return the top element from the stack.

        :return: Top data element if stack is not empty, otherwise None
        """
        return deque_stack_operations.pop(self)

    def peek(self):
        """
        Return the top element of the stack without removing it.

        :return: Top data element if stack is not empty, otherwise None
        """
        return deque_stack_operations.peek(self)

    def is_empty(self) -> bool:
        """
        Check whether the stack is empty.

        :return: True if stack is empty, False otherwise
        """
        return deque_stack_operations.is_empty(self)

    def size(self) -> int:
        """
        Return the number of elements currently in the stack.

        :return: Integer size of the stack
        """
        return deque_stack_operations.size(self)

    def clear(self) -> bool:
        """
        Remove all elements from the stack.

        :return: True if stack is empty after clearing, False otherwise
        """
        return deque_stack_operations.clear(self)

    def print_stack(self) -> None:
        """
        Print the stack contents from bottom to top.

        :return: None
        """
        return deque_stack_operations.print_stack(self)


