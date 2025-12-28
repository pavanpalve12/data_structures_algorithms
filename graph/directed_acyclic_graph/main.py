"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------
Entry point and test harness for DAG implementation.
------------------------------------------------------------------------------------
"""

from graph.directed_acyclic_graph.schemas import Graph


def generate_test_graph(graph: Graph) -> None:
    """
    Create a sample DAG structure.

    Example:
        A → B → D
        A → C → D
    """
    graph.insert_edge("A", "B")
    graph.insert_edge("A", "C")
    graph.insert_edge("B", "D")
    graph.insert_edge("C", "D")


def main() -> None:
    graph = Graph()
    generate_test_graph(graph)

    graph.print_graph()

    print("Is DAG:", graph.is_dag())
    print("Topological Sort:", graph.topological_sort())


if __name__ == "__main__":
    main()
