"""
------------------------------------------------------------------------------------
Module Name: list_stack
------------------------------------------------------------------------------------

This module defines a List-based Stack implementation and its public interface.

It provides:
- a ListStack container backed by a native Python list
- a clean, minimal stack API following LIFO semantics
- delegation of all operational logic to a dedicated operations module

The design enforces a strict separation of concerns:
- the ListStack class exposes the public interface only
- all core stack logic is implemented in the list_stack_operations module
- internal state is maintained exclusively via a single list attribute

------------------------------------------------------------------------------------
Data Structure
------------------------------------------------------------------------------------
- ListStack -> Stack abstraction implemented using a Python list

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
- No stack logic is implemented directly in the ListStack class
- All operations are delegated to the operations layer for consistency
- The underlying list is treated as a protected internal structure
- The implementation prioritizes clarity, predictability, and correctness

------------------------------------------------------------------------------------
"""

from stack.list_stack.operations import list_stack_operations
from typing import Any
# ----------- Clas Stack using List ------------------------------------------------
class ListStack:
    def __init__(self):
        self.stack = []

    # ----------- stack operations ------------------------------------------------
    def push(self, data) -> bool:
        """
        Function: push data element at the top
        :param data: data to be pushed
        :return: True if data is pushed else False
        """
        return list_stack_operations.push(self, data)

    def pop(self) -> Any:
        """
        Function: remove the data element from top of stack
        :return: returns data element if successful else None/Error
        """
        return list_stack_operations.pop(self)

    def peek(self) -> Any:
        """
        Function: check the data value at the top of stack
        :return: data value at stack top
        """
        return list_stack_operations.peek(self)

    def is_empty(self) -> bool:
        """
        Function: check if stack is empty
        :return: True if stack is empty else False
        """
        return list_stack_operations.is_empty(self)

    def size(self) -> int:
        """
        Function: returns the size - length of stack
        :return: length of stack
        """
        return list_stack_operations.size(self)

    def clear(self) -> bool:
        """
        Function: removes all data elements from stack
        :return: True if stack is empty else False
        """
        return list_stack_operations.clear(self)

    def print_stack(self):
        """
        Function: prints the stack from bottom to top
        :return: Nothing
        """
        return list_stack_operations.print_stack(self)