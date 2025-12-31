# Graph Implementations in Python

This document explains how a **Graph** can be implemented using different
graph models while preserving the **same graph abstraction**.

Currently, the repository includes:

1. **Undirected, Unweighted Graph**
2. **Directed, Unweighted Graph**
3. **Undirected, Weighted Graph**
4. **Directed, Weighted Graph**

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

------------------------------------------------------------------------------------

## Implementation 3: Undirected, Weighted Graph

### Key Characteristics
- Edges are **bidirectional** (u ↔ v)
- Each edge has an associated **weight**
- Adjacency list stores `(neighbor, weight)` tuples
- Traversals are **weight-agnostic**

### Operation Semantics

| Operation | Behavior |
|---------|----------|
| `insert_edge(u, v, w)` | Adds u ↔ v with weight w |
| `update_edge_weight` | Updates weight on both directions |
| `remove_edge(u, v)` | Removes both directions |
| `get_path_cost(path)` | Sum of weights along path |
| `shortest_path_dijkstra` | Computes shortest paths |

---
## Sample Output Representation
### Sample Graph
```text
         A
       / | \
     4/  |  \2
     B  1|   C
      \  |  /
      5\ | /3
         D

        E — F
```
### Sample Output
```text
----------------- Weighted Graph Structure -----------------
=========== Undirected Weighted Graph ============
	Graph [A] → [('B', 4), ('C', 2), ('D', 1)]
	Graph [B] → [('A', 4), ('D', 5)]
	Graph [C] → [('A', 2), ('D', 3)]
	Graph [D] → [('B', 5), ('C', 3), ('A', 1)]
	Graph [E] → [('F', 7)]
	Graph [F] → [('E', 7)]
==================================================
------------------------------------------------------------
--------------- Traversals (Weights Ignored) ---------------
BFS (Iterative) from A : ['A', 'B', 'C', 'D']
BFS (Recursive) from A : ['A', 'B', 'C', 'D']
DFS (Iterative) from A : ['A', 'D', 'C', 'B']
DFS (Recursive) from A : ['A', 'B', 'D', 'C']
------------------------------------------------------------
--------------------- Graph Properties ---------------------
Connected Components : 2
Cycle Detected       : True
------------------------------------------------------------
--------------------- Path Cost Tests ----------------------
Path           : ['A', 'D', 'C']
Total Cost     : 4
------------------------------------------------------------
----------------- Shortest Path (Dijkstra) -----------------
Distances from A : {'A': 0, 'B': 4, 'C': 2, 'D': 1, 'E': inf, 'F': inf}
Shortest Path A → D : ['A', 'B']
------------------------------------------------------------
```

------------------------------------------------------------------------------------

## Implementation 4: Directed, Weighted Graph

### Key Characteristics
- Edges are **one-way** (u → v)
- Each edge has an associated **weight**
- Adjacency list stores `(neighbor, weight)` tuples
- Traversal and shortest paths follow **edge direction**

### Operation Semantics

| Operation | Behavior |
|---------|----------|
| `insert_edge(u, v, w)` | Adds directed edge u → v with weight w |
| `update_edge_weight` | Updates weight for u → v only |
| `remove_edge(u, v)` | Removes directed edge u → v |
| `get_path_cost(path)` | Sum of weights along directed path |
| `shortest_path_dijkstra` | Computes shortest directed paths |

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

### Sample Output
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

------------------------------------------------------------------------------------

## Implementation 5: Directed Acyclic Graph (DAG)

### Key Characteristics
- Edges are **one-way** (u → v)
- **No cycles allowed** (acyclic by definition)
- Adjacency list is **asymmetric**
- Vertex ordering must respect **dependency direction**

### Operation Semantics

| Operation | Behavior |
|---------|----------|
| `insert_edge(u, v)` | Adds u → v **only if it does not create a cycle** |
| `remove_edge(u, v)` | Removes u → v |
| `bfs / dfs` | Traverses outgoing neighbors only |
| `detect_cycle` | Used to **enforce DAG invariant** |
| `topological_sort (Kahn)` | Level / dependency-based ordering |
| `topological_sort (DFS)` | Depth-based ordering (reverse postorder) |

---
## Sample Output
### Sample Graph
```text
Sample Graph
A → B → D → F
|    |
↓    ↓
C    E

G → H
```
### Output
```text
---------------------- DAG Structure -----------------------
============= Directed Acyclic Graph =============
	A → ['B', 'C']
	B → ['D', 'E']
	C → []
	D → ['F']
	E → []
	F → []
	G → ['H']
	H → []
==================================================
------------------------------------------------------------
------------------------ Traversals ------------------------
BFS from A : ['A', 'B', 'C', 'D', 'E', 'F']
DFS from A : ['A', 'B', 'D', 'F', 'E', 'C']
------------------------------------------------------------
---------------------- DAG Properties ----------------------
Is DAG                : True
Topological Sort (Kahn): ['A', 'G', 'B', 'C', 'H', 'D', 'E', 'F']
Topological Sort (DFS) : ['A', 'B', 'D', 'F', 'E', 'C']
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

## Graph Variants — Comparison Summary

| Feature / Property | Undirected Graph | Directed Graph | Undirected Weighted | Directed Weighted | DAG |
|-------------------|------------------|----------------|---------------------|-------------------|-----|
| Edge Direction | Bidirectional (u ↔ v) | One-way (u → v) | Bidirectional (u ↔ v) | One-way (u → v) | One-way (u → v) |
| Weights | ❌ | ❌ | ✅ | ✅ | ❌ |
| Cycles Allowed | ✅ Allowed | ✅ Allowed | ✅ Allowed | ✅ Allowed | ❌ Not Allowed |
| Adjacency List | Symmetric | Asymmetric | Symmetric | Asymmetric | Asymmetric |
| Traversal Scope | All neighbors | Outgoing neighbors only | All neighbors | Outgoing neighbors only | Outgoing neighbors only |
| Shortest Path | ❌ | ❌ | ✅ | ✅ | ❌ |
| Connected Components | Supported | Not meaningful | Supported | Not meaningful | Not meaningful |
| Topological Sort | ❌ Not applicable | ❌ Not guaranteed | ❌ Not applicable | ❌ Not applicable | ✅ Mandatory |

---

## Future Graph Variants (Planned)

- Bellman–Ford (negative weights)
- Floyd–Warshall (all-pairs shortest path)
- Strongly Connected Components (SCC)
- Minimum Spanning Tree (MST)

---

## Final Notes

The **graph abstraction remains constant** across implementations.
Only the **edge semantics and algorithms** change based on graph type.

This layered approach enables incremental learning and clean extensibility.
