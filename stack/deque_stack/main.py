"""
Module: main
------------
Entry point for testing and demonstrating deque-based stack operations.

This script validates the behavior of the `DequeStack` abstraction implemented
using Python’s `collections.deque` and operational logic from `stack.operations`.

It demonstrates standard LIFO semantics, boundary conditions, and stack state
transitions through push, pop, peek, and utility operations while leveraging
deque’s O(1) append and pop performance characteristics.

Example:
    from stack.schemas import DequeStack

    if __name__ == "__main__":
        stack = DequeStack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        stack.print_stack()
        print(stack.pop())
        print(stack.peek())
        print(stack.size())
        stack.clear()

Output:
    --------------- Stack ------------------
    Bottom → | 10 | 20 | 30 | ← Top
    ---------------------------------------
    Bottom → 10 & Top → 30
    ---------------------------------------

Notes:
    - Designed for fast behavioral validation
    - Assumes deque right end represents the top of the stack
    - `collections.deque` provides O(1) push and pop operations
    - Exception handling should be added for production use
"""

from stack.deque_stack.schemas import DequeStack
from collections import deque

def main():
    ds = DequeStack()

    ds.push(100)
    ds.push(200)
    ds.push(300)
    ds.push(400)
    ds.push(500)
    ds.print_stack()

    print(f"Is stack empty? -> {ds.is_empty()}.")
    print(f"Element popped from the top of stack is {ds.pop()}.")
    ds.print_stack()
    print(f"Element at the top of stack is {ds.peek()}.")
    ds.print_stack()
    print(f"Size of the stack is {ds.size()}.")
    ds.clear()
    print(f"Is stack empty? -> {ds.is_empty()}.")
    ds.print_stack()

if __name__ == '__main__':
    main()