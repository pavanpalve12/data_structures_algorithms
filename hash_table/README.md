# Hash Table Implementations in Python

This document explains how a **Hash Table** can be implemented using **two different
bucket strategies** while preserving the **same hash table abstraction**:

1. Hash Table using **Python List Buckets**
2. Hash Table using **Linked List Buckets (Chaining)**

The goal is to understand how **collision resolution strategies** affect internal
behavior, performance, and design complexity — without changing the public API.

---

## Hash Table Concept (Quick Recap)

A **hash table** is a data structure that maps **keys to values** using a
**hash function**.

Basic idea:

1. Compute an index using `hash(key)`
2. Store the key-value pair at that index
3. Handle collisions when multiple keys map to the same index

---

## Core Hash Table Operations

| Operation | Description |
|---------|-------------|
| `insert` | Insert or update a key-value pair |
| `lookup` | Retrieve value associated with a key |
| `delete` | Remove a key-value pair |
| `get_index` | Compute index using hash function |
| `resize` | Expand table size and rehash entries |
| `print` | Display internal table structure |

---

## Implementation 1: Hash Table using Python List Buckets

### Bucket Structure
- Each bucket is a **Python list**
- Collisions are handled by **appending to the list**
- Each bucket stores `(key, value)` tuples

### Key Characteristics
- Simple and easy to understand
- Uses Python’s built-in dynamic array
- Slightly higher overhead for tuple handling

### Operation Mapping

| Hash Operation | List-Based Behavior |
|---------------|---------------------|
| `insert` | Append `(key, value)` to bucket list |
| `lookup` | Linear search within bucket list |
| `delete` | Remove matching tuple |
| `resize` | Recreate table and reinsert tuples |

### Sample Output Representation
```
====================== Hash Table ======================
Bucket 0 → [('2025-12-18', 95.75)]
Bucket 1 → []
Bucket 2 → [('2025-12-20', 260.0)]
Bucket 3 → []
Bucket 4 → [('2025-12-19', 180.5)]
--------------------------------------------------------
Num elements → 3
Table size   → 5
Load Factor  → 0.60
========================================================
```

---

## Implementation 2: Hash Table using Linked List Buckets (Chaining)

### Bucket Structure
- Each bucket is a **singly linked list**
- Each node stores a `(key, value)` pair
- Collisions are handled by **node chaining**

### Key Characteristics
- Explicit pointer management
- Clear separation of structure and behavior
- Better control over invariants and memory layout
- Educational and closer to low-level implementations

### Operation Mapping

| Hash Operation | Linked List Behavior |
|---------------|----------------------|
| `insert` | Insert or overwrite node in bucket |
| `lookup` | Traverse linked list |
| `delete` | Remove node and relink |
| `resize` | Rehash all nodes into new buckets |

### Sample Output Representation
```
============================= Hash Table =============================
Bucket 0 → (2025-12-18, 95.75) → None
Bucket 1 → (2025-12-19, 180.5) → None
Bucket 2 → None
Bucket 3 → (2025-12-20, 260.0) → (2025-12-16, 310.25) → None
Bucket 4 → None
---------------------------------------------------------------------
Hash Table Details:
Hash Function      → hash(key) = (∑ ascii(chars)) % table size
Num elements       → 4
Size of hash table → 5
Load Factor        → 0.80
=====================================================================
```

---

## Project Structure

```
hash_table/
├── list_hash_table/
│   ├── schemas.py
│   ├── operations.py
│   └── main.py
│
└── linked_list_hash_table/
    ├── schemas.py
    ├── linked_list_operations.py
    ├── hash_operations.py
    └── main.py
```

---

## Comparison Summary

| Aspect | List Buckets | Linked List Buckets |
|------|-------------|---------------------|
| Collision Handling | List append | Node chaining |
| Insert Complexity | O(1)* | O(1)* |
| Lookup Complexity | O(n) in bucket | O(n) in bucket |
| Memory Overhead | Lower | Higher |
| Implementation Complexity | Low | Medium–High |
| Educational Value | Medium | High |
| Production Suitability | Acceptable | Common in systems |

\* Average case with good hash distribution.

---

## 🧠 Design Principles

- **Same abstraction, different internals**
- **No logic in schema/container classes**
- **All behavior delegated to operations layer**
- **Explicit invariant checks for correctness**
- **Controlled resizing with full rehash**

---

## 📝 Notes

- Designed for **deep data-structure understanding**
- Python list buckets are easier to reason about initially
- Linked list buckets closely resemble real-world hash table designs
- Both implementations share the **same conceptual API**
- Resizing logic is identical — only bucket mechanics differ

Easily extensible to:
- custom hash functions
- open addressing strategies
- tree-based buckets
- performance benchmarking
- thread-safe hash tables

---

> **One data structure. Two bucket strategies. Clear trade-offs.**
