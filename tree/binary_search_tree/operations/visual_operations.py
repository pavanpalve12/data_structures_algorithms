"""
------------------------------------------------------------------------------------
Module Name: visual_operations
------------------------------------------------------------------------------------
This module implements **visualization and pretty-printing utilities** for a
Binary Search Tree (BST).

It provides decorators and helper functions to render the tree structure,
relationships, and metadata in a human-readable format for debugging,
learning, and inspection purposes.

This module is responsible only for **presentation** and does not mutate
the tree or enforce invariants.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Pretty-print tree structure level by level
- Display parent–child relationships
- Display computed tree metadata
- Provide legend and formatting utilities
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- print_tree
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- pretty_print
- _get_metadata_strings
- _get_legend_strings
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Visualization relies on precomputed metadata
- Output is printed to stdout
- No mutation or validation logic is implemented here
- Intended for debugging and educational use
------------------------------------------------------------------------------------
"""

from functools import wraps
from typing import Tuple, List, Dict

from tree.binary_search_tree.schemas.schemas import Tree, Node
from tree.binary_search_tree.helpers import (
    structural_helpers as str_help,
    state_helpers as stt_help
)


# ================================================================================
# Tree Visualization Decorators
# ================================================================================
def pretty_print(func):
    """
    Decorator to format and pretty-print tree metadata.

    This decorator wraps a function that returns tree metadata and renders
    a structured, human-readable representation of the tree, including:
    - parent–child relationships
    - depth information
    - tree statistics and legend

    :param func: Function that returns tree metadata.
    :return: Wrapped function that prints formatted output.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        metadata = func(*args, **kwargs)
        child_map = metadata["child_map"]
        depth_map = metadata["depth_map"]

        child_values = {
            f"\tLevel {depth_map[parent]}: "
            f"{str(parent.data).rjust(2, ' ')}".ljust(13, ' '): (
                f"→ [{', '.join([str(c.data) for c in children])}]"
                if children else '→ **'
            )
            for parent, children in child_map.items()
        }

        result = "\n".join(
            f"{parent}{children}" for parent, children in child_values.items()
        )

        meta_lines = _get_metadata_strings(metadata)
        meta_max_left_widths = max([len(line) for line, _ in meta_lines], default=0)

        legend_lines = _get_legend_strings()
        legend_max_left_widths = max([len(line) for line, _ in legend_lines], default=0)

        width = 50
        title = " Binary Search Tree "
        header = title.center(width, '=')
        footer = "=" * width
        feed = "-" * width

        print(header)
        print(result)
        print(feed)
        print("\tLegend: ")
        for left, right in legend_lines:
            print(f"\t - {left.ljust(legend_max_left_widths, ' ')} → {right}")
        print(feed)
        for left, right in meta_lines:
            print(f"\t{left.ljust(meta_max_left_widths, ' ')} → {right}")
        print(footer)

    return wrapper


# ================================================================================
# Public Visualization API
# ================================================================================
@pretty_print
def print_tree(tree: Tree) -> Dict:
    """
    Print a visual representation of the Binary Search Tree.

    This function computes tree metadata and delegates rendering to the
    pretty_print decorator.

    :param tree: Tree instance to be printed.
    :return: Metadata dictionary used for visualization.
    """
    if str_help._is_empty_tree(tree):
        print('BST is empty.')
        return None

    metadata = stt_help._compute_metadata(tree)
    return metadata


# ================================================================================
# Internal Visualization Helpers
# ================================================================================
def _get_metadata_strings(metadata: Dict) -> List[Tuple[str, str]]:
    """
    Build formatted metadata strings for display.

    :param metadata: Metadata dictionary computed from the tree.
    :return: List of (label, value) tuples for tree metadata.
    """
    return [
        ("Root Node", metadata["bfs"][0].data),
        ("Size", f"{metadata['size']}"),
        ("Height (Levels)", f"{metadata['height_levels']}"),
        ("Height (Edges)", f"{metadata['height_edges']}"),
        ("Edges", f"{metadata['edge_count']}"),
        ("Min Node", f"{metadata['min_node'].data}"),
        ("Max Node", f"{metadata['max_node'].data}")
    ]


def _get_legend_strings():
    """
    Build legend strings explaining the tree visualization.

    :return: List of (symbol, description) tuples.
    """
    return [
        ("Parent", "Children Relationship"),
        ("**", "Leaf node")
    ]
