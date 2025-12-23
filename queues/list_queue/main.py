"""
Module: main
------------
Entry point for testing and demonstrating list-based queues operations.

This script validates the behavior of the `ListQueue` abstraction implemented
using a Python list and operational logic from `queues.list_queue.operations`.

It demonstrates standard FIFO semantics, boundary conditions, and queues state
transitions through enqueue, dequeue, peek, and utility operations.

Example:
    from queues.list_queue.schemas import ListQueue

    if __name__ == "__main__":
        queues = ListQueue()
        queues.enqueue("A")
        queues.enqueue("B")
        queues.enqueue("C")
        queues.print_queue()
        print(queues.dequeue())
        print(queues.peek())
        print(queues.size())
        queues.clear()

Output:
    ---------------- Queue -------------------
        Front → | A | B | C | D | ← Rear
    ------------------------------------------
        Front → B                 Rear → D
    ------------------------------------------

Notes:
    - Designed for fast behavioral validation
    - Assumes list head represents the front of the queues
    - Exception handling should be added for production use
"""

from queues.list_queue.schemas import ListQueue


def main():
    """
    Execute a demonstration of ListQueue operations.

    This function creates a queues instance and performs a sequence of
    enqueue, dequeue, peek, size, clear, and print operations to validate
    FIFO behavior and state transitions.

    :return: None
    """
    lq = ListQueue()

    lq.enqueue('A')
    lq.enqueue('B')
    lq.enqueue('C')
    lq.enqueue('D')
    lq.print_queue()

    print(f"Is queues is empty ? -> {lq.is_empty()}")
    print(f"Dequeued element from front -> {lq.dequeue()}")
    print(f"Peeked element at front -> {lq.peek()}")
    print(f"Size of queues is -> {lq.size()}")
    lq.print_queue()
    print(f"Queue is cleared -> {'Yes' if lq.clear() else 'No'}")
    lq.print_queue()


if __name__ == '__main__':
    main()
