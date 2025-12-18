"""
------------------------------------------------------------------------------------
Module Name: deque_queue_schemas
------------------------------------------------------------------------------------

This module defines the public schema for a deque-based Queue implementation.

It exposes a lightweight Queue container whose responsibility is limited to:
- initializing and holding internal deque-based state
- defining the public queue interface
- delegating all operational logic to the operations module

The underlying data structure is `collections.deque`, chosen for its efficient
O(1) insertion and removal from both ends.

------------------------------------------------------------------------------------
Data Structure
------------------------------------------------------------------------------------
- DequeQueue -> Queue abstraction implemented using collections.deque

------------------------------------------------------------------------------------
Public Queue Operations
------------------------------------------------------------------------------------
- enqueue -> Insert an element at the rear of the queue
- dequeue -> Remove and return the front element of the queue
- peek -> Return the front element without removing it
- is_empty -> Check whether the queue is empty
- size -> Return the number of elements in the queue
- clear -> Remove all elements from the queue

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_queue -> Print queue contents from front to rear

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- This module contains no queue business logic
- All operational behavior is delegated to the operations layer
- Internal state is maintained via a single deque attribute
- The schema enforces a strict separation of interface and implementation

------------------------------------------------------------------------------------
"""

from collections import deque
from typing import Any
from queue.deque_queue.operations import deque_queue_operations

class DequeQueue:
    """
    DequeQueue represents a FIFO (First-In-First-Out) queue abstraction
    backed by a collections.deque instance.

    This class is responsible for:
    - initializing the internal deque storage
    - exposing the public queue interface
    - delegating all operational logic to the operations module

    No queue behavior is implemented directly in this class.

    Design Constraints:
    - The internal deque is treated as a protected structure
    - All queue operations must be executed via the operations layer
    - This class serves strictly as an interface and state holder
    """

    def __init__(self):
        """
        Initialize an empty deque-based queue instance.
        :return: None
        """
        self.queue = deque()

    # -------------- Queue Operations ----------------------------------------------------------
    def enqueue(self, data) -> bool:
        """
        Insert an element at the rear of the queue.
        :param data: Element to be added to the queue
        :return: Result of the enqueue operation
        """
        return deque_queue_operations.enqueue(self, data)

    def dequeue(self) -> Any:
        """
        Remove and return the front element of the queue.
        :return: The element removed from the front of the queue
        """
        return deque_queue_operations.dequeue(self)

    def peek(self) -> Any:
        """
        Return the front element of the queue without removing it.
        :return: The front element of the queue
        """
        return deque_queue_operations.peek(self)

    def is_empty(self) -> bool:
        """
        Check whether the queue is empty.
        :return: True if the queue is empty, False otherwise
        """
        return deque_queue_operations.is_empty(self)

    def size(self) -> int:
        """
        Return the number of elements currently in the queue.
        :return: Integer representing the queue size
        """
        return deque_queue_operations.size(self)

    def clear(self):
        """
        Remove all elements from the queue.
        :return: True if the queue is empty after clearing
        """
        return deque_queue_operations.clear(self)

    def print_queue(self):
        """
        Print the contents of the queue from front to rear.
        :return: None
        """
        return deque_queue_operations.print_queue(self)
