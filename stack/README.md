# Stack Implementations in Python

This document explains how a **Stack** can be implemented using three different
underlying data structures in Python:

1. Python **List**
2. `collections.deque`
3. **Doubly Linked List (DLL)**

The goal is to understand how the **same stack abstraction** is preserved while
the **internal implementation** changes, along with its trade-offs.

---

## Stack Concept (Quick Recap)

A **stack** is a linear data structure that follows the **LIFO** principle:

> **Last In, First Out**

All operations are performed at a single end called the **top** of the stack.

---

## Core Stack Operations

| Operation | Description |
|---------|-------------|
| `push` | Add an element to the top |
| `pop` | Remove and return the top element |
| `peek` | Return the top element without removing it |
| `is_empty` | Check whether the stack is empty |
| `size` | Return the number of elements |
| `clear` | Remove all elements |
| `print` | Display stack contents (bottom → top) |

---

## Implementation 1: Stack using Python List

### Key Characteristics
- Top of stack → **end of list**
- Uses Python’s built-in dynamic array
- Simple, fast, and memory-efficient

### Operation Mapping

| Stack Operation | List Method / Behavior |
|-----------------|------------------------|
| `push` | `list.append(x)` |
| `pop` | `list.pop()` |
| `peek` | `list[-1]` |
| `is_empty` | `len(list) == 0` |
| `size` | `len(list)` |
| `clear` | `list.clear()` |
| `print` | Iterate list from index `0 → -1` |

---
## Sample Output Representation
```python
--------------- Stack --------------------
    Bottom → | 100 | 300 | 400 | ← Top
------------------------------------------
    Bottom → 100             Top → 400
------------------------------------------
```

**Explanation**
- The end of the list/deque is treated as the stack top  
- Elements grow and shrink only from the right side  
- No explicit pointers are required  

**Visual Consistency**
- Bottom = first inserted element  
- Top = most recently inserted element  
- Output is for visualization only and does not affect stack behavior

---

## Implementation 2: Stack using `collections.deque`

### Key Characteristics
- Top of stack → **right end**
- Implemented internally as a block-linked list
- Efficient at both ends, future-proof if stack evolves

### Operation Mapping

| Stack Operation | Deque Method / Behavior |
|-----------------|------------------------|
| `push` | `deque.append(x)` |
| `pop` | `deque.pop()` |
| `peek` | `deque[-1]` |
| `is_empty` | `len(deque) == 0` |
| `size` | `len(deque)` |
| `clear` | `deque.clear()` |
| `print` | Iterate deque from left → right |

---
## Sample Output Representation
```python
--------------- Stack --------------------
    Bottom → | 100 | 300 | 400 | ← Top
------------------------------------------
    Bottom → 100             Top → 400
------------------------------------------
```

**Explanation**
- The end of the list/deque is treated as the stack top  
- Elements grow and shrink only from the right side  
- No explicit pointers are required  

**Visual Consistency**
- Bottom = first inserted element  
- Top = most recently inserted element  
- Output is for visualization only and does not affect stack behavior

---

## Implementation 3: Stack using Doubly Linked List (DLL)

### Key Characteristics
- Top of stack → **tail node**
- Explicit node management using `prev` and `next`
- Useful for understanding pointer-level operations

### Operation Mapping

| Stack Operation | DLL Behavior |
|-----------------|--------------|
| `push` | Insert node at `tail` |
| `pop` | Remove node from `tail` |
| `peek` | `tail.data` |
| `is_empty` | `head is None` |
| `size` | Maintained counter or traversal |
| `clear` | Set `head = tail = None` |
| `print` | Traverse from `head → tail` |

---
## Sample Output Representation
```python
---------------------- Stack ----------------------
    Head → | 100 | ←→ | 200 | ←→ | 300 | ← Tail    
---------------------------------------------------
    Bottom → 100                      Top → 300    
---------------------------------------------------
```
**Explanation**
- `Head` represents the bottom of the stack  
- `Tail` represents the top of the stack  
- Bidirectional arrows (`←→`) indicate `prev` / `next` links

---

## Summary Comparison

| Aspect | List | Deque | DLL |
|------|------|-------|-----|
| Push / Pop | O(1) amortized | O(1) | O(1) |
| Memory Overhead | Low | Medium | High |
| Implementation Complexity | Low | Low | High |
| Best Use Case | Simple stack | Flexible stack / queue | Pointer-based systems |

---

## Final Notes

- **Python List** is the best default choice for stacks.
- **Deque** is ideal when stack behavior may evolve into queue or deque usage.
- **Doubly Linked List** is mainly educational or used in advanced systems.

> The stack abstraction remains the same — only the storage strategy changes.
