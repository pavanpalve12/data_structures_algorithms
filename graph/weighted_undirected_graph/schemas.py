"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------
This module defines the **core data schema** for the Undirected Weighted Graph
data structure.

It contains a lightweight, data-only Graph container that stores graph state
using a **weighted adjacency list** representation.

This module intentionally contains:
- No traversal logic
- No mutation logic
- No validation logic

All behavior is delegated to functions implemented in `operations.py`,
maintaining a strict separation between **data representation** and **behavior**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Define the Graph container structure
- Hold weighted adjacency list state
------------------------------------------------------------------------------------
Public Classes
------------------------------------------------------------------------------------
- Graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Graph holds state only (adjacency list)
- Adjacency list format:
    vertex -> List[(neighbor, weight)]
- All algorithms and mutations are implemented externally
------------------------------------------------------------------------------------
"""

from graph.weighted_undirected_graph import operations


class Graph:
    """
    Undirected Weighted Graph data container using adjacency list representation.

    This class stores graph state only and delegates all behavior
    (insert, delete, traversal, analysis) to external operations.
    """

    def __init__(self):
        """
        Initialize an empty undirected weighted graph.

        Adjacency list format:
        {
            A: [(B, 4), (C, 2)],
            B: [(A, 4)]
        }
        """
        self.graph = {}

    # ------------------------------------------------------------------
    # Core Operations (REUSED)
    # ------------------------------------------------------------------
    def insert_vertex(self, vertex):
        """Add a vertex to the graph."""
        return operations.insert_vertex(self.graph, vertex)

    def remove_vertex(self, vertex):
        """Remove a vertex and all its incident edges."""
        return operations.remove_vertex(self.graph, vertex)

    def remove_edge(self, from_vertex, to_vertex):
        """Remove an undirected edge between two vertices."""
        return operations.remove_edge(self.graph, from_vertex, to_vertex)

    # ------------------------------------------------------------------
    # Edge Operations (WEIGHTED)
    # ------------------------------------------------------------------
    def insert_edge(self, from_vertex, to_vertex, weight):
        """
        Add or update an undirected weighted edge (u ↔ v, w).
        """
        return operations.insert_edge(self.graph, from_vertex, to_vertex, weight)

    def update_edge_weight(self, from_vertex, to_vertex, weight):
        """
        Update weight of an existing edge.
        """
        return operations.update_edge_weight(self.graph, from_vertex, to_vertex, weight)

    def get_edge_weight(self, from_vertex, to_vertex):
        """
        Return weight for edge (u ↔ v).
        """
        return operations.get_edge_weight(self.graph, from_vertex, to_vertex)

    # ------------------------------------------------------------------
    # Traversals (REUSED – weight-agnostic)
    # ------------------------------------------------------------------
    def bfs_iterative(self, start_vertex):
        return operations.bfs_iterative(self.graph, start_vertex)

    def bfs_recursive(self, start_vertex):
        return operations.bfs_recursive(self.graph, [start_vertex], [])

    def dfs_iterative(self, start_vertex):
        return operations.dfs_iterative(self.graph, start_vertex)

    def dfs_recursive(self, start_vertex):
        return operations.dfs_recursive(self.graph, start_vertex, [])

    # ------------------------------------------------------------------
    # Graph Properties (REUSED)
    # ------------------------------------------------------------------
    def get_connected_components(self):
        return operations.get_connected_components(self.graph)

    def detect_cycle(self, start_vertex):
        return operations.detect_cycle(self.graph, start_vertex)

    # ------------------------------------------------------------------
    # Shortest Path / Weight Logic (NEW)
    # ------------------------------------------------------------------
    def get_path_cost(self, path):
        """
        Compute total cost of a given vertex path.
        """
        return operations.get_path_cost(self.graph, path)

    def shortest_path_dijkstra(self, source):
        """
        Compute shortest path distances from source to all vertices.
        """
        return operations.shortest_path_dijkstra(self.graph, source)

    def shortest_path_to(self, source, destination):
        """
        Compute shortest path and cost from source to destination.
        """
        return operations.shortest_path_to(self.graph, source, destination)

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------
    def print_graph(self):
        """Print the adjacency list representation."""
        return operations.print_graph(self.graph)
