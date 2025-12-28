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
## 🧱 Current Implementations — Unified Summary

| Data Structure | Status | Description | Supported Operations |
|---------------|--------|-------------|----------------------|
| **Singly Linked List** | ✅ Complete | Linear list with next-pointer only | Insert (head/tail), Delete, Search, Traverse, Cycle detection |
| **Doubly Linked List** | ✅ Complete | Linear list with prev & next pointers | Insert, Delete, Forward/Backward traversal, Search |
| **Stack (List-based)** | ✅ Complete | LIFO stack using Python list | Push, Pop, Peek, Is empty |
| **Stack (Deque-based)** | ✅ Complete | LIFO stack using `collections.deque` | Push, Pop, Peek, Is empty |
| **Stack (DLL-based)** | ✅ Complete | Stack using doubly linked list | Push, Pop, Peek, Invariant checks |
| **Queue (List-based)** | ✅ Complete | FIFO queue using Python list | Enqueue, Dequeue, Peek, Is empty |
| **Queue (Deque-based)** | ✅ Complete | FIFO queue using `collections.deque` | Enqueue, Dequeue, Peek, Is empty |
| **Queue (DLL-based)** | ✅ Complete | Queue using doubly linked list | Enqueue, Dequeue, Peek, Invariant checks |
| **Hash Table (List Buckets)** | ✅ Complete | Hash table with list-based chaining | Insert, Lookup, Delete, Resize handling |
| **Hash Table (Linked List Buckets)** | ✅ Complete | Hash table with linked-list chaining | Insert, Lookup, Delete, Bucket traversal |
| **Generic Tree (N-ary)** | ✅ Complete | Tree with multiple children per node | Insert, Delete, BFS, DFS, Parent tracking, Invariants |
| **Binary Tree / BST** | ✅ Complete | Binary tree with BST ordering rules | Insert, Delete, Search, BFS, DFS, Height, Depth, Size |
| **Graph (Undirected, Unweighted)** | ✅ Complete | Adjacency-list graph with bidirectional edges | Insert/Remove vertex & edge, BFS, DFS, Components, Cycle detection |
| **Graph (Directed)** | ✅ Complete | Graph with one-way edges | Insert/Remove vertex & edge, BFS, DFS, Indegree/Outdegree |
| **Graph (DAG)** | ⏳ Planned | Directed acyclic graph | Topological sort, Cycle check, Path queries |
| **Graph (Weighted)** | ⏳ Planned | Graph with edge weights | Shortest paths, Weighted traversal |

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
