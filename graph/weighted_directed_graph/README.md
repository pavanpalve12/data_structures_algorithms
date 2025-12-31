# Directed Weighted Graph Implementation (Python)

---

## Overview

This project provides a **clean, modular implementation of a Directed, Weighted Graph**
using an **adjacency list representation**, designed to clearly demonstrate how
directed weighted graph data structures work internally.

The implementation is derived from the undirected weighted graph by introducing
**edge directionality**, while preserving:

* traversal logic
* weight-aware algorithms
* separation of data and behavior

---

## Architecture

graph/<br>
└── graph/<br>
    ├── schemas.py    # Graph schema (state only, no logic)<br>
    ├── operations.py # Directed weighted graph algorithms and operations<br>
    └── main.py       # Entry point for testing and experimentation<br>

---

## Design Philosophy

* **Correctness before optimization**
* **Adjacency-list–driven structure**
* **No logic in schema (data) classes**
* **Explicit separation of concerns**
* **Traversal follows edge direction**
* **Algorithm-first learning approach**

---

## Data Structures

### Graph

* Represents a directed weighted graph using an adjacency list
* Each vertex maps to a list of `(neighbor, weight)` tuples
* Edges are **unidirectional** (`u → v`)
* Stores **state only**
* Delegates all behavior to `operations.py`

---

## Core Graph Operations

| Operation              | Description                                     |
| ---------------------- | ----------------------------------------------- |
| `insert_vertex`        | Add a vertex to the graph                       |
| `insert_edge(u, v, w)` | Add or update directed weighted edge `u → v`    |
| `update_edge_weight`   | Update weight of an existing directed edge      |
| `remove_vertex`        | Remove a vertex and all outgoing/incoming edges |
| `remove_edge`          | Remove a directed weighted edge                 |
| `bfs_iterative`        | Iterative breadth-first traversal (directional) |
| `bfs_recursive`        | Recursive (level-based) BFS                     |
| `dfs_iterative`        | Iterative depth-first traversal                 |
| `dfs_recursive`        | Recursive DFS                                   |
| `print_graph`          | Print adjacency list representation             |

---

## Directed Graph Semantics

* Edge `(u → v)` does **not** imply `(v → u)`
* All traversals and path computations follow **outgoing edges only**
* Reverse paths must be explicitly modeled

---

## Shortest Path & Cost Analysis

### Path Cost

* Path cost is the **sum of weights** along a given vertex path
* Each consecutive directed edge in the path must exist
* Invalid paths are rejected

### Shortest Path (Dijkstra)

* Computes shortest paths from a **single source**
* Operates on **directed, non-negative weighted edges**
* Uses a priority queue (min-heap)
* Returns:

  * distance map
  * predecessor map

---

## Sample Output Representation
### Sample Graph
```text
        (4)
   A --------▶ B
   | \         |
 (2)|  \(1)    |(5)
   |    \      |
   ▼     ▼     ▼
   C --------▶ D
        (3)


   E --------▶ F
        (7)

```

### Sample output
```text
------------ Directed Weighted Graph Structure -------------
============ Directed Weighted Graph =============
	Graph [A] → [('B', 4), ('C', 2), ('D', 1)]
	Graph [B] → [('D', 5)]
	Graph [C] → [('D', 3)]
	Graph [D] → []
	Graph [E] → [('F', 7)]
	Graph [F] → []
==================================================
------------------------------------------------------------
--------------- Traversals (Direction-Aware) ---------------
BFS (Iterative) from A : ['A', 'B', 'C', 'D']
BFS (Recursive) from A : ['A', 'B', 'C', 'D']
DFS (Iterative) from A : ['A', 'D', 'C', 'B']
DFS (Recursive) from A : ['A', 'B', 'D', 'C']
------------------------------------------------------------
--------------------- Path Cost Tests ----------------------
Path       : ['A', 'D']
Total Cost : 1
------------------------------------------------------------
----------------- Shortest Path (Dijkstra) -----------------
Distances from A : {'A': 0, 'B': 4, 'C': 2, 'D': 1, 'E': inf, 'F': inf}
Shortest Path A → D : ['A', 'D']
------------------------------------------------------------

```
---

## Module Responsibilities

### `schemas.py`

* Defines the `Graph` container
* Holds adjacency list state only

### `operations.py`

* Implements directed weighted graph operations
* Traversals (direction-aware, weight-agnostic)
* Path cost computation
* Shortest path (Dijkstra)

### `main.py`

* Entry point for experimentation and learning
* Constructs example directed graphs

---

## Notes

* Directionality is enforced **only** at edge insertion and update
* Shortest-path logic is unchanged from undirected version
* Suitable foundation for:

  * DAG shortest paths
  * Bellman–Ford extension
  * graph optimization problems

---
