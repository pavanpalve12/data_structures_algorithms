"""
Module: insert
--------------------------
Provides insertion utility functions for singly linked lists.

This module defines helper functions that handle all insertion scenarios
in a singly linked list. It supports inserting nodes at the head, at the
end, before or after a specific node, and at a given index position.

Each function expects a `LinkedList` object that implements:
    • `head` – reference to the first node
    • `is_empty()` – method returning True if the list is empty
    • `get_last_node()` – method returning the last node
    • `get_node_by_value(value)` – method returning (prev_node, target_node)
    • `get_node_by_index(index)` – method returning (prev_node, target_node)

Functions:
    insert_node_at_head(ll_obj, new_node):
        Insert a new node at the head of the linked list.
    insert_node_at_end(ll_obj, new_node):
        Insert a new node at the tail (end) of the linked list.
    insert_node_after_node(ll_obj, new_node, target_node):
        Insert a new node immediately after a given node.
    insert_node_before_node(ll_obj, new_node, target_node):
        Insert a new node immediately before a given node.
    insert_node_at_index(ll_obj, new_node, index):
        Insert a new node at the specified index position.

Example:
    >>> ll = LinkedList()
    >>> node1 = Node(100)
    >>> node2 = Node(200)
    >>> insert_node_at_head(ll, node1)
    Linked list is empty, node 100 is added as head node
    >>> insert_node_at_end(ll, node2)
    node 200 is added after node 100 at the end.

Notes:
    - All insertions update internal node links accordingly.
    - Functions print confirmation messages for clarity during testing.
    - For production code, consider replacing print statements with
      logging calls.
"""

def insert_node_at_head(ll_obj, new_node):
    """
    Function: Insert node at head
    :param new_node: New node to be added
    :param ll_obj: LinkedList class object
    :param data: data value for the node
    :return: Nothing
    """
    if ll_obj.is_empty():
        ll_obj.head = new_node
        new_node.next = None
        print(
            "Linked list is empty, "
            f"node {new_node.data} is added as head node"
        )
    else:
        new_node.next = ll_obj.head
        ll_obj.head = new_node
        print(f"node {new_node.data} is added before head node {ll_obj.head.data}")


def insert_node_at_end(ll_obj, new_node):
    """
    Function: Insert node at end
    :param new_node: New node to be added
    :param ll_obj: LinkedList class object
    :param data: data value for the node
    :return: Nothing
    """
    _, last_node = ll_obj.get_last_node()
    last_node.next = new_node
    print(f"node {new_node.data} is added after node {ll_obj.head.data} at the end.")

def insert_node_after_node(ll_obj, new_node, target_node):
    """
    Function: Inserts node after target node
    :param ll_obj: LinkedList object
    :param new_node: new node to be added
    :param target_node: target node afte which new node will be added
    :return: Nothing
    """
    _, target_node = ll_obj.get_node_by_value(target_node)
    new_node.next = target_node.next
    target_node.next = new_node

    print(f"node {new_node.data} is added after node {target_node.data}.")

def insert_node_before_node(ll_obj, new_node, target_node):
    """
    Function: Inserts node before target node
    :param ll_obj: LinkedList object
    :param new_node: new node to be added
    :param target_node: target node before which new node will be added
    :return: Nothing
    """
    prev_node, target_node = ll_obj.get_node_by_value(target_node)
    new_node.next = target_node
    prev_node.next = new_node

    print(f"node {new_node.data} is added before node {target_node.data}.")

def insert_node_at_index(ll_obj, new_node, index):
    """
    Function: Inserts new node at target index
    :param ll_obj: LinkedList class object
    :param new_node: new node to be added
    :param index: target index
    :return: Nothing
    """
    prev_node, target_node = ll_obj.get_node_by_index(index)
    new_node.next = target_node
    prev_node.next = new_node

    print(f"node {new_node.data} is added at index {index}.")
