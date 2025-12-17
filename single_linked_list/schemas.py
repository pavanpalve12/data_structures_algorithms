"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------

This module defines the core data structures and public API for a Singly Linked
List (SLL) implementation.

It provides:
- a Node abstraction with a forward reference
- a LinkedList container that manages the head pointer
- a complete set of list operations delegated to specialized submodules

The implementation emphasizes clarity, correctness, and modularity by
separating structural representation from operational logic.

------------------------------------------------------------------------------------
Data Structures
------------------------------------------------------------------------------------
- Node -> Represents a single element containing data and a next reference
- LinkedList -> Container managing the head pointer and exposing list operations

------------------------------------------------------------------------------------
Core Operations
------------------------------------------------------------------------------------
- is_empty -> Check whether the list contains any nodes
- traverse -> Traverse the list and return values, length, and string form
- print_linked_list -> Print the list in forward order
- clear -> Remove all nodes from the list
- get_length -> Return the total number of nodes

------------------------------------------------------------------------------------
Search Operations
------------------------------------------------------------------------------------
- get_last_node -> Return the last node and its previous node
- get_node_by_value -> Find a node by its value
- get_node_by_index -> Find a node by its index

------------------------------------------------------------------------------------
Insertion Operations
------------------------------------------------------------------------------------
- insert_node_at_head -> Insert a node at the beginning of the list
- insert_node_at_end -> Insert a node at the end of the list
- insert_node_after_node -> Insert a node after a target node
- insert_node_before_node -> Insert a node before a target node
- insert_node_at_index -> Insert a node at a specific index

------------------------------------------------------------------------------------
Removal Operations
------------------------------------------------------------------------------------
- remove_node_at_head -> Remove the first node
- remove_node_at_end -> Remove the last node
- remove_node_by_value -> Remove the first matching value
- remove_node_at_index -> Remove a node at a specific index
- remove_all_nodes -> Remove all nodes from the list

------------------------------------------------------------------------------------
Utility Operations
------------------------------------------------------------------------------------
- reverse_linked_list -> Reverse the list in place
- count_node_occurrences -> Count occurrences of a value
- find_middle_node -> Find the middle node(s)
- find_nth_from_last -> Find the nth node from the end
- merge_two_linked_lists -> Merge two linked lists
- detect_cycle -> Detect if the list contains a cycle
- remove_cycle -> Remove a detected cycle

------------------------------------------------------------------------------------
Helper Operations
------------------------------------------------------------------------------------
- to_list -> Convert the linked list to a Python list
- from_list -> Build the list from a Python list
- compare_lists -> Compare two linked lists for equality
- clone -> Create a deep copy of the linked list
- remove_duplicates -> Remove duplicate values
- get_max -> Return the maximum value in the list
- get_min -> Return the minimum value in the list
- print_reverse -> Print the list in reverse order without modification

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Node identity is preserved unless explicitly removed
- Operations manipulate links directly; data is not copied unnecessarily
- Cycle detection and removal utilities are included
- Logic is delegated to operation modules for maintainability and testability

------------------------------------------------------------------------------------
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
