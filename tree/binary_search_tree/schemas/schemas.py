"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------
This module defines the **core data schemas** for the Binary Search Tree (BST).

It contains lightweight, data-only classes that represent the fundamental
building blocks of the tree structure.

This module is intentionally minimal and contains:
- No traversal logic
- No mutation logic
- No validation logic

The classes defined here are used across operations, helpers, and invariants
to maintain a clean separation between **data representation** and **behavior**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Define the Node data structure
- Define the Tree container structure
------------------------------------------------------------------------------------
Public Classes
------------------------------------------------------------------------------------
- Node
- Tree
------------------------------------------------------------------------------------
Internal / Helper Classes
------------------------------------------------------------------------------------
None
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Classes hold state only (no business logic)
- Tree acts as a thin wrapper around the root node
- All operations are implemented externally
------------------------------------------------------------------------------------
"""

from typing import Any


# --------------------------------------------------------------------------
# Node - represents node in BST
# --------------------------------------------------------------------------
class Node:
    """
    Represents a single node in a Binary Search Tree.

    A node stores a value and references to its left and right children.
    It does not implement any traversal, mutation, or validation logic.
    """

    def __init__(self, data):
        """
        Initialize a Node instance.

        :param data: The value to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None


# --------------------------------------------------------------------------
# Tree - represents BST tree
# --------------------------------------------------------------------------
class Tree:
    """
    Represents a Binary Search Tree container.

    This class maintains a reference to the root node and enforces the
    concept of a single-rooted tree structure. All tree operations are
    implemented outside this class.
    """

    def __init__(self, root: Any = None):
        """
        Initialize a Tree instance.

        :param root: Optional root node of the tree.
        """
        self.root = root if root is not None else None
