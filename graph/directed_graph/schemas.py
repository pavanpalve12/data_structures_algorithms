"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------
This module defines the **core data schema** for the Directed Graph data structure.

It contains a lightweight, data-only Graph container that stores graph state
using an adjacency list representation.

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
- Hold directed adjacency list state
------------------------------------------------------------------------------------
Public Classes
------------------------------------------------------------------------------------
- Graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Graph holds state only (adjacency list)
- Edges are directional (u → v)
- All algorithms are implemented externally
------------------------------------------------------------------------------------
"""

from graph.directed_graph import operations

# ------------------------------------------------------------------
# Class Graph: structure for graph
# ------------------------------------------------------------------
class Graph:
    """
    Directed Graph data container using adjacency list representation.

    This class stores graph state only and delegates all behavior
    (insert, delete, traversal, analysis) to external operations.
    """

    def __init__(self):
        """
        Initialize an empty directed graph.

        Creates an empty adjacency list where:
        - Keys represent vertices
        - Values represent outgoing neighbors
        """
        self.graph = {}

# ------------------------------------------------------------------
# Core Operations
# ------------------------------------------------------------------
    def insert_vertex(self, vertex):
        """
        Add a vertex to the graph.

        :param vertex: Unique vertex identifier
        :return: None
        """
        return operations.insert_vertex(self.graph, vertex)

    def insert_edge(self, from_vertex, to_vertex):
        """
        Add a directed edge (from_vertex → to_vertex).

        :param from_vertex: Source vertex
        :param to_vertex: Destination vertex
        :return: None
        """
        return operations.insert_edge(self.graph, from_vertex, to_vertex)

    def remove_vertex(self, vertex):
        """
        Remove a vertex and all its incoming and outgoing edges.

        :param vertex: Vertex to remove
        :return: None
        """
        return operations.remove_vertex(self.graph, vertex)

    def remove_edge(self, from_vertex, to_vertex):
        """
        Remove a directed edge (from_vertex → to_vertex).

        :param from_vertex: Source vertex
        :param to_vertex: Destination vertex
        :return: None
        """
        return operations.remove_edge(self.graph, from_vertex, to_vertex)

# ------------------------------------------------------------------
# Traversals
# ------------------------------------------------------------------
    def bfs_iterative(self, start_vertex):
        """
        Perform iterative Breadth-First Search (BFS).

        :param start_vertex: Starting vertex
        :return: BFS traversal order
        """
        return operations.bfs_iterative(self.graph, start_vertex)

    def bfs_recursive(self, start_vertex):
        """
        Perform recursive (level-based) Breadth-First Search (BFS).

        :param start_vertex: Starting vertex
        :return: BFS traversal order
        """
        return operations.bfs_recursive(self.graph, start_vertex, [])

    def dfs_iterative(self, start_vertex):
        """
        Perform iterative Depth-First Search (DFS).

        :param start_vertex: Starting vertex
        :return: DFS traversal order
        """
        return operations.dfs_iterative(self.graph, start_vertex)

    def dfs_recursive(self, start_vertex):
        """
        Perform recursive Depth-First Search (DFS).

        :param start_vertex: Starting vertex
        :return: DFS traversal order
        """
        return operations.dfs_recursive(self.graph, start_vertex, [])

# ------------------------------------------------------------------
# Graph Properties
# ------------------------------------------------------------------
    def detect_cycle(self):
        """
        Detect whether the directed graph contains a cycle.

        :return: True if cycle exists, otherwise False
        """
        return operations.detect_cycle(self.graph)

# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------
    def print_graph(self):
        """
        Print the adjacency list representation of the graph.

        :return: None
        """
        return operations.print_graph(self.graph)
