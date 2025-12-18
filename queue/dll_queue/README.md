# Doubly Linked List–Based Queue Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular Queue implementation backed by a
Doubly Linked List (DLL)**, designed to clearly demonstrate low-level queue
mechanics and pointer-based data structure behavior.

The implementation follows **FIFO (First-In-First-Out)** semantics and mirrors
production-grade design principles by isolating:
- public interface (schemas)
- operational logic (operations)
- execution / validation (main)

This structure is ideal for understanding how queues work internally without
relying on Python’s built-in containers.

------------------------------------------------------------------------------------

## Architecture

queue/
└── dll_queue/
├── schemas.py      # Queue schema and node definitions (no logic)
├── operations.py   # Doubly linked list queue behavior
└── main.py         # Entry point for testing and demonstration

---

------------------------------------------------------------------------------------

## Design Philosophy

- **FIFO correctness first**
- **Explicit pointer management**
- **No logic in container classes**
- **All behavior delegated to operations layer**
- **Internal state managed via linked nodes and size tracking**

This mirrors how low-level systems implement queues in languages like C/C++.

------------------------------------------------------------------------------------

## Data Structures

### Node

- Represents a single element in a doubly linked list
- Stores data and bidirectional links (`prev` and `next`)
- Used internally by the queue implementation

### DLLQueue

- Queue abstraction implemented using a doubly linked list
- Enqueue inserts at the **rear**
- Dequeue removes from the **front**
- Maintains internal state via head/tail references and size tracking

> **Note:** In this implementation,  
> **DLL head = Rear** and **DLL tail = Front**

------------------------------------------------------------------------------------

## Core Queue Operations

| Operation | Description |
|---------|-------------|
| `enqueue` | Insert an element at the rear of the queue |
| `dequeue` | Remove and return the front element |
| `peek` | Return the front element without removing it |
| `is_empty` | Check whether the queue is empty |
| `size` | Return the number of elements in the queue |
| `clear` | Remove all elements from the queue |

------------------------------------------------------------------------------------

## Utility / Output Operations

| Operation | Description |
|---------|-------------|
| `print_queue` | Print queue contents from rear to front with labels |

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines `Node` and `DLLQueue`
- Holds internal state (head, tail, size)
- Exposes public queue methods
- Delegates all logic to `operations.py`
- Contains **no business logic**

### `operations.py`
- Implements all queue behavior using pointer manipulation
- Enforces FIFO semantics
- Maintains size consistency
- Handles traversal and utility output

### `main.py`
- Entry point for testing and demonstration
- Validates FIFO behavior and state transitions
- Intended for fast behavioral verification
- Not designed for production use

------------------------------------------------------------------------------------

## Example Usage

```python
from queue.dll_queue.schemas import DLLQueue

queue = DLLQueue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
queue.enqueue(500)

queue.print_queue()
print(queue.dequeue())
print(queue.peek())
print(queue.size())
queue.clear()
```
---
## Example Output
```python
--------------------------------- Queue ---------------------------------
    Head → | 500 | ←→ | 400 | ←→ | 300 | ←→ | 200 | ←→ | 100 | ← Tail
-------------------------------------------------------------------------
    Rear → 500                                            Front → 100
-------------------------------------------------------------------------

```
---
### Notes

- Designed for **deep data-structure understanding**
- Pointer correctness is critical — **invariants must be preserved**
- Size is tracked explicitly for **O(1) access**
- More verbose than list/deque, but **more educational**

Easily extensible to:
- canonical **head-front / tail-rear** design
- **thread-safe** queues
- **circular doubly linked** queues
---

You now have **three fully aligned README files**:
- List-based Queue
- Deque-based Queue
- DLL-based Queue

If you want next:
- a **top-level README** comparing all three
- Big-O and memory comparison table
- or a unified Queue interface contract

Just say it.
---