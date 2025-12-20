"""
------------------------------------------------------------------------------------
Module Name: hash_table_schemas
------------------------------------------------------------------------------------

This module defines the schema and public interface for a Hash Table implementation.

It exposes a lightweight container class responsible for:
- maintaining hash table state
- tracking size, element count, and load factor
- exposing dictionary-style access (__getitem__, __setitem__, __delitem__)
- delegating all hashing and collision-handling logic to the operations module

All hash table behavior, including hashing strategy, insertion, lookup,
deletion, and printing, is implemented in the `hash_operations` module.

------------------------------------------------------------------------------------
Data Structures
------------------------------------------------------------------------------------
- HashTable -> Hash table abstraction backed by an internal array

------------------------------------------------------------------------------------
Core Hash Table Operations
------------------------------------------------------------------------------------
- get_index -> Generate index for a given key
- __setitem__ -> Insert or update a key-value pair
- __getitem__ -> Retrieve value for a given key
- __delitem__ -> Delete a key-value pair
- get_num_elements -> Return number of stored elements
- get_size -> Return current table size
- get_alpha -> Return load factor

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_hash_table -> Print the internal hash table structure

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- This module contains no hashing or collision-resolution logic
- All operations are delegated to the operations layer
- Internal state is maintained via a backing list
- Dictionary-style interface is intentionally exposed
- This schema acts strictly as a state holder and interface

------------------------------------------------------------------------------------
"""

from typing import Any
from hash_table.list_hash_table.operations import hash_operations


class HashTable:
    def __init__(self):
        """
        Purpose: Initialize an empty hash table and its metadata
        :return: Nothing
        """
        self.hash = [[] for _ in range(5)]
        self.num_elements = 0
        self.resize_threshold = 0.8

# ============== Hash Operations ==========================================================
    def get_index(self, key) -> int:
        """
        Purpose: Generate index for hash table using hash(key)
        :param key:
        :return: integer index
        """
        return hash_operations.generate_index(self, key)

    def __setitem__(self, key, value) -> bool:
        """
        Purpose: Insert or update a key-value pair in the hash table
        :param key: key to be stored in hash table
        :param value: value associated with a key
        :return: return True if success else Error
        """
        return hash_operations.insert_key_value_in_hash(self, key, value)

    def __getitem__(self, key) -> Any:
        """
        Purpose: Retrieve the value associated with a given key
        :param key: lookup key
        :return: value associated with a key
        """
        return hash_operations.lookup_key_value_in_hash(self, key)

    def __delitem__(self, key):
        """
        Purpose: Delete a key-value pair from the hash table
        :param key: key to be deleted
        :return: True if success else Error
        """
        return hash_operations.delete_key_value_in_hash(self, key)

    def get_num_elements(self) -> int:
        """
        Purpose: Return the number of elements stored in the hash table
        :return: number of elements in hash table
        """
        return self.num_elements

    def get_size(self) -> int:
        """
        Purpose: Return the current size of the hash table
        :return: size of hash table
        """
        return len(self.hash)

    def get_alpha(self) -> float:
        """
        Purpose: Return the current load factor of the hash table
        :return: load factor of the hash table
        """
        return self.get_num_elements() / self.get_size()

    def get_resize_threshold(self):
        """
        Purpose: Return the resize threshold for hash table
        :return: resize threshold
        """
        return self.resize_threshold

    def print_hash_table(self):
        """
        Purpose: Print the internal structure of the hash table
        :return: Nothing
        """
        return hash_operations.print_hash_table(self)

# ===========================================================================================


