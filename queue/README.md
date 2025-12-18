# Queue Implementations in Python

This document explains how a **Queue** can be implemented using three different
underlying data structures in Python:

1. Python **List**
2. `collections.deque`
3. **Doubly Linked List (DLL)**

The goal is to understand how the **same queue abstraction** is preserved while
the **internal implementation** changes, along with its trade-offs.

---

## Queue Concept (Quick Recap)

A **queue** is a linear data structure that follows the **FIFO** principle:

> **First In, First Out**

Elements are:
- **added** at the **rear**
- **removed** from the **front**

---

## Core Queue Operations

| Operation | Description |
|---------|-------------|
| `enqueue` | Add an element to the rear |
| `dequeue` | Remove and return the front element |
| `peek` | Return the front element without removing it |
| `is_empty` | Check whether the queue is empty |
| `size` | Return the number of elements |
| `clear` | Remove all elements |
| `print` | Display queue contents (front → rear) |

---

## Implementation 1: Queue using Python List

### Key Characteristics
- Rear of queue → **end of list**
- Front of queue → **start of list**
- Simple and intuitive, but dequeue is expensive

### Operation Mapping

| Queue Operation | List Method / Behavior |
|-----------------|------------------------|
| `enqueue` | `list.append(x)` |
| `dequeue` | `list.pop(0)` |
| `peek` | `list[0]` |
| `is_empty` | `len(list) == 0` |
| `size` | `len(list)` |
| `clear` | `list.clear()` |
| `print` | Iterate list from index `0 → -1` |

### Sample Output Representation
```
---------------- Queue -----------------
    Front → | A | B | C | D | ← Rear
----------------------------------------
    Front → A               Rear → D
----------------------------------------
```

---

## Implementation 2: Queue using `collections.deque`

### Key Characteristics
- Rear of queue → **right end**
- Front of queue → **left end**
- Optimized for insertions and removals at both ends

### Operation Mapping

| Queue Operation | Deque Method / Behavior |
|-----------------|------------------------|
| `enqueue` | `deque.append(x)` |
| `dequeue` | `deque.popleft()` |
| `peek` | `deque[0]` |
| `is_empty` | `len(deque) == 0` |
| `size` | `len(deque)` |
| `clear` | `deque.clear()` |
| `print` | Iterate deque from left → right |

### Sample Output Representation
```
---------------- Queue -----------------
    Front → | A | B | C | D | ← Rear
----------------------------------------
    Front → A               Rear → D
----------------------------------------
```

---

## Implementation 3: Queue using Doubly Linked List (DLL)

### Key Characteristics
- Rear of queue → **DLL head**
- Front of queue → **DLL tail**
- Explicit pointer management using `prev` and `next`
- Size tracked explicitly for O(1) access

### Operation Mapping

| Queue Operation | DLL Behavior |
|-----------------|--------------|
| `enqueue` | Insert node at `head` (rear) |
| `dequeue` | Remove node from `tail` (front) |
| `peek` | `tail.data` |
| `is_empty` | `head is None` |
| `size` | Maintained counter |
| `clear` | Set `head = tail = None` |
| `print` | Traverse from `head → tail` |

### Sample Output Representation
```
--------------------------------- Queue ---------------------------------
    Head → | 500 | ←→ | 400 | ←→ | 300 | ←→ | 200 | ←→ | 100 | ← Tail
-------------------------------------------------------------------------
    Rear → 500                                            Front → 100
-------------------------------------------------------------------------
```

---

## Project Structure

```
queue/
├── list_queue/
│   ├── schemas.py
│   ├── operations.py
│   └── main.py
│
├── deque_queue/
│   ├── schemas.py
│   ├── operations.py
│   └── main.py
│
└── dll_queue/
    ├── schemas.py
    ├── operations.py
    └── main.py
```

---

## Summary Comparison

| Aspect | List | Deque | DLL |
|------|------|-------|-----|
| Enqueue | O(1) | O(1) | O(1) |
| Dequeue | O(n) | O(1) | O(1) |
| Memory Overhead | Low | Medium | High |
| Implementation Complexity | Low | Low | High |
| Best Use Case | Learning | Production | Internals / Education |

---

## 🧠 Key Design Principles

- **FIFO correctness first**
- **No logic in container classes**
- **All behavior delegated to operations layer**
- **Consistent API across implementations**
- **Clear documentation and enforced invariants**

---

## 📝 Notes

- Designed for **deep data-structure understanding**
- Python list queue is intentionally included despite inefficiency
- `collections.deque` is the **recommended real-world choice**
- DLL queue emphasizes **pointer correctness and invariants**
- Size is tracked explicitly where applicable for **O(1) access**

Easily extensible to:
- canonical **head-front / tail-rear** DLL design
- **thread-safe** queues
- **async** queues
- **circular doubly linked** queues
- **priority** queues

---

> **Same abstraction. Three implementations. Clear trade-offs.**
