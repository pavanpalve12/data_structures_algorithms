"""
------------------------------------------------------------------------------------
Module Name: deque_queue_schemas
------------------------------------------------------------------------------------

This module defines the public schema for a deque-based Queue implementation.

It exposes a lightweight Queue container whose responsibility is limited to:
- initializing and holding internal deque-based state
- defining the public queues interface
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
- This module contains no queues business logic
- All operational behavior is delegated to the operations layer
- Internal state is maintained via a single deque attribute
- The schema enforces a strict separation of interface and implementation

------------------------------------------------------------------------------------
"""

from collections import deque
from typing import Any
from queues.deque_queue.operations import deque_queue_operations

class DequeQueue:
    """
    DequeQueue represents a FIFO (First-In-First-Out) queues abstraction
    backed by a collections.deque instance.

    This class is responsible for:
    - initializing the internal deque storage
    - exposing the public queues interface
    - delegating all operational logic to the operations module

    No queues behavior is implemented directly in this class.

    Design Constraints:
    - The internal deque is treated as a protected structure
    - All queues operations must be executed via the operations layer
    - This class serves strictly as an interface and state holder
    """

    def __init__(self):
        """
        Initialize an empty deque-based queues instance.
        :return: None
        """
        self.queue = deque()

    # -------------- Queue Operations ----------------------------------------------------------
    def enqueue(self, data) -> bool:
        """
        Insert an element at the rear of the queues.
        :param data: Element to be added to the queues
        :return: Result of the enqueue operation
        """
        return deque_queue_operations.enqueue(self, data)

    def dequeue(self) -> Any:
        """
        Remove and return the front element of the queues.
        :return: The element removed from the front of the queues
        """
        return deque_queue_operations.dequeue(self)

    def peek(self) -> Any:
        """
        Return the front element of the queues without removing it.
        :return: The front element of the queues
        """
        return deque_queue_operations.peek(self)

    def is_empty(self) -> bool:
        """
        Check whether the queues is empty.
        :return: True if the queues is empty, False otherwise
        """
        return deque_queue_operations.is_empty(self)

    def size(self) -> int:
        """
        Return the number of elements currently in the queues.
        :return: Integer representing the queues size
        """
        return deque_queue_operations.size(self)

    def clear(self):
        """
        Remove all elements from the queues.
        :return: True if the queues is empty after clearing
        """
        return deque_queue_operations.clear(self)

    def print_queue(self):
        """
        Print the contents of the queues from front to rear.
        :return: None
        """
        return deque_queue_operations.print_queue(self)
