"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------
This module serves as the **entry point and test harness** for the Graph
implementation.

It is intended for:
- Manual testing
- Behavioral verification
- Learning and experimentation

This module:
- Constructs sample graphs
- Invokes core graph operations
- Demonstrates traversals and graph properties
- Prints results for inspection

It is **not intended for production use**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Create representative test graphs
- Exercise Graph APIs
- Display traversal and property outputs
------------------------------------------------------------------------------------
Dependencies
------------------------------------------------------------------------------------
- schemas.Graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Focuses on clarity over automation
- Uses explicit graph construction
- Mirrors real usage patterns of the Graph API
------------------------------------------------------------------------------------
"""

from graph.undirected_graph.schemas import Graph


def generate_test_graph(graph: Graph) -> None:
    """
    Populate the graph with a predefined structure for testing.

    The generated graph contains:
    - One connected component with a cycle
    - One separate connected component

    Structure:

        A — B — C
        |   |
        E — D

        F — G

    :param graph: Graph instance to populate
    :return: None
    """
    # Component 1 (cyclic)
    graph.insert_edge("A", "B")
    graph.insert_edge("B", "C")
    graph.insert_edge("B", "D")
    graph.insert_edge("D", "E")
    graph.insert_edge("E", "A")

    # Component 2 (disconnected)
    graph.insert_edge("F", "G")


def main() -> None:
    """
    Execute graph operations to validate functionality.

    This function:
    - Builds a test graph
    - Prints graph structure
    - Runs BFS and DFS traversals
    - Computes graph properties
    - Performs mutation operations
    - Displays results after each stage

    :return: None
    """
    graph = Graph()
    generate_test_graph(graph)

    print(" Graph Structure ".center(60, "-"))
    graph.print_graph()
    print("-" * 60)

    print(" Traversals ".center(60, "-"))
    print(f"BFS (Iterative) from A : {graph.bfs_iterative('A')}")
    print(f"BFS (Recursive) from A : {graph.bfs_recursive('A')}")
    print(f"DFS (Iterative) from A : {graph.dfs_iterative('A')}")
    print(f"DFS (Recursive) from A : {graph.dfs_recursive('A')}")
    print("-" * 60)

    print(" Graph Properties ".center(60, "-"))
    print(f"Connected Components        : {graph.get_connected_components()}")
    print(f"Cycle Detected (Iterative)  : {graph.detect_cycle_iterative('A')}")
    print(f"Cycle Detected (Recursive)  : {graph.detect_cycle_recursive('A')}")
    print("-" * 60)

    print(" Mutation Tests ".center(60, "-"))
    print("Removing edge A — B")
    graph.remove_edge("A", "B")
    graph.print_graph()

    print("\nRemoving vertex D")
    graph.remove_vertex("D")
    graph.print_graph()
    print("-" * 60)


if __name__ == "__main__":
    main()
