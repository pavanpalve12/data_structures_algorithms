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

from stack.dll_stack.schemas import DLLStack, Node

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

"""
Manual DLL test
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400)
    n5 = Node(500)
    n6 = Node(600)

    n1.next, n1.prev = n2, None
    n2.next, n2.prev = n3, n1
    n3.next, n3.prev = n4, n2
    n4.next, n4.prev = n5, n3
    n5.next, n5.prev = n6, n4
    n6.next, n6.prev = None, n5

    dll.head, dll.tail = n1, n6
"""