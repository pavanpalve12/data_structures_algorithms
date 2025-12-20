# 🧠 Data Structures & Algorithms (DSA) – Python Implementation

A clean, modular, and well-documented repository for mastering **Data Structures and Algorithms** in Python.  
Each data structure is implemented from scratch with production-style code organization, clear docstrings, and testable examples.
---

## 🚀 Features

### 🔹 Common Data Structures
- **Linked Lists**  
  Linear data structure consisting of nodes connected via pointers.  
  Efficient for insertions and deletions without reallocating memory.

- **Stacks & Queues**  
  Abstract data types following *LIFO* (Last-In-First-Out) and *FIFO* (First-In-First-Out) principles respectively.  
  Useful in parsing, recursion tracking, and scheduling systems.

- **Trees**  
  Hierarchical data structure with parent-child relationships.  
  Backbone of efficient searching and sorting (e.g., BST, AVL, heaps).

- **Graphs**  
  Collection of nodes (vertices) connected by edges.  
  Ideal for modeling networks, shortest path algorithms, and dependency resolution.

- **Hash Tables**  
  Data structure that maps keys to values using hash functions.  
  Enables constant-time average access and is heavily used in caching and indexing.

---

### ⚙️ Core Algorithms
- **Sorting Algorithms**  
  Includes Merge Sort, Quick Sort, Bubble Sort, and Insertion Sort.  
  Demonstrates time–space trade-offs and algorithmic efficiency.

- **Searching Algorithms**  
  Covers Linear Search and Binary Search.  
  Forms the foundation of optimized data retrieval in ordered structures.

- **Recursion & Backtracking**  
  Fundamental approach to solving problems by breaking them down into subproblems.  
  Applied in puzzles, pathfinding, and tree traversal.

- **Graph Algorithms**  
  Classic implementations like BFS, DFS, Dijkstra’s, and Topological Sort.  
  Useful for route planning, dependency management, and optimization problems.

- **Dynamic Programming**  
  Optimization technique to solve overlapping subproblems efficiently.  
  Examples: Fibonacci sequence, knapsack problem, matrix path finding.

---

### 🧩 Additional Highlights
- **Fully modular architecture** – Each operation isolated in its own file for readability.  
- **Comprehensive docstrings** – Clear, consistent documentation across modules.  
- **Multiple implementations per data structure** to understand trade-offs.  
- **Strict separation of concerns** – schemas, operations, and execution layers.  
- **Easy testing & demos** – Each structure includes example usage via `main.py`.
---
## 🧱 Current Implementations

| Data Structure | Status | Highlights |
|----------------|---------|------------|
| **Singly Linked List** | ✅ Complete | Modular, cycle-safe, test-covered |
| **Doubly Linked List** | ✅ Complete | Pointer-based, size-tracked |
| **Stack (List-based)** | ✅ Complete | Simple implementation, learning-focused |
| **Stack (Deque-based)** | ✅ Complete | Efficient push/pop, production-aligned |
| **Stack (DLL-based)** | ✅ Complete | Pointer-driven, invariant-checked |
| **Queue (List-based)** | ✅ Complete | FIFO via list, dequeue-cost awareness |
| **Queue (Deque-based)** | ✅ Complete | Optimal FIFO, production-ready |
| **Queue (DLL-based)** | ✅ Complete | Explicit head/tail control |
| **Hash Table (List Buckets)** | ✅ Complete | Chaining via Python lists, resize-aware |
| **Hash Table (Linked List Buckets)** | ✅ Complete | Node-based chaining, invariants enforced |
| **Trees** | ⏳ Planned | Binary tree, BST, traversal ops |
| **Graphs** | ⏳ Planned | Adjacency list & matrix |
---

## 🧩 Getting Started
```bash
# Clone the repo
git clone https://github.com/pavanpalve12/data_structures_algorithms
cd dsa

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt
