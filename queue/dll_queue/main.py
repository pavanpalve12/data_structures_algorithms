"""
Module: main
------------
Entry point for testing and demonstrating a doubly linked list–based queue.

This script validates the behavior of the `DLLQueue` abstraction implemented
using a doubly linked list and operational logic from `dll_queue_operations`.

It demonstrates standard FIFO semantics, queue state transitions, and utility
operations including enqueue, dequeue, peek, size inspection, and clearing
the queue.

Example:
    from queue.dll_queue.schemas import DLLQueue

    if __name__ == "__main__":
        dll = DLLQueue()
        dll.enqueue(100)
        dll.enqueue(200)
        dll.enqueue(300)
        dll.print_queue()
Example output:
--------------------------------- Queue ---------------------------------
	Head → | 500 | ←→ | 400 | ←→ | 300 | ←→ | 200 | ←→ | 100 | ← Tail
-------------------------------------------------------------------------
	Rear → 500                                            Front → 100
-------------------------------------------------------------------------

Notes:
    - Designed for fast behavioral validation
    - Assumes DLL head represents the rear and DLL tail represents the front
    - Intended for learning and correctness verification, not production use
"""

from queue.dll_queue.schemas import DLLQueue


def main():
    """
    Execute a demonstration of DLLQueue operations.

    This function creates a doubly linked list–based queue instance and performs
    a sequence of enqueue, dequeue, peek, size, clear, and print operations to
    validate FIFO behavior and internal state transitions.

    :return: None
    """
    dll = DLLQueue()

    dll.enqueue(100)
    dll.enqueue(200)
    dll.enqueue(300)
    dll.enqueue(400)
    dll.enqueue(500)
    dll.print_queue()

    print(f"Is dll queue is empty? -> {'Yes' if dll.is_empty() else 'No'}")
    print(f"Size of queue -> {dll.get_size()}")
    print(f"Dequeued element is -> {dll.dequeue()}")
    dll.print_queue()
    print(f"Peek in queue: {dll.peek()}")
    dll.print_queue()
    dll.clear()
    print(f"Is dll queue is empty? -> {'Yes' if dll.is_empty() else 'No'}")
    dll.print_queue()


if __name__ == '__main__':
    main()
