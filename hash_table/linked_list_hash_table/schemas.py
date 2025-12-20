"""
------------------------------------------------------------------------------------
Module Name: linked_list_hash_table_schemas
------------------------------------------------------------------------------------

This module defines the **schema layer** for a Hash Table implementation that
uses **separate chaining with singly linked lists** for collision handling.

The module is intentionally limited to **state representation and public API
exposure**, with all operational logic delegated to dedicated operations modules.

It provides:
- Node structure for storing key-value pairs
- LinkedList structure used as hash table buckets
- HashTable abstraction exposing dictionary-style access

All hashing logic, resizing logic, and linked list manipulation is implemented
in the corresponding operations modules.

------------------------------------------------------------------------------------
Design Principles
------------------------------------------------------------------------------------
- No business logic in schema classes
- No direct node manipulation outside operations layer
- Internal state protected via naming conventions (`_` prefix)
- HashTable is the only public entry point
- LinkedList acts as a pure state holder

------------------------------------------------------------------------------------
Data Structures
------------------------------------------------------------------------------------
- Node        -> Stores a single key-value pair and link to next node
- LinkedList -> Bucket container used for chaining
- HashTable  -> Hash table abstraction backed by linked list buckets

------------------------------------------------------------------------------------
Public Functions / Methods
------------------------------------------------------------------------------------
Node
- __init__ -> Initialize a node with key, value, and next reference

LinkedList
- __init__ -> Initialize an empty linked list bucket
- _get_size -> Return number of nodes in the linked list (internal use)

HashTable
- __init__ -> Initialize hash table with linked list buckets
- get_num_elements -> Return total stored elements
- get_size -> Return number of buckets
- get_load_factor -> Compute current load factor
- __setitem__ -> Insert or update a key-value pair
- __getitem__ -> Retrieve value for a given key
- __delitem__ -> Delete a key-value pair
- print_hash_table -> Print internal hash table structure

------------------------------------------------------------------------------------
"""

from typing import Any
from hash_table.linked_list_hash_table.operations import hash_operations

# ================================================================================
# Node
# ================================================================================
class Node:
    def __init__(self, key, value):
        """
        Purpose: Initialize a linked list node with a key-value pair
        :param key: Key associated with the value
        :param value: Value associated with the key
        :return: Nothing
        """
        self._key = key
        self._value = value
        self._next = None

# ================================================================================
# LinkedList (Bucket State Holder)
# ================================================================================
class LinkedList:
    def __init__(self):
        """
        Purpose: Initialize an empty linked list bucket
        :return: Nothing
        """
        self._head = None
        self._size = 0

    def _get_size(self):
        """
        Purpose: Return the number of nodes currently stored in the linked list
        :return: Number of nodes in the linked list
        """
        return self._size

# ================================================================================
# HashTable (Public Interface)
# ================================================================================
class HashTable:
    """
    Hash table implementation using separate chaining with linked lists.

    This class represents the public interface and state holder for the hash
    table. It exposes dictionary-style access for inserting, retrieving, and
    deleting key-value pairs while delegating all operational logic to the
    `hash_operations` module.

    Internal details such as hashing strategy, collision handling, resizing,
    and invariant enforcement are intentionally hidden from users.

    Invariants:
    - `_buckets` is a fixed-size list of LinkedList instances
    - `_num_elements` accurately reflects total stored key-value pairs
    - Load factor is derived as num_elements / number of buckets
    - No duplicate keys exist across buckets
    """
    def __init__(self):
        """
        Purpose: Initialize an empty hash table with linked list buckets
        :return: Nothing
        """
        self._buckets = self._create_buckets(5)
        self._num_elements = 0
        self.resize_threshold = 1.2

# ============== operations =================================================================
    # --------------------------------------------------------------------------
    # Internal helpers
    # --------------------------------------------------------------------------
    @staticmethod
    def _create_buckets(size):
        """
        Purpose: create hash table of provided size
        :param size: size of hash table
        :return: hash table
        """
        return [LinkedList() for _ in range(size)]

    # --------------------------------------------------------------------------
    # Metadata accessors
    # --------------------------------------------------------------------------
    def get_num_elements(self) -> int:
        """
        Purpose: Return the total number of key-value pairs stored in the hash table
        :return: Number of elements in the hash table
        """
        return self._num_elements

    def get_size(self) -> int:
        """
        Purpose: Return the number of buckets in the hash table
        :return: Hash table bucket count
        """
        return len(self._buckets)

    def get_load_factor(self) -> float:
        """
        Purpose: Compute the current load factor of the hash table
        :return: Load factor calculated as num_elements / table size
        """
        return self.get_num_elements() / self.get_size()

    def get_resize_threshold(self) -> float:
        """
        Purpose: return resize_threshold variable
        :return: resize_threshold
        """
        return self.resize_threshold

    # --------------------------------------------------------------------------
    # Public dictionary-style API
    # --------------------------------------------------------------------------
    def __setitem__(self, key, value) -> Any:
        """
        Purpose: Insert or update a key-value pair in the hash table
        :param key: Key to insert or update
        :param value: Value associated with the key
        :return: Result of insert operation
        """
        #new_node = Node(key, value)
        return hash_operations.insert_element(self, key, value)

    def __getitem__(self, key) -> Any:
        """
        Purpose: Retrieve the value associated with a given key
        :param key: Key to look up
        :return: Value associated with the key
        """
        return hash_operations.lookup_element(self, key)

    def __delitem__(self, key) -> Any:
        """
        Purpose: Delete a key-value pair from the hash table
        :param key: Key to delete
        :return: Result of delete operation
        """
        return hash_operations.delete_element(self, key)

    def print_hash_table(self) -> None:
        """
        Purpose: Print the internal structure of the hash table for inspection
        :return: Nothing
        """
        return hash_operations.print_hash_table(self)

#============================================================================================
