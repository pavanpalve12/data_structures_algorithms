"""
------------------------------------------------------------------------------------
Module Name: schemas
------------------------------------------------------------------------------------

This module defines the core data structures and public API for a fully featured
Doubly Linked List (DLL) implementation.

It provides:
- a Node abstraction with bidirectional links
- a DoubleLinkedList container that manages head and tail pointers
- a comprehensive set of operations delegated to specialized submodules

The design follows a clean separation of concerns:
- the DoubleLinkedList class exposes the public interface
- actual logic is implemented in dedicated operation modules
- all structural integrity rules are centrally enforced

------------------------------------------------------------------------------------
Data Structures
------------------------------------------------------------------------------------
- Node -> Represents a single list element with prev and next references
- DoubleLinkedList -> Container managing head and tail pointers and list state

------------------------------------------------------------------------------------
Core / Utility Operations
------------------------------------------------------------------------------------
- is_empty -> Check whether the list contains any nodes
- traverse -> Traverse list and collect basic structural information
- print_linked_list -> Print the list in a readable forward format
- clear -> Remove all nodes and reset the list

------------------------------------------------------------------------------------
Insertion Operations
------------------------------------------------------------------------------------
- insert_at_head -> Insert a new node at the beginning of the list
- insert_at_tail -> Insert a new node at the end of the list
- insert_at_index -> Insert a new node at a specific index
- insert_before_node -> Insert a node before a given node reference
- insert_after_node -> Insert a node after a given node reference
- insert_before_value -> Insert a node before the first occurrence of a value
- insert_after_value -> Insert a node after the first occurrence of a value
- insert_sorted_ascending -> Insert a node while maintaining ascending order
- insert_sorted_descending -> Insert a node while maintaining descending order

------------------------------------------------------------------------------------
Deletion Operations
------------------------------------------------------------------------------------
- delete_from_head -> Remove and return the head node
- delete_from_tail -> Remove and return the tail node
- delete_at_index -> Remove and return the node at a given index
- delete_node -> Remove a node using a direct node reference
- delete_by_value -> Remove the first node matching a value
- delete_before_node -> Remove the node immediately before a given node
- delete_after_node -> Remove the node immediately after a given node
- delete_all_occurrences -> Remove all nodes matching a value
- clear -> Remove all nodes from the list

------------------------------------------------------------------------------------
Traversal Operations
------------------------------------------------------------------------------------
- traverse_forward -> Traverse nodes from head to tail
- traverse_backward -> Traverse nodes from tail to head
- traverse_from_node_forward -> Traverse forward starting from a given node
- traverse_from_node_backward -> Traverse backward starting from a given node

------------------------------------------------------------------------------------
Search Operations
------------------------------------------------------------------------------------
- search_by_value -> Find the first node with a given value
- search_by_index -> Find the node at a specific index
- search_first_occurrence -> Find the first occurrence of a value
- search_last_occurrence -> Find the last occurrence of a value
- contains -> Check whether a value exists in the list
- get_last_node -> Return the tail node of the list

------------------------------------------------------------------------------------
Update / Modification Operations
------------------------------------------------------------------------------------
- update_node_value -> Update the value stored in a specific node
- update_value_at_position -> Update the value at a given index
- replace_all_occurrences -> Replace all matching values in the list
- swap_nodes -> Swap the positions of two nodes
- relink_nodes -> Move a node before another node without changing data

------------------------------------------------------------------------------------
Utility / Information Operations
------------------------------------------------------------------------------------
- to_list -> Convert the linked list to a Python list
- from_list -> Populate the list from a Python iterable
- get_length -> Return the number of nodes in the list
- get_middle_node -> Return the middle node of the list
- get_nth_from_start -> Return the nth node from the head
- get_nth_from_end -> Return the nth node from the tail

------------------------------------------------------------------------------------
Sorting Operations
------------------------------------------------------------------------------------
- sort_ascending -> Sort the list in ascending order (in-place)
- sort_descending -> Sort the list in descending order (in-place)

------------------------------------------------------------------------------------
Reordering / Structural Operations
------------------------------------------------------------------------------------
- reverse -> Reverse the list in place
- rotate -> Rotate the list left or right by k positions
- split -> Split the list into two independent lists at a given index
- merge -> Merge another list using append or alternate strategy

    Supported merge modes:
    - append -> Append the second list to the end of the first
    - alternate -> Interleave nodes from both lists

------------------------------------------------------------------------------------
Validation / Integrity Checks
------------------------------------------------------------------------------------
- validate_dll_structure -> Run all structural integrity validations
- check_forward_backward_consistency -> Verify next/prev pointer symmetry
- detect_cycle -> Detect cycles in the list
- verify_head_tail_integrity -> Ensure head.prev and tail.next are None

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All operations preserve node identity unless explicitly deleted
- Structural and sorting operations modify links only; node data is never copied
- Validation utilities are provided to detect corruption early
- The implementation favors correctness and clarity over implicit behavior

------------------------------------------------------------------------------------
"""

from double_linked_list.operations import (
    core, insert, search, delete, validations,
    update, reorder, helpers, traversal, sort
)

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
    def insert_at_head(self, value):
        """
        Function: inserts new node at head
        :return: Nothing
        """
        new_node = Node(value)
        return insert.insert_at_head(self, new_node)

    def insert_at_tail(self, value):
        """
        Function: inserts new node at tail
        :param value: new node value
        :return: nothing
        """
        new_node = Node(value)
        return insert.insert_at_tail(self, new_node)

    def insert_at_index(self, index, value):
        """
        Function: Inserts new node at an index
        :param index: target index
        :param value: new node value
        :return:
        """
        new_node = Node(value)
        return insert.insert_at_index(self, index, new_node)

    def insert_before_node(self, target_node_value, value):
        """
        Function: insert new node before node
        :param target_node_value: target node value
        :param value: new node value
        :return:Nothing
        """
        new_node = Node(value)
        return insert.insert_before_node(self, target_node_value, new_node)

    def insert_after_node(self, target_node_value, value):
        """
        Function: Inserts new node after a node
        :param target_node_value: target node value
        :param value: new node value
        :return: Nothing
        """
        new_node = Node(value)
        return insert.insert_after_node(self, target_node_value, new_node)

    def insert_before_value(self, target_value, value):
        """
        Function: inserts node before first occurrence of a value
        :param target_value: target node value
        :param value: new node value
        :return: nothing
        """
        new_node = Node(value)
        return insert.insert_before_value(self, target_value, new_node)

    def insert_after_value(self, target_value, value):
        """
        Function: inserts node after first occurrence of a value
        :param target_value: target node value
        :param value: new node value
        :return: nothing
        """
        new_node = Node(value)
        return insert.insert_after_value(self, target_value, new_node)

    def insert_sorted_ascending(self, value):
        """
        Function: Insert a new node while maintaining ascending sorted order
        :param value: new node value
        :return: nothing
        """
        new_node = Node(value)
        return insert.insert_sorted_ascending(self, new_node)

    def insert_sorted_descending(self, value):
        """
        Function: Insert a new node while maintaining descending sorted order
        :param value: new node value
        :return: nothing
        """
        new_node = Node(value)
        return insert.insert_sorted_descending(self, new_node)

# ----------- Deletion -------------------------------------------------------------------
    def delete_from_head(self) -> Node:
        """
        Function: Delete the first node (head) of the linked list
        :return: Deleted node if successful, otherwise None
        """
        return delete.delete_from_head(self)

    def delete_from_tail(self) -> Node:
        """
        Function: Delete the last node (tail) of the linked list
        :return: Deleted node if successful, otherwise None
        """
        return delete.delete_from_tail(self)

    def delete_at_index(self, index: int) -> Node:
        """
        Function: Delete a node at a specific index
        :param index: Zero-based position of the node to delete
        :return: Deleted node if successful, otherwise None
        """
        return delete.delete_at_index(self, index)

    def delete_node(self, target_node: Node) -> Node:
        """
        Function: Delete a specific node using direct reference
        :param target_node: Node to be deleted
        :return: Deleted node if successful, otherwise None
        """
        return delete.delete_node(self, target_node)

    def delete_by_value(self, value) -> Node:
        """
        Function: Delete the first occurrence of a value
        :param value: Value of the node to delete
        :return: Deleted node if found, otherwise None
        """
        return delete.delete_by_value(self, value)

    def delete_before_node(self, target_node: Node) -> Node:
        """
        Function: Delete the node immediately before a given node
        :param target_node: Node whose previous node will be deleted
        :return: Deleted node if successful, otherwise None
        """
        return delete.delete_before_node(self, target_node)

    def delete_after_node(self, target_node: Node) -> Node:
        """
        Function: Delete the node immediately after a given node
        :param target_node: Node whose next node will be deleted
        :return: Deleted node if successful, otherwise None
        """
        return delete.delete_after_node(self, target_node)

    def delete_all_occurrences(self, value) -> int:
        """
        Function: Delete all nodes containing a given value
        :param value: Value to remove from the list
        :return: Number of nodes deleted
        """
        return delete.delete_all_occurrences(self, value)

    def clear(self) -> None:
        """
        Function: Delete all nodes from the linked list
        :return: None
        """
        delete.delete_all_nodes(self)

# ----------- Traversal ------------------------------------------------------------------
    def traverse_forward(self):
        """
        Function: Traverse from head to tail
        :return: None
        """
        return traversal.traverse_forward(self)

    def traverse_backward(self):
        """
        Function: Traverse from tail to head
        :return: None
        """
        return traversal.traverse_backward(self)

    def traverse_from_node_forward(self, node):
        """
        Function: Traverse forward from a given node
        :param node: Starting node
        :return: None
        """
        return traversal.traverse_from_node_forward(self, node)

    def traverse_from_node_backward(self, node):
        """
        Function: Traverse backward from a given node
        :param node: Starting node
        :return: None
        """
        return traversal.traverse_from_node_backward(self, node)

# ----------- Search ---------------------------------------------------------------------
    def search_by_value(self, value):
        """
        Function: searches node by value
        :param value: target value
        :return: node
        """
        return search.search_by_value(self, value)

    def search_by_index(self, index):
        """
        Function: searches node by index
        :param index:target index
        :return: node
        """
        return search.search_by_index(self, index)

    def search_first_occurrence(self, value) -> Node:
        """
        Function: searches first occurrence of value
        :param value: first node with matching value
        :return: Node
        """
        return search.search_first_occurrence(self, value)

    def search_last_occurrence(self, value) -> Node:
        """
        Function: search for last occurrence of value
        :param value:last node with matching value
        :return: node
        """
        return search.search_last_occurrence(self, value)

    def contains(self, value) -> bool:
        """
        Function: checks if value is print in linked list
        :param value: target value
        :return: True is value is found else False
        """
        return search.contains(self, value)

    def get_last_node(self) -> Node :
        """
        Function: return last node of linked list
        :return: last node
        """
        return search.get_last_node(self)

# ----------- Update / Modification ------------------------------------------------------
    def update_node_value(self, node, new_value):
        """
        Function: Update the value stored in a given node
        :param node: Node whose value will be updated
        :param new_value: New value to assign to the node
        :return: None
        """
        return update.update_node_value(self, node, new_value)

    def update_value_at_position(self, position, new_value):
        """
        Function: Update the value at a given position
        :param position: Zero-based index in the list
        :param new_value: New value to assign
        :return: None
        """
        return update.update_value_at_position(self, position, new_value)

    def replace_all_occurrences(self, old_value, new_value):
        """
        Function: Replace all occurrences of a value in the list
        :param old_value: Value to be replaced
        :param new_value: Replacement value
        :return: Number of nodes updated
        """
        return update.replace_all_occurrences(self, old_value, new_value)

    def swap_nodes(self, node_a, node_b):
        """
        Function: Swap two nodes in the list
        :param node_a: First node
        :param node_b: Second node
        :return: None
        """
        return update.swap_nodes(self, node_a, node_b)

    def relink_nodes(self, node_a, node_b):
        """
        Function: Modify node links without changing node data
        :param node_a: First node involved in re-linking
        :param node_b: Second node involved in re-linking
        :return: None
        """
        return update.relink_nodes(self, node_a, node_b)

    # ----------- Utility / Information ------------------------------------------------------
    def to_list(self) -> list:
        """
        Function: Convert the linked list to a Python list
        :return: List containing node values in order
        """
        return helpers.to_list(self)

    def from_list(self, values):
        """
        Function: Create a doubly linked list from a Python list
        :param values: Iterable of values to populate the linked list
        :return: Doubly linked list instance
        """
        return helpers.from_list(self, values)

    def get_length(self) -> int:
        """
        Function: Get the number of nodes in the linked list
        :return: Total number of nodes
        """
        return helpers.get_length(self)

    def get_middle_node(self):
        """
        Function: Get the middle node of the linked list
        :return: Middle node if list is not empty, otherwise None
        """
        return helpers.get_middle_node(self)

    def get_nth_from_start(self, n):
        """
        Function: Get the nth node from the start of the linked list
        :param n: Zero-based index from the start
        :return: Node at the given position if found, otherwise None
        """
        return helpers.get_nth_from_start(self, n)

    def get_nth_from_end(self, n):
        """
        Function: Get the nth node from the end of the linked list
        :param n: Zero-based index from the end
        :return: Node at the given position if found, otherwise None
        """
        return helpers.get_nth_from_end(self, n)

# ----------- Reordering / Structural ----------------------------------------------------
    def reverse(self) -> None:
        """
        Function: Reverse the doubly linked list in place.
        After execution, the head becomes the tail and the order is fully reversed.
        :return: None
        """
        return reorder.reverse_list(self)

    def rotate(self, k: int) -> None:
        """
        Function: Rotate the doubly linked list by k positions.
        Positive k rotates to the right, negative k rotates to the left.
        :param k: Number of positions to rotate
        :return: None
        """
        return reorder.rotate_list(self, k)

    def split(self, position: int, new_dll):
        """
        Function: Split the doubly linked list at the given position.
        Returns two independent doubly linked lists.
        :param position: Index at which to split the list
        :param new_dll: Doubly linked list object for second part
        :return: Tuple of two doubly linked list objects
        """
        return reorder.split_list(self, position, new_dll)

    def merge(self, other_dll, mode) -> None:
        """
        Function: Merge another doubly linked list into this list.
        The merge strategy is defined by the reorder implementation.
        :param other_dll: Another doubly linked list to merge with
        :param mode: [append or alternate]
        :return: None
        """
        return reorder.merge_lists(self, other_dll, mode)

# ----------- Sorting --------------------------------------------------------------------
    def sort_ascending(self):
        """
        Sort the doubly linked list in ascending order.

        This method delegates the sorting logic to the sort module.
        It rearranges nodes (not just values) to maintain proper
        prev/next pointer integrity.

        Returns:
            None
        """
        return sort.sort_ascending(self)

    def sort_descending(self):
        """
        Sort the doubly linked list in descending order.

        This method delegates the sorting logic to the sort module.
        It rearranges nodes (not just values) while preserving
        correct bidirectional links.

        Returns:
            None
        """
        return sort.sort_descending(self)

    # ----------- Validation / Integrity -----------------------------------------------------
    def validate_dll_structure(self) -> bool:
        """
        Function: Perform a full structural validation of the doubly linked list.
        This wrapper delegates to the validation helper module.
        :return: True if the list passes all validation checks
        """
        return validations.validate_dll_structure(self)

    def check_forward_backward_consistency(self) -> bool:
        """
        Function: Verify forward and backward link consistency for all nodes.
        Ensures next/prev pointers are symmetric across the list.
        :return: True if links are consistent
        """
        return validations.check_forward_backward_consistency(self)

    def detect_cycle(self) -> bool:
        """
        Function: Detect cycles in the doubly linked list structure.
        Cycles indicate corruption and invalid list state.
        :return: True if no cycle is detected
        """
        return validations.detect_cycle(self)

    def verify_head_tail_integrity(self) -> bool:
        """
        Function: Verify head and tail boundary conditions.
        Ensures head.prev is None and tail.next is None.
        :return: True if head and tail pointers are valid
        """
        return validations.verify_head_tail_integrity(self)

