"""
------------------------------------------------------------------------------------
Module Name: list_queue
------------------------------------------------------------------------------------

This module defines a List-based Queue implementation and its public interface.

It provides:
- a ListQueue container backed by a native Python list
- a clean, minimal queues API following FIFO semantics
- delegation of all operational logic to a dedicated operations module

The design enforces a strict separation of concerns:
- the ListQueue class exposes the public interface only
- all core queues logic is implemented in the list_queue_operations module
- internal state is maintained exclusively via a single list attribute

------------------------------------------------------------------------------------
Data Structure
------------------------------------------------------------------------------------
- ListQueue -> Queue abstraction implemented using a Python list

------------------------------------------------------------------------------------
Core Queue Operations
------------------------------------------------------------------------------------
- enqueue -> Insert an element at the rear of the queues
- dequeue -> Remove and return the front element of the queues
- peek -> Return the front element without removing it
- is_empty -> Check whether the queues is empty
- size -> Return the number of elements in the queues
- clear -> Remove all elements from the queues

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_queue -> Print queues contents from front to rear

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- The queues follows strict FIFO (First-In-First-Out) behavior
- No queues logic is implemented directly in the ListQueue class
- All operations are delegated to the operations layer for consistency
- The underlying list is treated as a protected internal structure
- The implementation prioritizes clarity, predictability, and correctness

------------------------------------------------------------------------------------
"""

from queues.list_queue.operations import list_queue_operations


class ListQueue:
    def __init__(self):
        """
        Initialize an empty queues instance.

        :return: None
        """
        self.queue = []

# -------------- Queue Operations --------------------------------------------------------------
    def enqueue(self, data):
        """
        Add an element to the rear of the queues.

        :param data: Element to be inserted into the queues
        :return: Result of the enqueue operation
        """
        return list_queue_operations.enqueue(self, data)

    def dequeue(self):
        """
        Remove and return the front element of the queues.

        :return: The element removed from the front of the queues
        """
        return list_queue_operations.dequeue(self)

    def is_empty(self):
        """
        Check whether the queues is empty.

        :return: True if the queues is empty, False otherwise
        """
        return list_queue_operations.is_empty(self)

    def clear(self):
        """
        Remove all elements from the queues.

        :return: None
        """
        return list_queue_operations.clear(self)

    def peek(self):
        """
        Return the front element of the queues without removing it.

        :return: The front element of the queues
        """
        return list_queue_operations.peek(self)

    def size(self):
        """
        Return the number of elements currently in the queues.

        :return: Integer representing the queues size
        """
        return list_queue_operations.size(self)

    def print_queue(self):
        """
        Print the contents of the queues from front to rear.

        :return: None
        """
        return list_queue_operations.print_queue(self)
