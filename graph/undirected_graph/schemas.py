"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------
This module defines the **core data schemas** for the Graph data structure.

It contains lightweight, data-only classes that represent the fundamental
building blocks of a graph using an adjacency list representation.

This module is intentionally minimal and contains:
- No traversal logic
- No mutation logic
- No validation logic

All behavior is delegated to functions implemented in `operations.py`,
ensuring a clean separation between **data representation** and **behavior**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Define the Graph container structure
- Hold adjacency list state
------------------------------------------------------------------------------------
Public Classes
------------------------------------------------------------------------------------
- Graph
------------------------------------------------------------------------------------
Internal / Helper Classes
------------------------------------------------------------------------------------
None
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Graph holds state only (adjacency list)
- All algorithms and mutations are implemented externally
- This module acts as a thin façade over operations
- Traversal order is not enforced at schema level
------------------------------------------------------------------------------------
"""

from graph.undirected_graph import operations


class Graph:
    """
    Graph data container using adjacency list representation.

    This class stores graph state only and delegates all behavior
    (insert, delete, traversal, analysis) to external operations.
    """

    def __init__(self):
        """
        Initialize an empty graph.

        Creates an empty adjacency list where:
        - Keys represent vertices
        - Values represent neighboring vertices
        """
        self.graph = {}

    # ------------------------------------------------------------------
    # Core Operations
    # ------------------------------------------------------------------
    def insert_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Delegates to operations.insert_vertex.

        :param vertex: Unique identifier for the vertex
        :type vertex: Any hashable type
        :return: None
        """
        return operations.insert_vertex(self.graph, vertex)

    def insert_edge(self, from_vertex, to_vertex):
        """
        Add an undirected edge between two vertices.

        Delegates to operations.insert_edge.
        Missing vertices may be auto-created.

        :param from_vertex: Source vertex
        :type from_vertex: Any hashable type
        :param to_vertex: Destination vertex
        :type to_vertex: Any hashable type
        :return: None
        """
        return operations.insert_edge(self.graph, from_vertex, to_vertex)

    def remove_vertex(self, vertex):
        """
        Remove a vertex and all its incident edges.

        Delegates to operations.remove_vertex.

        :param vertex: Vertex to remove
        :type vertex: Any hashable type
        :return: None
        """
        return operations.remove_vertex(self.graph, vertex)

    def remove_edge(self, from_vertex, to_vertex):
        """
        Remove an undirected edge between two vertices.

        Delegates to operations.remove_edge.

        :param from_vertex: One endpoint of the edge
        :type from_vertex: Any hashable type
        :param to_vertex: Other endpoint of the edge
        :type to_vertex: Any hashable type
        :return: None
        """
        return operations.remove_edge(self.graph, from_vertex, to_vertex)

    # ------------------------------------------------------------------
    # BFS Traversal
    # ------------------------------------------------------------------
    def bfs_iterative(self, start_vertex):
        """
        Perform iterative Breadth-First Search (BFS).

        Delegates to operations.bfs_iterative.

        :param start_vertex: Starting vertex for traversal
        :type start_vertex: Any hashable type
        :return: BFS traversal order
        :rtype: list
        """
        return operations.bfs_iterative(self.graph, start_vertex)

    def bfs_recursive(self, start_vertex):
        """
        Perform recursive (level-based) Breadth-First Search (BFS).

        Delegates to operations.bfs_recursive.
        Internally manages traversal state.

        :param start_vertex: Starting vertex for traversal
        :type start_vertex: Any hashable type
        :return: BFS traversal order
        :rtype: list
        """
        return operations.bfs_recursive(self.graph, [start_vertex], [])

    # ------------------------------------------------------------------
    # DFS Traversals
    # ------------------------------------------------------------------
    def dfs_iterative(self, start_vertex):
        """
        Perform iterative Depth-First Search (DFS).

        Delegates to operations.dfs_iterative.

        :param start_vertex: Starting vertex for traversal
        :type start_vertex: Any hashable type
        :return: DFS traversal order
        :rtype: list
        """
        return operations.dfs_iterative(self.graph, start_vertex)

    def dfs_recursive(self, start_vertex):
        """
        Perform recursive Depth-First Search (DFS).

        Delegates to operations.dfs_recursive.
        Internally manages traversal state.

        :param start_vertex: Starting vertex for traversal
        :type start_vertex: Any hashable type
        :return: DFS traversal order
        :rtype: list
        """
        return operations.dfs_recursive(self.graph, start_vertex, [])

    # ------------------------------------------------------------------
    # Graph State Operations
    # ------------------------------------------------------------------
    def get_connected_components(self):
        """
        Compute the number of connected components in the graph.

        Delegates to operations.get_connected_components.

        :return: Number of connected components
        :rtype: int
        """
        return operations.get_connected_components(self.graph)

    def detect_cycle_iterative(self, start_vertex):
        """
        Detect whether the graph contains a cycle using iterative DFS.

        Delegates to operations.detect_cycle_iterative.

        :param start_vertex: Starting vertex
        :type start_vertex: Any hashable type
        :return: True if a cycle exists, otherwise False
        :rtype: bool
        """
        return operations.detect_cycle_iterative(self.graph, start_vertex)

    def detect_cycle_recursive(self, start_vertex):
        """
        Detect whether the graph contains a cycle using recursive DFS.

        Delegates to operations.detect_cycle_recursive.

        :param start_vertex: Starting vertex
        :type start_vertex: Any hashable type
        :return: True if a cycle exists, otherwise False
        :rtype: bool
        """
        return operations.detect_cycle_recursive(self.graph, start_vertex)

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------
    def print_graph(self):
        """
        Print the adjacency list representation of the graph.

        Delegates to operations.print_graph.

        :return: None
        """
        return operations.print_graph(self.graph)
