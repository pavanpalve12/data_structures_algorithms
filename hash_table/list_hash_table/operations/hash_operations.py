"""
------------------------------------------------------------------------------------
Module Name: hash_operations
------------------------------------------------------------------------------------
- This module implements all operational logic for the HashTable data structure.
- It serves as the execution layer for hash table behavior while keeping the
    HashTable schema lightweight and focused solely on exposing the public API.
- All functions in this module operate on a HashTable instance and directly
    manipulate its underlying storage structure.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement core hash table operations using hashing and indexing
- Generate valid indices using hash(key)
- Insert, update, lookup, and delete key-value pairs
- Maintain hash table metadata such as element count
- Enforce correct key-based access semantics
------------------------------------------------------------------------------------
Core Hash Table Operations
------------------------------------------------------------------------------------
- generate_index -> Generate an index for a given key
- insert_key_value_in_hash -> Insert or update a key-value pair
- lookup_key_value_in_hash -> Retrieve value for a given key
- delete_key_value_in_hash -> Remove a key-value pair
------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_hash_table -> Print the internal hash table structure
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a HashTable instance as the first argument
- All hashing, indexing, and collision-handling logic lives here
- No function mutates schema-level definitions
- No I/O is performed except explicitly documented utilities
- Placeholder implementations are provided for incremental development
------------------------------------------------------------------------------------
"""
import re
from typing import Any

def _check_invariants(ht):
    # 1. Table size must never be zero
    assert ht.get_size() > 0, (
        "Invariant violated: Hash table size must be > 0."
    )

    actual_count = 0
    keys = set()

    # 2. Buckets must be lists
    for index, bucket in enumerate(ht.hash):
        assert isinstance(bucket, list), (
            f"Invariant violated: Bucket at index {index} "
            f"is not a list (found {type(bucket).__name__})."
        )

        for k, _ in bucket:
            # 3. Key must belong to its computed bucket
            computed_index = ht.get_index(k)
            assert computed_index == index, (
                f"Invariant violated: Key '{k}' is stored in bucket {index}, "
                f"but computed index is {computed_index}."
            )

            # 4. Keys must be unique across the table
            assert k not in keys, (
                f"Invariant violated: Duplicate key '{k}' found in hash table."
            )

            keys.add(k)
            actual_count += 1

    # 5. Metadata must reflect actual contents
    assert actual_count == ht.num_elements, (
        f"Invariant violated: num_elements={ht.num_elements}, "
        f"but actual stored elements={actual_count}."
    )

def generate_index(ht, key) -> int:
    """
    Purpose: Generate a valid index in the hash table using hash(key)
    :param ht: HashTable instance containing internal storage and metadata
    :param key: Key to be hashed
    :return: Computed index within hash table bounds

    hash(key)= (∑ ascii(each char in key)) % table size
    """
    ascii_sum = sum([ord(char) for char in key])
    index = ascii_sum % ht.get_size()
    return index

def insert_key_value_in_hash(ht, key, value, _resize_flag = False) -> bool:
    """
    Purpose: Insert or update a key-value pair in the hash table
    :param ht: HashTable instance containing internal storage and metadata
    :param key: Key to insert or update
    :param value: Value associated with the key
    :param _resize_flag: True if resize is triggered else False
    :return: True if insertion or update succeeds
    """
    if not _resize_flag:
        # check if next insert will trigger resize
        num_elements, size = ht.get_num_elements(), ht.get_size()
        alpha = (num_elements + 1) / size

        if alpha >= ht.get_resize_threshold():
            print("Resize is required")
            _resize_hash_table(ht)
            print(
                "Resizing complete"
                "New Table details:"
                f"\n\tSize = {ht.get_size()}, "
                f"\n\tNumber of elements = {ht.get_num_elements()}"
                f"\t\tLoad Factor = {ht.get_alpha():.2f}"
            )

    index = ht.get_index(key)
    bucket = ht.hash[index]

    for idx, (k, _) in enumerate(bucket):
        if key == k:
            print(
                f"Key '{key}' found in hash table: "
                f"overwritten with {(key, value)} at index = {index}."
            )
            bucket[idx] = (key, value)
            if not _resize_flag:
                _check_invariants(ht)
            return True

    bucket.append((key, value))
    ht.num_elements += 1
    print(
        f"Key '{key}' not found in hash table: "
        f"{(key, value)} is inserted at index = {index}."
    )
    if not _resize_flag:
        _check_invariants(ht)
    return True

def lookup_key_value_in_hash(ht, key) -> Any:
    """
    Purpose: Retrieve the value associated with a given key
    :param ht: HashTable instance containing internal storage
    :param key: Key to look up
    :return: Value mapped to the key if found
    """
    index = ht.get_index(key)
    bucket = ht.hash[index]
    for (k, v) in bucket:
        if key == k:
            return v

    raise KeyError(f"Lookup failed: key {key} is not in hash table.")

def delete_key_value_in_hash(ht, key) -> bool:
    """
    Purpose: Remove a key-value pair from the hash table
    :param ht: HashTable instance containing internal storage and metadata
    :param key: Key to delete
    :return: Result of delete operation
    """
    index = ht.get_index(key)
    bucket = ht.hash[index]

    for idx, (k, _) in enumerate(bucket):
        if key == k:
            print(f"Key '{key}' from bucket {index} is deleted.")
            del bucket[idx]
            ht.num_elements -= 1
            _check_invariants()
            return True

    raise KeyError(f"Lookup failed: key {key} is not in hash table.")

def _resize_hash_table(ht) -> bool:
    """
    Purpose: resizes the hash table if alpha >= 0.8 to 2x of old
    :return: True if success else False
    """
    old_hash_table = ht.hash
    old_hash_table_size = ht.get_size()
    ht.hash = [[] for _ in range(2 * old_hash_table_size)]
    ht.num_elements = 0

    for bucket in old_hash_table:
        for key, value in bucket:
            insert_key_value_in_hash(ht, key, value, _resize_flag = True)
    _check_invariants(ht)
    return True

def print_hash_table(ht):
    """
    Purpose: Print the internal structure of the hash table for inspection
    :param ht: HashTable instance containing internal storage
    :return: Printed representation of the hash table
    """

    # ---------- Prepare table data ----------
    rows = [(str(i), str(bucket)) for i, bucket in enumerate(ht.hash)]

    index_header = "index"
    bucket_header = "(key-value)"

    index_width = max(len(index_header), max(len(r[0]) for r in rows)) + 4
    bucket_width = max(len(bucket_header), max(len(r[1]) for r in rows)) + 4

    table_width = index_width + bucket_width + 3  # | + |

    feed_row = "-" * table_width

    # ---------- Metadata ----------
    TAB_WIDTH = 8
    meta_lines = [
        "Hash Function -> hash(key) = (∑ ascii(chars)) % size",
        f"Num elements  -> {ht.get_num_elements()}",
        f"Size of hash  -> {ht.get_size()}",
        f"Load Factor   -> {ht.get_alpha():.2f}",
    ]
    meta_width = max(
        TAB_WIDTH + len(f"{i}. ") + len(line)
        for i, line in enumerate(meta_lines, start=1)
    )
    header_width = max(table_width, meta_width)

    title = " Hash Table "
    header = title.center(header_width, "=")
    footer = "=" * header_width

    # ---------- Print ----------
    print(header)
    print(feed_row)

    # Column headers
    print(
        f"|{index_header.center(index_width)}"
        f"| {bucket_header.center(bucket_width - 1)}|"
    )
    print(feed_row)

    # Rows
    for idx, bucket in rows:
        print(
            f"|{idx.center(index_width)}"
            f"| {bucket.ljust(bucket_width - 1)}|"
        )

    print(feed_row)
    print(footer)

    # Metadata
    print("Hash Table Details:")
    for i, line in enumerate(meta_lines, start=1):
        print(f"\t{i}. {line}")

    print(footer)


