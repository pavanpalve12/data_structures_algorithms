"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------

This module defines the core data structures required to build and manage
a doubly linked list, including nodes with bidirectional links and a list
container that tracks the head of the list.

The implementation is intentionally minimal and focuses on structural
representation rather than full list operations.
------------------------------------------------------------------------------------
"""

from double_linked_list.operations import core

class Node:
    """
    Represents a single node in a doubly linked list.

    Each node stores a data element and maintains references to both the
    previous and next nodes in the list. Nodes do not manage list-level
    behavior; they exist solely as structural elements.
    """

    def __init__(self, data):
        """
        Initialize a node with data and empty links.

        Args:
            data: The value stored in the node. No type restrictions are
                  enforced; responsibility for data consistency lies with
                  the caller.
        """
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    """
    Container for a doubly linked list.

    This class maintains a reference to the head of the list. It does not
    impose constraints on node insertion, removal, or traversal logic,
    which must be implemented separately.
    """

    def __init__(self):
        """
        Initialize an empty doubly linked list.

        The list starts with no nodes and a head reference set to None.
        """
        self.head = None
        self.tail = None

# ----------- Core Functions ------------------------------------------------------------
    def is_empty(self) -> bool:
        """
        Function: check if dll is empty
        :return: True if empty else False
        """
        return core.is_empty(self)

    def traverse(self) -> dict:
        """
        Function: traverse dll and collect basic info
        :return: basic info in dict format
        """
        return core.traverse(self)

    def print_linked_list(self):
        """
        Function: print linked list
        :return: Nothing
        """
        return core.print_linked_list(self)

    def clear(self) -> bool:
        """
        Function: removes all nodes from linked list
        :return:
        """
        return core.clear(self)

# ----------- Insertion ------------------------------------------------------------------

# ----------- Deletion -------------------------------------------------------------------

# ----------- Traversal ------------------------------------------------------------------

# ----------- Search ---------------------------------------------------------------------

# ----------- Update / Modification ------------------------------------------------------

# ----------- Utility / Information ------------------------------------------------------

# ----------- Reordering / Structural ----------------------------------------------------

# ----------- Sorting --------------------------------------------------------------------

# ----------- Validation / Integrity -----------------------------------------------------

# ----------- Conversion / Transformation ------------------------------------------------

# ----------- Advanced / Use-case Specific ------------------------------------------------


