"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------
This module serves as the **entry point and test harness** for the
Directed Acyclic Graph (DAG) implementation.

It is intended for:
- Manual testing
- Behavioral verification
- Learning and experimentation

This module:
- Constructs sample DAGs
- Invokes core DAG operations
- Demonstrates traversals and topological sorting
- Verifies acyclic invariants
- Prints results for inspection

It is **not intended for production use**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Create representative DAG test graphs
- Exercise DAG APIs
- Display traversal, ordering, and invariant outputs
------------------------------------------------------------------------------------
Dependencies
------------------------------------------------------------------------------------
- schemas.Graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Focuses on correctness and clarity
- Uses explicit graph construction
- Ensures no cycles are introduced
- Mirrors real usage patterns of the DAG API
------------------------------------------------------------------------------------
"""

from graph.directed_acyclic_graph.schemas import Graph


def generate_test_dag(graph: Graph) -> None:
    """
    Populate the DAG with a predefined acyclic structure for testing.

    Structure:

        A → B → D → F
        |    |
        ↓    ↓
        C    E

        G → H

    Properties:
    - Two disconnected components
    - No cycles
    - Multiple valid topological orders

    :param graph: Graph instance to populate
    :return: None
    """
    # Component 1
    graph.insert_edge("A", "B")
    graph.insert_edge("A", "C")
    graph.insert_edge("B", "D")
    graph.insert_edge("B", "E")
    graph.insert_edge("D", "F")

    # Component 2 (disconnected)
    graph.insert_edge("G", "H")


def main() -> None:
    """
    Execute DAG operations to validate functionality.

    This function:
    - Builds a test DAG
    - Prints graph structure
    - Runs BFS and DFS traversals
    - Performs topological sorting (Kahn and DFS)
    - Verifies DAG invariant
    - Performs mutation tests
    - Displays results after each stage

    :return: None
    """
    graph = Graph()
    generate_test_dag(graph)

    print(" DAG Structure ".center(60, "-"))
    graph.print_graph()
    print("-" * 60)

    print(" Traversals ".center(60, "-"))
    print(f"BFS from A : {graph.bfs(['A'])}")
    print(f"DFS from A : {graph.dfs('A')}")
    print("-" * 60)

    print(" DAG Properties ".center(60, "-"))
    print(f"Is DAG                : {graph.is_dag()}")
    print(f"Topological Sort (Kahn): {graph.kahn_topological_sort()}")
    print(f"Topological Sort (DFS) : {graph.dfs_topological_sort('A')}")
    print("-" * 60)

    print(" Mutation Tests ".center(60, "-"))
    print("Attempting to introduce a cycle: F → A")
    graph.insert_edge("F", "A")   # should be rejected
    graph.print_graph()

    print("\nRemoving edge B → E")
    graph.remove_edge("B", "E")
    graph.print_graph()
    print("-" * 60)


if __name__ == "__main__":
    main()
