"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements **core operations and invariants** for a
Directed Acyclic Graph (DAG).

All functions operate on a **directed adjacency list** represented as a
dictionary mapping vertices to lists of outgoing neighbors.

Primary responsibilities:
- Vertex and edge mutation
- Enforcing the DAG (acyclic) invariant
- Topological sorting (DFS-based and Kahn’s algorithm)
- Graph traversal utilities
- Cycle detection for directed graphs

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Graph is represented as an adjacency list (dict)
- All edges are directional (u → v)
- DAG validity is enforced during edge insertion
- Traversal utilities do not enforce DAG invariants
- No I/O or persistence logic exists in this module
------------------------------------------------------------------------------------
"""

from collections import deque
from typing import Any, List, Set


# ------------------------------------------------------------------
# Core Operations
# ------------------------------------------------------------------
def insert_vertex(graph: dict, vertex: Any) -> None:
    """
    Insert a vertex into the DAG.

    If the vertex already exists, this operation is a no-op.

    :param graph: Directed adjacency list
    :param vertex: Hashable vertex identifier
    :return: None
    """
    if vertex not in graph:
        graph[vertex] = []


def insert_edge(graph: dict, from_vertex: Any, to_vertex: Any) -> None:
    """
    Insert a directed edge (from_vertex → to_vertex).

    Vertices are auto-created if missing.
    If the edge introduces a cycle, it is rolled back to
    preserve the DAG invariant.

    :param graph: Directed adjacency list
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: None
    """
    if from_vertex not in graph:
        graph[from_vertex] = []

    if to_vertex not in graph:
        graph[to_vertex] = []

    if to_vertex in graph[from_vertex]:
        return

    graph[from_vertex].append(to_vertex)

    # Enforce DAG invariant
    if not is_dag(graph):
        graph[from_vertex].remove(to_vertex)


def remove_vertex(graph: dict, vertex: Any) -> None:
    """
    Remove a vertex and all incoming and outgoing edges.

    If the vertex does not exist, this operation is a no-op.

    :param graph: Directed adjacency list
    :param vertex: Vertex to remove
    :return: None
    """
    if vertex not in graph:
        return

    # Remove outgoing edges
    graph[vertex].clear()

    # Remove incoming edges
    for vtx in graph:
        if vertex in graph[vtx]:
            graph[vtx].remove(vertex)

    del graph[vertex]


def remove_edge(graph: dict, from_vertex: Any, to_vertex: Any) -> None:
    """
    Remove a directed edge (from_vertex → to_vertex).

    If the edge or source vertex does not exist,
    the operation is a no-op.

    :param graph: Directed adjacency list
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: None
    """
    if from_vertex in graph and to_vertex in graph[from_vertex]:
        graph[from_vertex].remove(to_vertex)


# ------------------------------------------------------------------
# DAG Properties
# ------------------------------------------------------------------
def is_dag(graph: dict) -> bool:
    """
    Determine whether the graph is acyclic.

    :param graph: Directed adjacency list
    :return: True if graph is a DAG, otherwise False
    """
    return not detect_cycle(graph)


def kahn_topological_sort(graph: dict) -> List[Any]:
    """
    Perform topological sorting using Kahn’s algorithm.

    This algorithm is level-based and processes vertices
    in order of dependency readiness (indegree = 0).

    :param graph: Directed adjacency list
    :return: List of vertices in topological order
    """
    indegree_map = {vertex: 0 for vertex in graph}

    for neighbors in graph.values():
        for vertex in neighbors:
            indegree_map[vertex] += 1

    process_queue = deque()
    sort_output = []

    for vertex, indegree in indegree_map.items():
        if indegree == 0:
            process_queue.append(vertex)

    while process_queue:
        current = process_queue.popleft()
        sort_output.append(current)

        for neighbor in graph[current]:
            indegree_map[neighbor] -= 1
            if indegree_map[neighbor] == 0:
                process_queue.append(neighbor)

    return sort_output


def dfs_topological_sort(graph: dict, start_vertex: Any) -> List[Any]:
    """
    Perform DFS-based topological sorting starting from a given vertex.

    Uses an explicit stack with exploration flags to simulate recursion.
    This method only covers vertices reachable from start_vertex.

    :param graph: Directed adjacency list
    :param start_vertex: Starting vertex for DFS
    :return: Topological order of reachable vertices
    """
    visited = []
    stack = [(start_vertex, False)]

    while stack:
        current, explored = stack.pop()

        if explored is True and current not in visited:
            visited.append(current)
        else:
            stack.append((current, True))
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, False))

    return visited[::-1]


# ------------------------------------------------------------------
# Cycle Detection
# ------------------------------------------------------------------
def detect_cycle(graph: dict) -> bool:
    """
    Detect whether a directed graph contains a cycle.

    Uses DFS with recursion-stack tracking.
    A cycle exists if a vertex is revisited while still
    present in the current DFS path.

    :param graph: Directed adjacency list
    :return: True if a cycle exists, otherwise False
    """
    visited = set()
    rec_stack = set()

    for vertex in graph:
        if vertex not in visited:
            if _detect_cycle_dfs(graph, vertex, visited, rec_stack):
                return True
    return False


def _detect_cycle_dfs(
        graph: dict,
        vertex: Any,
        visited: Set[Any],
        rec_stack: Set[Any]
) -> bool:
    """
    Recursive helper for directed cycle detection.

    :param graph: Directed adjacency list
    :param vertex: Current vertex
    :param visited: Fully explored vertices
    :param rec_stack: Current DFS recursion path
    :return: True if a cycle is detected, otherwise False
    """
    visited.add(vertex)
    rec_stack.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if _detect_cycle_dfs(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(vertex)
    return False


# ------------------------------------------------------------------
# Traversals (Utility)
# ------------------------------------------------------------------
def bfs(graph: dict, level_vertices: List[Any], visited: List[Any]) -> List[Any]:
    """
    Perform breadth-first traversal from the given frontier.

    This function does not enforce DAG invariants.

    :param graph: Directed adjacency list
    :param level_vertices: Current BFS frontier
    :param visited: Accumulated traversal order
    :return: BFS traversal order
    """
    if not level_vertices:
        return visited

    next_level = []

    for vertex in level_vertices:
        if vertex not in visited:
            visited.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                next_level.append(neighbor)

    return bfs(graph, next_level, visited)


def dfs(graph: dict, vertex: Any, visited: List[Any]) -> List[Any]:
    """
    Perform depth-first traversal from a given vertex.

    This function does not enforce DAG invariants.

    :param graph: Directed adjacency list
    :param vertex: Starting vertex
    :param visited: Accumulated traversal order
    :return: DFS traversal order
    """
    if vertex in visited:
        return visited

    visited.append(vertex)

    for neighbor in graph[vertex]:
        dfs(graph, neighbor, visited)

    return visited


# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------
def print_graph(graph: dict) -> None:
    """
    Print the adjacency list representation of the graph.

    :param graph: Directed adjacency list
    :return: None
    """
    width = 50
    title = " Directed Acyclic Graph "
    print(title.center(width, "="))

    for vertex, neighbors in graph.items():
        print(f"\t{vertex} → {neighbors}")

    print("=" * width)
