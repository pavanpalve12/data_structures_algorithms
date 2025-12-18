# Stack Implementations – Modular Design (DLL-Based Stack)

## Overview
This repository demonstrates a **clean, modular stack architecture** with a strict
separation between **public interfaces** and **operational logic**.

The primary focus is a **Doubly Linked List (DLL)–based stack** that enforces
**LIFO (Last-In-First-Out)** semantics while maintaining predictable performance
characteristics and a disciplined code structure.

All stack behavior is delegated to a dedicated operations layer, keeping the
stack container lightweight and consistent across implementations.

---

## Architecture
The design follows a **three-layer structure**:

1. **Schema / Interface Layer**
   - Exposes the public stack API
   - Holds stack state only (`head`, `tail`)
   - Contains zero business logic

2. **Operations Layer**
   - Implements all stack behavior
   - Operates directly on stack internals
   - Enforces invariants and error handling

3. **Entry Point (main)**
   - Used for behavioral validation
   - Demonstrates stack state transitions
   - Not intended for production use

---

## Data Structures

### Node
A doubly linked list node containing:
- `data` – stored value
- `next` – reference to the next node
- `prev` – reference to the previous node

### DLLStack
A stack abstraction implemented using a doubly linked list.

Internal state:
- `head` – top of the stack
- `tail` – bottom of the stack

This structure guarantees **O(1)** push and pop operations.

---

## Core Stack Operations
The following operations are exposed by `DLLStack` and implemented in
`dll_stack_operations`:

- `push(data)` – Insert an element at the top of the stack
- `pop()` – Remove and return the top element
- `peek()` – Return the top element without removing it
- `is_empty()` – Check whether the stack is empty
- `size()` – Return the number of elements in the stack
- `clear()` – Remove all elements from the stack

---

## Utility Operations
- `print_stack()` – Prints stack contents from bottom to top

This function is intended for debugging and validation only.

---

## Design Principles
- **Strict LIFO semantics**
- **Zero logic in the stack container**
- **All behavior delegated to operations modules**
- **Constant-time stack operations**
- **Clear contracts via docstrings**
- **Predictable and testable structure**

---

## Example Usage

```python
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
```
---
## Performance Characteristics

- **Push:** O(1)
- **Pop:** O(1)
- **Peek:** O(1)
- **Space Complexity:** O(n)

---

## Notes

- The operations module currently contains placeholders and must be implemented
  to enable full functionality.
- Exception handling is minimal and intentionally left open for extension.
- This architecture is designed to scale cleanly to other stack backends
  (list, deque, array, etc.) without altering the public interface.

---

## Intended Audience

- Developers learning data structure design
- Engineers enforcing clean architecture and separation of concerns
- Anyone validating stack behavior without framework overhead
---