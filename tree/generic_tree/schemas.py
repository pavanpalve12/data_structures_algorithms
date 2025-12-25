"""
------------------------------------------------------------------------------------
Module: tree_schemas
------------------------------------------------------------------------------------

Schema definitions for a generic linked tree.

This module defines the **data structures only** for representing a tree.
It intentionally contains **no business logic, traversal logic, or validation**.

All operations on the tree are implemented in higher-level modules
(`tree_operations`, `tree_helpers`, `bst_api`).

Design goals:
- Represent structure, not behavior
- Keep nodes lightweight and mutable
- Enforce separation of concerns

------------------------------------------------------------------------------------
"""

from typing import Any, List, Optional


class Node:
    """
    Represents a single node in a generic tree.

    A Node stores:
    - its data value
    - references to child nodes
    - a reference to its parent node

    This class contains **no traversal, validation, or mutation logic**
    beyond maintaining structural relationships.
    """

    def __init__(self, data: Any):
        """
        Create a tree node with the given value.

        :param data: Value stored in the node
        """
        self.data = data
        self.children: List["Node"] = []
        self.parent: Optional["Node"] = None


class Tree:
    """
    Container object representing a tree.

    The Tree holds a reference to the root node and does not
    implement any operational logic. All tree behavior is
    delegated to other modules.
    """

    def __init__(self, root_node: Optional[Node] = None):
        """
        Create a tree with an optional root node.

        :param root_node: Root node of the tree, or None for an empty tree
        """
        self.root: Optional[Node] = root_node
