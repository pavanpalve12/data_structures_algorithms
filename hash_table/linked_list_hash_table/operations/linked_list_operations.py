"""
------------------------------------------------------------------------------------
Module Name: linked_list_operations
------------------------------------------------------------------------------------
This module implements **linked list–level operational logic** used by hash table
buckets for collision resolution.

It operates exclusively on LinkedList and Node instances and is completely
agnostic of hash table semantics.

This module is responsible for:
- Node insertion
- Node lookup by key
- Node deletion
- Maintaining linked list size and structure
- Preserving pointer correctness

No hashing logic exists in this module.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Insert nodes into a linked list
- Search for nodes by key
- Delete nodes by key
- Maintain linked list invariants
- Update linked list metadata
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- insert_node
- search_node
- delete_node
------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _check_invariants
- _is_empty
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a LinkedList instance as the first argument
- Node creation is handled outside this module
- No hash table metadata is accessed here
- No I/O is performed
------------------------------------------------------------------------------------
"""
from typing import Any

def insert_node(linked_list, key, value) -> str:
    """
    Purpose: Insert a node at the tail of the linked list
    :param linked_list: LinkedList instance representing a bucket
    :param key: Node(Key & Value associated with the key)
    :param value: Node(Key & Value associated with the key)
    :return: Result of insert operation
    """
    from hash_table.linked_list_hash_table.schemas import Node
    new_node = Node(key, value)
    curr_node = linked_list._head
    prev_node = None
    while curr_node and curr_node._key != new_node._key:
        prev_node = curr_node
        curr_node = curr_node._next

    # overwrite if key is found
    if curr_node:
        curr_node._value = new_node._value
        _check_invariants(linked_list)
        return True

    # insert at head if bucket is empty else insert at tail
    if linked_list._head == None:
        linked_list._head = new_node
    else:
        prev_node._next = new_node

    new_node._next = None
    linked_list._size += 1

    _check_invariants(linked_list)
    return True

def search_node(linked_list, key) -> Any:
    """
    Purpose: Search for a node in the linked list by key
    :param linked_list: LinkedList instance representing a bucket
    :param key: Key to search for
    :return: searched node
    """
    if _is_empty(linked_list):
        raise KeyError("Search Failed: the linked list is empty.")

    curr_node = linked_list._head
    while curr_node and curr_node._key != key:
        curr_node = curr_node._next

    if not curr_node:
        raise KeyError("Search Failed: key is not in linked list.")

    return curr_node._value

def delete_node(linked_list, key) -> bool:
    """
    Purpose: Delete a node from the linked list by key
    :param linked_list: LinkedList instance representing a bucket
    :param key: Key identifying the node to delete
    :return: Result of delete operation
    """
    if _is_empty(linked_list):
        raise KeyError("Deleted Failed: the linked list is empty.")

    curr_node = linked_list._head
    prev_node = None
    while curr_node and curr_node._key != key:
        prev_node = curr_node
        curr_node = curr_node._next

    if not curr_node:
        raise KeyError("Delete Failed: key is not in linked list")

    if curr_node == linked_list._head:
        linked_list._head = linked_list._head._next
    else:
        prev_node._next = curr_node._next
    curr_node._next = None
    linked_list._size -= 1

    _check_invariants(linked_list)
    return True

def _check_invariants(linked_list):
    """
    Purpose: Validate structural invariants of the linked list
    :param linked_list: LinkedList instance to validate
    :return: Nothing
    """
    temp_size = 0
    key, value = None, None
    curr_node = linked_list._head
    while curr_node:
        assert curr_node._key is not None and curr_node._value is not None, \
            "Invariant violated: hash table entry must have both key and value."

        temp_size += 1
        curr_node = curr_node._next

    assert temp_size == linked_list._size,\
        "Invariant violated: linked list size is incorrect."

def _is_empty(linked_list):
    """
    Purpose: checks if linked list is empty
    :param linked_list:
    :return:
    """
    if linked_list._size == 0 and linked_list._head == None:
        return True
    return False