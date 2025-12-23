"""
------------------------------------------------------------------------------------
Module Name: tree_visualization
------------------------------------------------------------------------------------
This module implements **visualization and formatted printing utilities**
for a Normal Binary Tree.

It is responsible for rendering a human-readable representation of the tree
structure using level-order (BFS) traversal and displaying tree metadata such
as root, size, and height.

This module does NOT perform:
- Tree mutation
- Tree validation
- Tree traversal logic (delegated to helpers)

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Pretty-print tree structure using BFS levels
- Decorate tree printing with headers, notes, and metadata
- Display parent → children relationships visually

------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- print_tree

------------------------------------------------------------------------------------
Decorators
------------------------------------------------------------------------------------
- pretty_print

------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _bfs_print
- _get_metadata_strings

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Visualization is read-only
- Tree structure must not be modified
- Traversal mechanics are delegated to structural helpers
- Output is intended for debugging and learning purposes
------------------------------------------------------------------------------------
"""

from functools import wraps

import structural_helpers
from schemas import Node, Tree

# ================================================================================
# Tree Visualization Decorators
# ================================================================================
def pretty_print(func):
    """
    Purpose: Decorator that adds formatted headers, notes, and metadata
             around tree visualization output.

    The decorator prints:
    - A formatted header
    - The tree structure (via wrapped function)
    - Legend and notes
    - Tree metadata (root, size, height)

    :param func: Tree printing function to decorate
    :return: Wrapped function with formatted output
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tree = args[0]

        meta_lines = _get_metadata_strings(tree)
        meta_max_left_widths = max([len(line) for line, _ in meta_lines], default=0)

        legend_lines = _get_legend_strings()
        legend_max_left_widths = max([len(line) for line, _ in legend_lines], default=0)

        width = 50
        title = " Binary Tree "
        header = title.center(width, '=')
        footer = "=" * width
        feed = "-" * width

        print(header)
        func(*args, **kwargs)
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
def print_tree(tree: Tree) -> None:
    """
    Purpose: Print a visual representation of the binary tree.

    The tree is printed level-by-level using BFS traversal,
    showing parent → children relationships.

    :param tree: Tree instance to be printed
    :return: None
    """
    if structural_helpers.is_tree_empty(tree):
        print("Tree is empty.")
        return

    _bfs_print([tree.root], 0)


# ================================================================================
# Internal Visualization Helpers
# ================================================================================
def _bfs_print(level_nodes: list[Node], level: int = 0) -> None:
    """
    Purpose: Recursively print tree nodes level-by-level using BFS.

    :param level_nodes: List of nodes at the current level
    :param level: Current tree depth level
    :return: None
    """
    if not level_nodes:
        return

    next_level = []
    for node in level_nodes:
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)
        children_values = [n.data for n in children if n is not None]
        children_str = ', '.join(children_values) if children else '**'
        print(f"\tLevel {level}: {node.data} → {children_str}")

    _bfs_print(next_level, level + 1)


def _get_metadata_strings(tree: Tree) -> list[tuple[str, str]]:
    """
    Purpose: Build formatted metadata strings for tree visualization.

    Metadata includes:
    - Root node
    - Tree size
    - Tree height (levels and edges)

    :param tree: Tree instance
    :return: List of (label, value) metadata tuples
    """
    return [
        ("Root Node", str(tree.root.data)),
        ("Size", f"{structural_helpers.compute_size(tree)}"),
        ("Height (Levels)", f"{structural_helpers.compute_height(tree)}"),
        ("Height (Edges)", f"{structural_helpers.compute_height(tree, True)}"),
        ("Edges", f"{structural_helpers.compute_edges(tree)}")
    ]

def _get_legend_strings():
    """
    Purpose: return legend lines
    :return: legend lines
    """
    return [
        ("Parent", "Children Relationship"),
        ("**", "Leaf node")
    ]