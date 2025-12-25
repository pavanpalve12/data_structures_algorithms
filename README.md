# 🧠 Data Structures & Algorithms (DSA) – Python Implementation

A clean, modular, and well-documented repository for mastering **Data Structures and Algorithms** in Python.  
Each data structure is implemented from scratch with **production-style architecture**, clear docstrings, and executable examples.

This repository emphasizes **correctness, invariants, and separation of concerns**, rather than relying on Python built-ins as black boxes.

---

## 🚀 Features

### 🔹 Common Data Structures

- **Linked Lists**  
  Linear data structures composed of nodes connected via pointers.  
  Implementations focus on pointer correctness, cycle safety, and size tracking.

- **Stacks & Queues**  
  Abstract data types following *LIFO* and *FIFO* principles.  
  Implemented using lists, deques, and linked lists to demonstrate trade-offs.

- **Trees (Generic N-ary Tree)**  
  Hierarchical data structure with explicit parent–child relationships.  
  Implemented as a **linked, invariant-checked generic tree** supporting any number of children per node.

- **Graphs**  
  Collection of vertices connected by edges.  
  Suitable for modeling networks, dependencies, and traversal algorithms.

- **Hash Tables**  
  Key–value mapping using hashing techniques.  
  Implementations cover collision handling, resizing, and invariant enforcement.

---

### ⚙️ Core Algorithms

- **Sorting Algorithms**  
  Merge Sort, Quick Sort, Bubble Sort, Insertion Sort.  
  Demonstrates time–space trade-offs and algorithmic complexity.

- **Searching Algorithms**  
  Linear Search and Binary Search.  
  Foundations for efficient data retrieval.

- **Recursion & Backtracking**  
  Core problem-solving techniques used extensively in trees and graphs.

- **Graph Algorithms**  
  BFS, DFS, Dijkstra’s Algorithm, Topological Sort.

- **Dynamic Programming**  
  Optimization over recursive solutions (e.g., Fibonacci, knapsack, grid paths).

---

### 🧩 Additional Highlights

- **Fully modular architecture** — schemas, operations, helpers, APIs  
- **Invariant-driven design** — correctness enforced explicitly  
- **Readable, testable code** — no hidden magic  
- **Multiple implementations per structure** — understand trade-offs  
- **Educational-first** — ideal for interviews and deep learning  

---

## 🧱 Current Implementations

| Data Structure | Status | Highlights |
|----------------|--------|------------|
| **Singly Linked List** | ✅ Complete | Modular, cycle-safe, invariant-checked |
| **Doubly Linked List** | ✅ Complete | Explicit prev/next pointers |
| **Stack (List-based)** | ✅ Complete | Simple, learning-focused |
| **Stack (Deque-based)** | ✅ Complete | O(1) push/pop, production-aligned |
| **Stack (DLL-based)** | ✅ Complete | Pointer-driven, invariant-checked |
| **Queue (List-based)** | ✅ Complete | FIFO via list, dequeue-cost awareness |
| **Queue (Deque-based)** | ✅ Complete | Optimal FIFO |
| **Queue (DLL-based)** | ✅ Complete | Explicit head/tail control |
| **Hash Table (List Buckets)** | ✅ Complete | Chaining, resize-aware |
| **Hash Table (Linked List Buckets)** | ✅ Complete | Node-based buckets |
| **Generic Tree (N-ary)** | ✅ **Complete** | Parent pointers, DFS/BFS, invariants |
| **Binary Tree / BST** | ✅ **Complete** | Parent pointers, DFS/BFS, invariants  |
| **Graphs** | ⏳ Planned | Adjacency list & matrix |

---

## 🌳 Generic Tree (N-ary Tree)

The repository includes a **Generic (N-ary) Tree** implementation designed to expose how trees work internally.

### Key Characteristics
- Linked, node-based structure
- Explicit `parent` and `children` references
- Supports **any number of children per node**
- Strict invariant enforcement:
  - single root
  - exactly one parent per non-root node
  - full connectivity
  - no cycles
  - `edges = nodes - 1`

### Supported Operations
- Insert and delete subtrees
- Search by value (BFS)
- DFS preorder and postorder traversals
- BFS (level-order) traversal
- Height (levels / edges)
- Depth of a node
- Size (node count)
- Human-readable BFS printing

### Structure
```
generic_tree/
├── schemas.py      # Node & Tree (state only)
├── operations.py   # Insert, delete, search, DFS/BFS
├── helpers.py      # Invariants, height, depth, size, printing
├── tree_api.py     # Public facade
└── main.py         # Examples & demos
```

This implementation is intentionally verbose and explicit to aid learning and correctness.

---

## 🧩 Getting Started

```bash
# Clone the repo
git clone https://github.com/pavanpalve12/data_structures_algorithms
cd dsa

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

## 🎯 Who This Repo Is For

- Learners who want to **understand data structures, not memorize them**
- Engineers preparing for **DSA interviews**
- Developers interested in **clean architecture & invariants**
- Anyone who wants to see how structures work *under the hood*

---

## 📌 Notes

- This repo favors **clarity over cleverness**
- Python built-ins are avoided where they hide structure
- Code is written to be read, reasoned about, and extended

---
