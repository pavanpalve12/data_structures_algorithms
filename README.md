# 🧠 Data Structures & Algorithms (DSA) – Python Implementation

A clean, modular, and well-documented repository for mastering **Data Structures and Algorithms** in Python.  
Each data structure is implemented from scratch with production-style code organization, clear docstrings, and testable examples.

---

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
- **Comprehensive docstrings** – Consistent *Purpose / Args / Returns* format.  
- **Cycle detection, merge, reverse, sort, and deduplication support.**  
- **Helper operations** – Conversions (`to_list`, `from_list`), comparisons, and data cleanup.  
- **Linted & formatted** – Enforced via `.pylintrc` and pre-commit hooks.  
- **Easy testing** – Every structure ships with its own unit tests and examples.

---

## 🧱 Current Implementations
| Data Structure | Status | Highlights |
|----------------|---------|-------------|
| **Single Linked List** | ✅ Complete | Modular, cycle-safe, test-covered |
| **Stacks & Queues** | ⏳ Planned | Array & Linked implementations |
| **Trees** | ⏳ Planned | Binary tree, BST, traversal ops |
| **Graphs** | ⏳ Planned | Adjacency list & matrix representations |

---


## 🧩 Getting Started
```bash
# Clone the repo
git clone https://github.com/<your-username>/dsa.git
cd dsa

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt
    
