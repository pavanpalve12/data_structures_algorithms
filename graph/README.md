# Graph Implementations in Python

This document explains how a **Graph** can be implemented using different
graph models while preserving the **same graph abstraction**.

Currently, the repository includes:

1. **Undirected, Unweighted Graph**
2. **Directed, Unweighted Graph**

Future graph variants will extend this foundation without changing the
core conceptual model.

---

## Graph Concept (Quick Recap)

A **graph** is a non-linear data structure consisting of:

- **Vertices (nodes)** — entities in the system
- **Edges** — relationships between vertices

Graphs are used to model:
- networks
- dependencies
- workflows
- hierarchies with cross-links

---

## Core Graph Operations

These operations are common across all graph variants.

| Operation | Description |
|---------|-------------|
| `insert_vertex` | Add a vertex to the graph |
| `insert_edge` | Add an edge between vertices |
| `remove_vertex` | Remove a vertex and its edges |
| `remove_edge` | Remove an edge |
| `bfs` | Breadth-first traversal |
| `dfs` | Depth-first traversal |
| `detect_cycle` | Detect cycles in the graph |
| `print_graph` | Display adjacency list |

---

## Implementation 1: Undirected, Unweighted Graph

### Key Characteristics
- Edges are **bidirectional** (u ↔ v)
- Adjacency list is **symmetric**
- Traversal can move both ways along an edge

### Operation Semantics

| Operation | Behavior |
|---------|----------|
| `insert_edge(u, v)` | Adds u → v and v → u |
| `remove_edge(u, v)` | Removes both directions |
| `bfs / dfs` | Traverses all neighbors |
| `detect_cycle` | Parent-based DFS logic |
| `components` | Multiple connected components supported |

---
## Sample Output Representation
## Example Graph

```text
        A — B — C
        |   |
        E — D

        F — G
```

Adjacency List:

```text
================ Undirected Graph ================
	Graph [A] → [B, E]
	Graph [B] → [A, C, D]
	Graph [C] → [B]
	Graph [D] → [B, E]
	Graph [E] → [D, A]
	Graph [F] → [G]
	Graph [G] → [F]
==================================================
------------------------ Traversals ------------------------
BFS (Iterative) from A : ['A', 'B', 'E', 'C', 'D']
BFS (Recursive) from A : ['A', 'B', 'E', 'C', 'D']
DFS (Iterative) from A : ['A', 'E', 'D', 'B', 'C']
DFS (Recursive) from A : ['A', 'B', 'C', 'D', 'E']
------------------------------------------------------------
--------------------- Graph Properties ---------------------
Connected Components        : 2
Cycle Detected (Iterative)  : True
Cycle Detected (Recursive)  : True
------------------------------------------------------------
```

------------------------------------------------------------------------------------

## Implementation 2: Directed, Unweighted Graph

### Key Characteristics
- Edges are **one-way** (u → v)
- Adjacency list is **asymmetric**
- Traversal follows **outgoing edges only**

### Operation Semantics

| Operation | Behavior |
|---------|----------|
| `insert_edge(u, v)` | Adds u → v only |
| `remove_edge(u, v)` | Removes u → v |
| `bfs / dfs` | Traverses outgoing neighbors |
| `detect_cycle` | DFS recursion-stack tracking |
| `reachability` | Direction-aware reachability |

---
## Sample Output Representation
## Example Graph
```text
        A → B → C → D
            ↑       ↓
            F ← E ←-

        G → H

================ Directed Graph  =================
	Graph [A] → [B]
	Graph [B] → [C]
	Graph [C] → [D]
	Graph [D] → [E]
	Graph [E] → [F]
	Graph [F] → [B]
	Graph [G] → [H]
	Graph [H] → []
==================================================
------------------------------------------------------------
------------------------ Traversals ------------------------
BFS (Iterative) from A : ['A', 'B', 'C', 'D', 'E', 'F']
BFS (Recursive) from A : ['A', 'B', 'C', 'D', 'E', 'F']
DFS (Iterative) from A : ['A', 'B', 'C', 'D', 'E', 'F']
DFS (Recursive) from A : ['A', 'B', 'C', 'D', 'E', 'F']
------------------------------------------------------------
--------------------- Graph Properties ---------------------
Cycle Detected : True
------------------------------------------------------------
```

---

## Structural Design (Common to All Graphs)

All graph implementations follow the same architecture:

```
graph/<variant>/
├── schemas.py      # Graph container (state only)
├── operations.py   # All graph algorithms
└── main.py         # Test harness
```

### Design Principles
- No logic inside schema classes
- All algorithms live in operations modules
- Adjacency list passed explicitly
- Traversal order not enforced

---

## Summary Comparison

| Aspect | Undirected Graph | Directed Graph |
|------|------------------|----------------|
| Edge Direction | Bidirectional | One-way |
| Adjacency List | Symmetric | Asymmetric |
| BFS / DFS | Same logic | Same logic |
| Cycle Detection | Parent-based | Recursion stack |
| Components | Connected components | Reachability-based |

---

## Future Graph Variants (Planned)

- Directed Acyclic Graph (DAG)
- Weighted Graph
- Strongly Connected Components (SCC)
- Topological Sorting
- Shortest Path Algorithms

---

## Final Notes

The **graph abstraction remains constant** across implementations.
Only the **edge semantics and algorithms** change based on graph type.

This layered approach enables incremental learning and clean extensibility.
