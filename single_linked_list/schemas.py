"""
Module: schemas
---------------
Defines the foundational data structures for a singly linked list — the `Node` and
`LinkedList` classes — and integrates them with modular operation components.

This module serves as the **core schema layer** of the linked list package.
It establishes the object structure (`Node`, `LinkedList`) and delegates
implementation details to specialized operation modules.

Integrated operation modules:
    • core    → fundamental list utilities (traverse, print, clear, is_empty)
    • insert  → node insertion methods (head, tail, before/after node, at index)
    • remove  → node deletion methods (head, tail, by value, by index, all)
    • search  → node lookup methods (by index, by value, last node)
    • utility → extended utilities (reverse, middle, nth-from-last, merge, cycle ops)

-------------------------------------------------------------------------------
Classes
-------------------------------------------------------------------------------

Node
~~~~
Represents an individual node in the linked list.

Attributes:
    data (Any): Value stored in the node.
    next (Node | None): Pointer to the next node in the list.

-------------------------------------------------------------------------------

LinkedList
~~~~~~~~~~
Represents a singly linked list composed of `Node` objects.

Attributes:
    head (Node | None): The first node in the list.

Methods (grouped by category):
------------------------------

**Core Operations**
    - is_empty() -> bool
      Check whether the list is empty.

    - traverse() -> dict
      Return dictionary with keys: 'values', 'length', and 'str_repr'.

    - print_linked_list() -> None
      Print the linked list in readable format.

    - clear() -> bool
      Delete all nodes and reset the list.

    - get_length() -> int
      Return and print the total number of nodes.

**Search / Access Operations**
    - get_last_node() -> tuple[Node | None, Node]
      Return the last node and its previous node.

    - get_node_by_value(target_node: int) -> tuple[Node | None, Node]
      Find a node by value and return (previous_node, found_node).

    - get_node_by_index(index: int) -> tuple[Node | None, Node]
      Find a node by index (0-based) and return (previous_node, found_node).

**Insertion Operations**
    - insert_node_at_head(data: Any) -> None
      Insert a new node at the beginning of the list.

    - insert_node_at_end(data: Any) -> None
      Insert a new node at the end of the list.

    - insert_node_after_node(data: Any, target_node: int) -> None
      Insert a new node after a specific node (by value).

    - insert_node_before_node(data: Any, target_node: int) -> None
      Insert a new node before a specific node (by value).

    - insert_node_at_index(data: Any, index: int) -> None
      Insert a new node at a specific position (0-based index).

**Removal Operations**
    - remove_node_at_head() -> Node
      Remove the first node and return it.

    - remove_node_at_end() -> Node
      Remove the last node and return it.

    - remove_node_by_value(target_node: int) -> Node
      Remove a node by its value.

    - remove_node_at_index(index: int) -> Node
      Remove a node by index (0-based).

    - remove_all_nodes() -> None
      Remove all nodes from the list (alias for clear).

**Utility Operations**
    - reverse_linked_list() -> LinkedList
      Reverse the linked list in place.

    - count_node_occurrences(target_node: Any) -> int
      Count the number of nodes with the given data value.

    - find_middle_node() -> tuple[Node | None, Node]
      Find and return the middle node(s) of the list.

    - find_nth_from_last(n: int) -> Node
      Return the n-th node from the end (1-based index).

    - merge_two_linked_lists(other: LinkedList) -> Node
      Interleave (alternate) nodes from this list and another list.

    - detect_cycle() -> Node | None
      Detect a loop in the linked list; returns the node before the loop starts.

    - remove_cycle() -> LinkedList
      Break the detected cycle by setting the linking node’s `.next = None`.

-------------------------------------------------------------------------------
"""


from typing import Any

from single_linked_list.operations import core
from single_linked_list.operations import insert
from single_linked_list.operations import search
from single_linked_list.operations import remove
from single_linked_list.operations import utility
from single_linked_list.operations import helpers


# ----------------------- Node class -------------------------
class Node:
    """
    Purpose: Represents a single node in a singly linked list.
    Args: data (Any) – The data to store in the node.
    Returns: Node instance with `data` and `next=None`.
    """
    def __init__(self, data: Any):
        self.data = data
        self.next = None


# --------------------- Linked List class -------------------------
class LinkedList:
    """
    Purpose: Represents and manages a singly linked list.
    Args: None
    Returns: LinkedList instance with `head=None`.
    """
    def __init__(self):
        self.head = None

    # ------------ core methods ----------------
    def is_empty(self) -> bool:
        """
        Purpose: Check whether the linked list is empty.
        Args: None
        Returns: bool – True if the list is empty, else False.
        """
        return core.is_empty(self)

    def traverse(self) -> dict:
        """
        Purpose: Traverse the list and return node values and length.
        Args: None
        Returns: dict – Contains 'values', 'length', and 'str_repr'.
        """
        return core.traverse(self)

    def print_linked_list(self):
        """
        Purpose: Print the linked list nodes in order.
        Args: None
        Returns: None
        """
        core.print_linked_list(self)

    def clear(self):
        """
        Purpose: Remove all nodes and reset the linked list.
        Args: None
        Returns: bool – True if list cleared successfully.
        """
        return core.clear_linked_list(self)

    def get_length(self):
        """
        Purpose: Get the total number of nodes in the linked list.
        Args: None
        Returns: int – Length of the list.
        """
        return utility.get_length(self)

    # ------------- search methods --------------
    def get_last_node(self) -> (Node, Node):
        """
        Purpose: Get the last node and its previous node.
        Args: None
        Returns: tuple – (previous_node, last_node).
        """
        return search.get_last_node(self)

    def get_node_by_value(self, target_node: int) -> (Node, Node):
        """
        Purpose: Find a node by its data value.
        Args: target_node (int) – Value to search for.
        Returns: tuple – (previous_node, matching_node).
        """
        return search.get_node_by_value(self, target_node)

    def get_node_by_index(self, index: int) -> (Node, Node):
        """
        Purpose: Get the node at a specific index.
        Args: index (int) – Zero-based position in the list.
        Returns: tuple – (previous_node, target_node).
        """
        return search.get_node_by_index(self, index)

    # ------------- insert methods --------------
    def insert_node_at_head(self, data):
        """
        Purpose: Insert a new node at the beginning of the list.
        Args: data (Any) – Value to insert.
        Returns: None
        """
        new_node = Node(data)
        return insert.insert_node_at_head(self, new_node)

    def insert_node_at_end(self, data):
        """
        Purpose: Insert a new node at the end of the list.
        Args: data (Any) – Value to insert.
        Returns: None
        """
        new_node = Node(data)
        return insert.insert_node_at_end(self, new_node)

    def insert_node_after_node(self, data, target_node):
        """
        Purpose: Insert a new node after a specific target node.
        Args: data (Any), target_node (int) – Value and reference node.
        Returns: None
        """
        new_node = Node(data)
        return insert.insert_node_after_node(self, new_node, target_node)

    def insert_node_before_node(self, data, target_node):
        """
        Purpose: Insert a new node before a specific target node.
        Args: data (Any), target_node (int) – Value and reference node.
        Returns: None
        """
        new_node = Node(data)
        return insert.insert_node_before_node(self, new_node, target_node)

    def insert_node_at_index(self, data, index):
        """
        Purpose: Insert a new node at a given index.
        Args: data (Any), index (int) – Value and position.
        Returns: None
        """
        new_node = Node(data)
        return insert.insert_node_at_index(self, new_node, index)

    # ------------- remove methods --------------
    def remove_node_at_head(self) -> Node:
        """
        Purpose: Remove the first node in the list.
        Args: None
        Returns: Node – The removed node.
        """
        return remove.remove_node_at_head(self)

    def remove_node_at_end(self) -> Node:
        """
        Purpose: Remove the last node in the list.
        Args: None
        Returns: Node – The removed node.
        """
        return remove.remove_node_at_end(self)

    def remove_node_by_value(self, target_node) -> Node:
        """
        Purpose: Remove a node that matches a specific value.
        Args: target_node (Any) – Node value to remove.
        Returns: Node – The removed node.
        """
        return remove.remove_node_by_value(self, target_node)

    def remove_node_at_index(self, index) -> Node:
        """
        Purpose: Remove the node at a given index.
        Args: index (int) – Zero-based position in the list.
        Returns: Node – The removed node.
        """
        return remove.remove_node_at_index(self, index)

    def remove_all_nodes(self):
        """
        Purpose: Remove all nodes from the list.
        Args: None
        Returns: None
        """
        return remove.remove_all_nodes(self)

    # ------------- utility methods --------------
    def reverse_linked_list(self) -> Any:
        """
        Purpose: Reverse the linked list in place.
        Args: None
        Returns: LinkedList – The reversed list.
        """
        return utility.reverse_linked_list(self)

    def count_node_occurrences(self, target_node) -> int:
        """
        Purpose: Count how many nodes match a given value.
        Args: target_node (Any) – Value to count.
        Returns: int – Number of occurrences.
        """
        return utility.count_node_occurrences(self, target_node)

    def find_middle_node(self) -> (Node, Node):
        """
        Purpose: Find the middle node(s) of the linked list.
        Args: None
        Returns: tuple – (previous_middle, middle_node).
        """
        return utility.find_middle_node(self)

    def find_nth_from_last(self, n) -> Node:
        """
        Purpose: Get the nth node from the end.
        Args: n (int) – 1-based index from the tail.
        Returns: Node – The target node.
        """
        return utility.find_nth_from_last(self, n)

    def merge_two_linked_lists(self, other) -> Node:
        """
        Purpose: Merge this list with another linked list.
        Args: other (LinkedList) – Second linked list.
        Returns: Node – Head of the merged list.
        """
        return utility.merge_two_linked_lists(self, other)

    def detect_cycle(self) -> Node:
        """
        Purpose: Detect if the linked list contains a cycle.
        Args: None
        Returns: Node | None – Node where cycle detected, else None.
        """
        return utility.detect_cycle(self)

    def remove_cycle(self) -> Node:
        """
        Purpose: Remove a detected cycle from the linked list.
        Args: None
        Returns: LinkedList – Cycle-free linked list.
        """
        return utility.remove_cycle(self)

    # ------------- helper methods --------------
    def to_list(self) -> list:
        """
        Purpose: Convert the linked list into a standard Python list of node values.
        Args: None
        Returns: list – A list containing all node values in order.
        """
        return helpers.to_list(self)

    def from_list(self, data_list: list):
        """
        Purpose: Build or reset the linked list from a Python list of values.
        Args: data_list (list) – List of values to populate the linked list.
        Returns: LinkedList – The updated linked list instance.
        """
        return helpers.from_list(self, data_list)

    def compare_lists(self, other) -> bool:
        """
        Purpose: Compare this linked list with another for data equality with optional rules.
        Args:
            other (LinkedList) – The linked list to compare with.
        Returns: bool – True if both lists match under the chosen comparison rules, else False.
        """
        return helpers.compare_lists(self, other)

    def clone(self, source_obj):
        """
        Purpose: Create and return a deep copy of the linked list.
        Args: source obj
        Returns: LinkedList – A new linked list with identical data.
        """
        return helpers.clone(self, source_obj)

    def remove_duplicates(self):
        """
        Purpose: Remove duplicate values from the linked list.
        Args: None
        Returns: LinkedList – The updated linked list without duplicates.
        """
        return helpers.remove_duplicates(self)

    def get_max(self):
        """
        Purpose: Return the maximum data value stored in the linked list.
        Args: None
        Returns: Any – Maximum node value, or None if the list is empty.
        """
        return helpers.get_max(self)

    def get_min(self):
        """
        Purpose: Return the minimum data value stored in the linked list.
        Args: None
        Returns: Any – Minimum node value, or None if the list is empty.
        """
        return helpers.get_min(self)

    def print_reverse(self):
        """
        Purpose: Print the linked list nodes in reverse order without modifying the list.
        Args: None
        Returns: None
        """
        return helpers.print_reverse(self)
