"""
------------------------------------------------------------------------------------
Module Name: tree_schemas
------------------------------------------------------------------------------------

This module defines the **schema (state) layer** for a Normal Binary Tree.

It contains the core data structures used to represent the tree:
- individual nodes
- the tree container holding the root

This module is intentionally limited to **state representation only**.
It does not implement insertion, deletion, traversal, or validation logic.

All behavioral logic is delegated to higher-level modules such as:
- operations
- helpers
- invariant
- tree_api

------------------------------------------------------------------------------------
Classes Defined
------------------------------------------------------------------------------------
- Node -> Represents a single binary tree node (state only)
- Tree -> Represents the binary tree container holding the root node

------------------------------------------------------------------------------------
"""

from typing import Any


class Node:
    """
    Represents a single node in a Normal Binary Tree.

    This class is a **pure data holder** and defines only structural state.
    It does not implement any tree logic such as insertion, deletion,
    traversal, or validation.

    Attributes conceptually represented:
    - data  : value stored in the node
    - left  : reference to left child node
    - right : reference to right child node
    """

    def __init__(self, data: Any) -> None:
        """
        Purpose: Initialize a binary tree node with a value
        :param data: Value to be stored in the node
        :return: None
        """
        self.data = data
        self.left = None
        self.right = None


class Tree:
    """
    Represents a Normal Binary Tree container.

    This class acts as a thin wrapper around the root node and enforces
    the concept of a **single-rooted tree structure**.

    No tree operations are implemented in this class.
    """

    def __init__(self, root_node: Node) -> None:
        """
        Purpose: Initialize a binary tree with a root node
        :param root_node: Root node of the tree
        :return: None
        """
        self.root = root_node
