"""
------------------------------------------------------------------------------------
Module Name: dll_stack
------------------------------------------------------------------------------------

This module defines a Doubly Linked List (DLL) based Stack implementation and its
public interface.

It provides:
- a DLLStack container backed by a doubly linked list
- a strict LIFO (Last-In-First-Out) stack abstraction
- a clean, minimal stack API
- full delegation of operational logic to a dedicated operations module

The design enforces a clear separation of concerns:
- the DLLStack class exposes only the public interface
- all core stack logic is implemented in the dll_stack_operations module
- internal state is maintained via explicit head and tail node references

------------------------------------------------------------------------------------
Data Structure
------------------------------------------------------------------------------------
- Node     -> Doubly linked list node containing data, next, and prev references
- DLLStack -> Stack abstraction implemented using a doubly linked list

------------------------------------------------------------------------------------
Core Stack Operations
------------------------------------------------------------------------------------
- push     -> Insert an element at the top of the stack
- pop      -> Remove and return the top element of the stack
- peek     -> Return the top element without removing it
- is_empty -> Check whether the stack is empty
- size     -> Return the number of elements in the stack
- clear    -> Remove all elements from the stack

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_stack -> Print stack contents from bottom to top

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- The stack follows strict LIFO semantics
- No stack logic is implemented directly in the DLLStack class
- All operations are delegated to the operations layer for consistency
- Head and tail pointers provide O(1) push and pop operations
- The implementation prioritizes correctness, clarity, and modularity

------------------------------------------------------------------------------------
"""

from stack.dll_stack.operations import dll_stack_operations

class Node:
    """
    Represents a node in a doubly linked list.

    Each node stores:
    - data : the value held by the node
    - next : reference to the next node in the list
    - prev : reference to the previous node in the list

    This node structure is used internally by the DLLStack
    to support constant-time stack operations.
    """

    def __init__(self, data):
        """
        Initialize a new doubly linked list node.

        Args:
            data: The value to be stored in the node
        """
        self.data = data
        self.next = None
        self.prev = None

class DLLStack:
    """
    Stack implementation based on a doubly linked list.

    This class exposes a public stack interface while delegating
    all operational logic to the dll_stack_operations module.

    Internal State:
    - head : reference to the top of the stack
    - tail : reference to the bottom of the stack

    The design ensures:
    - O(1) push and pop operations
    - strict LIFO behavior
    - clean separation between interface and logic
    """

    def __init__(self):
        """
        Initialize an empty stack.
        Both head and tail references are set to None.
        """
        self.head = None
        self.tail = None

    # --------------- Stack Operations --------------------------------------------------------
    def push(self, data):
        """
        Pushes an element onto the top of the stack.
        :param data: Value to be pushed onto the stack
        :type data: any
        :return: None
        """
        new_node = Node(data)
        return dll_stack_operations.insert_at_tail(self, new_node)

    def pop(self):
        """
        Removes and returns the top element of the stack.

        :return: Top element of the stack
        :rtype: any
        :raises IndexError: If the stack is empty
        """
        return dll_stack_operations.delete_at_tail(self)

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        :return: Top element of the stack
        :rtype: any
        :raises IndexError: If the stack is empty
        """
        return dll_stack_operations.get_data_at_tail(self)

    def is_empty(self):
        """
        Checks whether the stack is empty.

        :return: True if the stack is empty, False otherwise
        :rtype: bool
        """
        return dll_stack_operations.is_empty(self)

    def size(self):
        """
        Returns the number of elements in the stack.

        :return: Number of elements in the stack
        :rtype: int
        """
        return dll_stack_operations.size(self)

    def clear(self):
        """
        Removes all elements from the stack.

        :return: None
        """
        return dll_stack_operations.clear(self)

    def print_stack(self):
        """
        Prints the contents of the stack from bottom to top.

        :return: None
        """
        return dll_stack_operations.print_linked_list(self)

