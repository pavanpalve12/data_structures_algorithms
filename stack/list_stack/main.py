"""
Module: main
------------
Entry point for testing and demonstrating list-based stack operations.

This script validates the behavior of the `ListStack` abstraction implemented
using a Python list and operational logic from `stack.operations`.

It demonstrates standard LIFO semantics, boundary conditions, and stack state
transitions through push, pop, peek, and utility operations.

Example:
    from stack.schemas import ListStack

    if __name__ == "__main__":
        stack = ListStack()
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
	Bottom → | 100 | 300 | 400 | ← Top
------------------------------------------
	Bottom → 100 & Top → 400
------------------------------------------

Notes:
    - Designed for fast behavioral validation
    - Assumes list tail represents the top of the stack
    - Exception handling should be added for production use
"""

from stack.list_stack.schemas import ListStack

def main():
    ls = ListStack()

    ls.push(100)
    ls.push(200)
    ls.push(300)
    ls.push(400)
    ls.push(500)
    ls.print_stack()

    print(f"Is stack empty? -> {ls.is_empty()}.")
    print(f"Element popped from the top of stack is {ls.pop()}.")
    ls.print_stack()
    print(f"Element at the top of stack is {ls.peek()}.")
    ls.print_stack()
    print(f"Size of the stack is {ls.size()}.")
    ls.clear()
    print(f"Is stack empty? -> {ls.is_empty()}.")
    ls.print_stack()

if __name__ == '__main__':
    main()