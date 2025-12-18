"""
Module: main
------------
Entry point for testing and demonstrating doubly linked list (DLL) based stack
operations.

This script validates the behavior of the `DLLStack` abstraction implemented
using a doubly linked list and operational logic from `dll_stack_operations`.

It demonstrates standard LIFO semantics, boundary conditions, and stack state
transitions through push, pop, peek, and utility operations while leveraging
constant-time insertions and removals via head and tail node references.

Example:
    from stack.schemas import DLLStack

    if __name__ == "__main__":
        stack = DLLStack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        stack.print_stack()
        print(stack.pop())
        print(stack.peek())
        print(stack.size())
        stack.clear()

Output:
    -------------------------------------- Stack ---------------------------------------
	    Head → | 100 | ←→ | 200 | ←→ | 300 | ←→ | 400 | ←→ | 500 | ←→ | 600 | ← Tail
    ------------------------------------------------------------------------------------
	    Bottom → 100                                                       Top → 600
    ------------------------------------------------------------------------------------

Notes:
    - Designed for fast behavioral validation
    - Assumes the head node represents the top of the stack
    - Push and pop operations execute in O(1) time
    - Exception handling should be added for production use
"""

from stack.dll_stack.schemas import DLLStack

def main():
    dll = DLLStack()

    dll.push(100)
    dll.push(200)
    dll.push(300)
    dll.print_stack()

    print(f"Is dll stack is empty? -> {"Yes" if dll.is_empty() else "No"}")
    print(f"Size of stack -> {dll.size()}")
    print(f"Popped element is -> {dll.pop()}")
    dll.print_stack()
    print(f"Peek in stack: {dll.peek()}")
    dll.print_stack()
    dll.clear()
    print(f"Is dll stack is empty? -> {"Yes" if dll.is_empty() else "No"}")

if __name__ == '__main__':
    main()
