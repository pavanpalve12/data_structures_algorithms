"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------
This module defines the **core data schema** for the Directed Acyclic Graph (DAG).

It contains a lightweight, data-only Graph container that stores DAG state
using an adjacency list representation.

This module intentionally contains:
- No traversal logic
- No mutation logic
- No validation logic

All behavior and invariant enforcement is delegated to `operations.py`.
------------------------------------------------------------------------------------
"""

from graph.directed_acyclic_graph import operations


class Graph:
    """
    Directed Acyclic Graph (DAG) data container.

    Stores adjacency list state only.
    """

    def __init__(self):
        """
        Initialize an empty DAG.
        """
        self.graph = {}

# ------------------------------------------------------------------
# Core Operations
# ------------------------------------------------------------------
    def insert_vertex(self, vertex):
        """Add a vertex to the DAG."""
        return operations.insert_vertex(self.graph, vertex)

    def insert_edge(self, from_vertex, to_vertex):
        """
        Add a directed edge (from_vertex → to_vertex).

        Must not introduce a cycle.
        """
        return operations.insert_edge(self.graph, from_vertex, to_vertex)

    def remove_vertex(self, vertex):
        """Remove a vertex and all incident edges."""
        return operations.remove_vertex(self.graph, vertex)

    def remove_edge(self, from_vertex, to_vertex):
        """Remove a directed edge."""
        return operations.remove_edge(self.graph, from_vertex, to_vertex)

# ------------------------------------------------------------------
# DAG Properties
# ------------------------------------------------------------------
    def is_dag(self):
        """Check whether the graph satisfies DAG invariant."""
        return operations.is_dag(self.graph)

    def kahn_topological_sort(self):
        """Return a topological ordering of vertices."""
        return operations.kahn_topological_sort(self.graph)

    def dfs_topological_sort(self, start_vertex):
        """Return a topological ordering of vertices."""
        return operations.dfs_topological_sort(self.graph, start_vertex)

# ------------------------------------------------------------------
# Traversals
# ------------------------------------------------------------------
    def bfs(self, start_vertex):
        return operations.bfs(self.graph, start_vertex, [])

    def dfs(self, start_vertex):
        return operations.dfs(self.graph, start_vertex,[])

# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------
    def print_graph(self):
        return operations.print_graph(self.graph)
