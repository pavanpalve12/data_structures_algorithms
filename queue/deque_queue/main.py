"""
Module: main
------------
Entry point for testing and demonstrating deque-based queue operations.

This script is intended to validate the behavior of the DequeQueue abstraction
implemented using `collections.deque` and operational logic from the
deque_queue_operations module.

It demonstrates FIFO semantics, queue state transitions, and utility operations
in a controlled, non-production context.

Example:
    from queue.deque_queue.schemas import DequeQueue

    if __name__ == "__main__":
        queue = DequeQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.print_queue()
Sample Output:
---------------- Queue -----------------
	Front → | A | B | C | D | ← Rear
----------------------------------------
	Front → A               Rear → D
----------------------------------------

Notes:
    - Designed for fast behavioral validation
    - Assumes deque head represents the front of the queue
    - Placeholder implementation only
    - Exception handling to be added during implementation
"""

from queue.deque_queue.schemas import DequeQueue
def main():
    """
    Entry point for testing and demonstrating deque-based queue operations.
    This function simulates enqueue, dequeue, peek,
    size, clear, and print operations for the DequeQueue abstraction.
    :return: None
    """
    dq = DequeQueue()

    dq.enqueue('A')
    dq.enqueue('B')
    dq.enqueue('C')
    dq.enqueue('D')
    dq.print_queue()

    print(f"Is queue is empty ? -> {dq.is_empty()}")
    print(f"Dequeued element from front -> {dq.dequeue()}")
    print(f"Peeked element at front -> {dq.peek()}")
    print(f"Size of queue is -> {dq.size()}")
    dq.print_queue()
    print(f"Queue is cleared -> {'Yes' if dq.clear() else 'No'}")
    dq.print_queue()


if __name__ == "__main__":
    main()
