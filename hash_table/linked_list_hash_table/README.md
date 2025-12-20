# Hash Table Implementation Using List with Chaining (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular Hash Table implementation backed by a
Python list using chaining for collision resolution**, designed to clearly
demonstrate how hash tables work internally.

The implementation focuses on **core hash table mechanics**, including:
- hashing and index generation
- collision handling via chaining
- load factor tracking
- dynamic resizing and rehashing
- invariant-based correctness checks

The design mirrors **production-grade separation of concerns** by isolating:
- public interface and state (schemas)
- operational logic (operations)
- execution / validation (main)

This structure is ideal for understanding hash tables beyond Python’s built-in
`dict` abstraction.

------------------------------------------------------------------------------------

## Architecture

hash_table/
└── hash_table/
├── schemas.py      # HashTable schema and public interface (no logic)
├── operations.py   # Hash table operations (hashing, insert, resize, lookup)
└── main.py         # Entry point for testing and demonstration

---

------------------------------------------------------------------------------------

## Design Philosophy

- **Correctness before optimization**
- **Explicit collision handling via chaining**
- **No logic in container (schema) classes**
- **All behavior delegated to operations layer**
- **Invariant-driven development**
- **Resizing handled as a controlled rebuild**

This mirrors how real-world hash tables are implemented in systems and databases.

------------------------------------------------------------------------------------

## Data Structures

### HashTable

- Hash table abstraction backed by a list of buckets
- Each bucket is a linked list storing `(key, value)` pairs
- Handles collisions using **separate chaining**
- Tracks:
  - number of elements
  - table size
  - load factor
  - resize threshold

Buckets grow dynamically, ensuring correctness even under collisions.

------------------------------------------------------------------------------------

## Core Hash Table Operations

| Operation | Description |
|---------|-------------|
| `insert` | Insert or update a key-value pair |
| `lookup` | Retrieve value associated with a key |
| `delete` | Remove a key-value pair |
| `resize` | Expand table size and rehash entries |
| `get_index` | Compute index using hash(key) |
| `get_load_factor` | Compute load factor |

------------------------------------------------------------------------------------

## Collision Handling (Chaining)

- Multiple keys hashing to the same index are stored in a linked list bucket
- No overwriting occurs unless keys are identical
- Average-case operations remain **O(1)** with proper resizing

------------------------------------------------------------------------------------

## Resizing Strategy

- Load factor is monitored before each insertion
- Resize is triggered when projected load factor exceeds the threshold
- Table size is doubled
- All existing key-value pairs are **rehashed and reinserted**
- Invariants are validated after resize completion

This ensures sustained performance and correctness.

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines the `HashTable`, `LinkedList`, and `Node` structures
- Maintains internal state only
- Exposes dictionary-style interface (`__setitem__`, `__getitem__`, `__delitem__`)
- Delegates all logic to operations modules
- Contains **no hashing or collision logic**

### `operations.py`
- Implements hashing and index generation
- Handles insert, update, lookup, and delete
- Manages resizing and rehashing
- Enforces invariants to ensure correctness
- Contains optional debug and print utilities

### `main.py`
- Entry point for testing and demonstration
- Inserts sample data
- Prints internal table structure
- Validates lookup and overwrite behavior
- Intended for learning and validation, not production use

------------------------------------------------------------------------------------

## Example Usage

```python
from hash_table.schemas import HashTable

ht = HashTable()

ht["2025-12-20"] = 260.0
ht["2025-12-19"] = 180.5
ht["2025-12-18"] = 95.75

ht.print_hash_table()

print(ht["2025-12-20"])
del ht["2025-12-18"]
```

---

## Example Output

```text
============================= Hash Table =============================
Bucket 0 → (2025-12-18, 95.75) → None
Bucket 1 → (2025-12-19, 180.5) → None
Bucket 2 → None
Bucket 3 → (2025-12-20, 260.0) → None
Bucket 4 → None
---------------------------------------------------------------------
Hash Table Details:
Hash Function      → hash(key) = (∑ ascii(chars)) % table size
Num elements       → 3
Size of hash table → 5
Load Factor        → 0.60
=====================================================================
```

------------------------------------------------------------------------------------

## Notes

- Designed for **deep data-structure understanding**
- Emphasizes correctness and invariant enforcement
- Resizing is explicit and traceable
- More verbose than Python `dict`, but **far more educational**
- Suitable as a foundation for:
  - alternative hash functions
  - different collision strategies
  - performance experiments

------------------------------------------------------------------------------------
