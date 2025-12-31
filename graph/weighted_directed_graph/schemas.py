"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------
This module defines the **core data schema** for the Directed Weighted Graph
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
- Edges are **directed** (u → v)
------------------------------------------------------------------------------------
"""

from graph.weighted_directed_graph import operations


class Graph:
    """
    Directed Weighted Graph data container using adjacency list representation.

    This class stores graph state only and delegates all behavior
    (insert, delete, traversal, analysis) to external operations.
    """

    def __init__(self):
        """
        Initialize an empty directed weighted graph.

        Adjacency list format:
        {
            A: [(B, 4), (C, 2)],
            B: [(D, 5)],
            C: [],
            D: []
        }
        """
        self.graph = {}

    # ------------------------------------------------------------------
    # Core Operations
    # ------------------------------------------------------------------
    def insert_vertex(self, vertex):
        """
        Add a vertex to the graph.

        :param vertex: Vertex identifier
        :return: None
        """
        return operations.insert_vertex(self.graph, vertex)

    def remove_vertex(self, vertex):
        """
        Remove a vertex and all its incident edges (incoming and outgoing).

        :param vertex: Vertex identifier
        :return: None
        """
        return operations.remove_vertex(self.graph, vertex)

    def remove_edge(self, from_vertex, to_vertex):
        """
        Remove a directed edge (u → v).

        :param from_vertex: Source vertex
        :param to_vertex: Destination vertex
        :return: None
        """
        return operations.remove_edge(self.graph, from_vertex, to_vertex)

    # ------------------------------------------------------------------
    # Edge Operations (WEIGHTED, DIRECTED)
    # ------------------------------------------------------------------
    def insert_edge(self, from_vertex, to_vertex, weight):
        """
        Add or update a directed weighted edge (u → v, w).

        :param from_vertex: Source vertex
        :param to_vertex: Destination vertex
        :param weight: Edge weight
        :return: None
        """
        return operations.insert_edge(self.graph, from_vertex, to_vertex, weight)

    def update_edge_weight(self, from_vertex, to_vertex, weight):
        """
        Update weight of an existing directed edge.

        :param from_vertex: Source vertex
        :param to_vertex: Destination vertex
        :param weight: New weight
        :return: None
        """
        return operations.update_edge_weight(self.graph, from_vertex, to_vertex, weight)

    def get_edge_weight(self, from_vertex, to_vertex):
        """
        Return weight for directed edge (u → v).

        :param from_vertex: Source vertex
        :param to_vertex: Destination vertex
        :return: Edge weight if present, else None
        """
        return operations.get_edge_weight(self.graph, from_vertex, to_vertex)

    # ------------------------------------------------------------------
    # Traversals (DIRECTION-AWARE, WEIGHT-AGNOSTIC)
    # ------------------------------------------------------------------
    def bfs_iterative(self, start_vertex):
        """
        Perform iterative BFS following edge direction.

        :param start_vertex: Starting vertex
        :return: BFS traversal order
        """
        return operations.bfs_iterative(self.graph, start_vertex)

    def bfs_recursive(self, start_vertex):
        """
        Perform recursive BFS following edge direction.

        :param start_vertex: Starting vertex
        :return: BFS traversal order
        """
        return operations.bfs_recursive(self.graph, [start_vertex], [])

    def dfs_iterative(self, start_vertex):
        """
        Perform iterative DFS following edge direction.

        :param start_vertex: Starting vertex
        :return: DFS traversal order
        """
        return operations.dfs_iterative(self.graph, start_vertex)

    def dfs_recursive(self, start_vertex):
        """
        Perform recursive DFS following edge direction.

        :param start_vertex: Starting vertex
        :return: DFS traversal order
        """
        return operations.dfs_recursive(self.graph, start_vertex, [])

    # ------------------------------------------------------------------
    # Shortest Path / Weight Logic
    # ------------------------------------------------------------------
    def get_path_cost(self, path):
        """
        Compute total cost of a given directed vertex path.

        :param path: List of vertices
        :return: Total cost or None if invalid path
        """
        return operations.get_path_cost(self.graph, path)

    def shortest_path_dijkstra(self, source):
        """
        Compute shortest path distances from source using Dijkstra's algorithm.

        :param source: Source vertex
        :return: Distance map and predecessor map
        """
        return operations.shortest_path_dijkstra(self.graph, source)

    def shortest_path_to(self, source, destination):
        """
        Compute shortest directed path from source to destination.

        :param source: Source vertex
        :param destination: Destination vertex
        :return: Shortest path as list of vertices
        """
        return operations.shortest_path_to(self.graph, source, destination)

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------
    def print_graph(self):
        """
        Print adjacency list representation of the directed weighted graph.

        :return: None
        """
        return operations.print_graph(self.graph)
