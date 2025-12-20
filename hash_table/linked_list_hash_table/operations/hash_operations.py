"""
------------------------------------------------------------------------------------
Module Name: hash_operations
------------------------------------------------------------------------------------
This module implements **hash table–level operational logic** for a HashTable
that uses **separate chaining with linked lists** for collision resolution.

It acts as the execution layer between the HashTable schema and the underlying
linked list bucket operations.

This module is responsible for:
- Computing hash indices
- Selecting appropriate buckets
- Delegating node-level operations to linked_list_operations
- Maintaining hash table metadata (element count)
- Enforcing hash table invariants
- Handling resizing and rehashing

No schema definitions are declared here.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Hash computation and index generation
- Insert, lookup, and delete operations at hash-table level
- Resize decision and rehash orchestration
- Load factor management
- Invariant validation

------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- insert_element
- lookup_element
- delete_element
- print_hash_table

------------------------------------------------------------------------------------
Internal / Helper Functions
------------------------------------------------------------------------------------
- _generate_index
- _resize_hash_table
- _check_invariants

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a HashTable instance as the first argument
- All linked list manipulation is delegated to linked_list_operations
- No direct node manipulation occurs here
- This module contains no I/O except optional debug utilities

------------------------------------------------------------------------------------
"""

import hash_table.linked_list_hash_table.operations.linked_list_operations as linked_list_operations

def insert_element(ht, key, value, _rehashing = False):
    """
    Purpose: Insert or update a key-value pair in the hash table
    :param ht: HashTable instance containing buckets and metadata
    :param _rehashing: True if resize is triggered else False
    :param key: Node(Key & Value associated with the key)
    :param value: Node(Key & Value associated with the key)
    :return: Result of insert operation
    """
    if not _rehashing:
        num_elements = ht.get_num_elements()
        table_size = ht.get_size()
        alpha = (num_elements + 1) / table_size

        if alpha >= ht.get_resize_threshold():
            _resize_hash_table(ht)
            print(
                "Resizing complete"
                f"\nNew Table details:"
                f"\n\tSize = {ht.get_size()}, "
                f"\n\tNumber of elements = {ht.get_num_elements()}"
                f"\t\tLoad Factor = {ht.get_load_factor():.2f}"
            )

    index = _generate_index(ht, key)
    bucket = ht._buckets[index]
    bucket_size = bucket._size

    linked_list_operations.insert_node(bucket, key, value)
    # increment hast table num of elements for insert only
    # for overwrite bucket size will remain same
    # diff between old and updated value dynamically increment num of elements
    ht._num_elements += (bucket._size - bucket_size)

    if not _rehashing:
        _check_invariants(ht)
    return True

def lookup_element(ht, key):
    """
    Purpose: Retrieve the value associated with a given key from the hash table
    :param ht: HashTable instance containing buckets
    :param key: Key to look up
    :return: Value associated with the key
    """
    index = _generate_index(ht, key)
    bucket = ht._buckets[index]

    return linked_list_operations.search_node(bucket, key)

def delete_element(ht, key):
    """
    Purpose: Remove a key-value pair from the hash table
    :param ht: HashTable instance containing buckets and metadata
    :param key: Key to delete
    :return: Result of delete operation
    """
    index = _generate_index(ht, key)
    bucket = ht._buckets[index]

    linked_list_operations.delete_node(bucket, key)
    ht._num_elements -= 1

    _check_invariants(ht)
    return True

def _generate_index(ht, key):
    """
    Purpose: Generate a bucket index for a given key using the hash function
    :param ht: HashTable instance containing table size information
    :param key: Key to be hashed
    :return: Computed bucket index

    hash(key)= (∑ ascii(each char in key)) % table size
    """
    ascii_sum = sum([ord(char) for char in key])
    index = ascii_sum % ht.get_size()
    return index

def _resize_hash_table(ht):
    """
    Purpose: Resize the hash table and rehash all existing elements
    :param ht: HashTable instance to be resized
    :return: Result of resize operation
    """
    old_hash_table = ht._buckets
    old_size = ht.get_size()
    new_size = old_size * 2
    ht._buckets = ht._create_buckets(new_size)
    ht._num_elements = 0

    for bucket in old_hash_table:
        curr_node = bucket._head
        while curr_node:
            print(f"key -> {curr_node._key} & value -> {curr_node._value}")
            insert_element(ht, curr_node._key, curr_node._value, _rehashing = True)
            curr_node = curr_node._next
    _check_invariants(ht)
    return True

def _check_invariants(ht):
    """
    Purpose: Validate structural and metadata invariants of the hash table
    :param ht: HashTable instance to validate
    :return: Nothing
    """
    # hash table size must be greater than 0
    assert ht.get_size() > 0, "Invariant violated: Hash table size must be > 0."

    actual_num_elements = 0
    keys = set()
    # buckets must be linked lists
    for index, bucket in enumerate(ht._buckets):
        assert hasattr(bucket, "_head") and hasattr(bucket, "_size"), \
            f"Invariant violated: Bucket at index {index} "\
            f"is not a linked list (found {type(bucket).__name__})."

        # key must belong to computed bucket
        curr_node = bucket._head
        while curr_node:
            computed_index = _generate_index(ht, curr_node._key)
            assert computed_index == index,\
                f"Invariant violated: Key '{curr_node._key}' is stored in bucket {index}, "\
                f"but computed index is {computed_index}."

            # keys must be unique
            assert curr_node._key not in keys,\
                f"Invariant violated: Duplicate key '{curr_node._key}' found in hash table."
            actual_num_elements += 1
            keys.add(curr_node._key)
            curr_node = curr_node._next

    # number of elements should match actual num elements
    assert actual_num_elements == ht.get_num_elements(),\
        f"Invariant violated: num_elements={ht.get_num_elements()}, "\
        f"but actual stored elements={actual_num_elements}."

def _get_bucket_as_strings(ht) -> list:
    """
    Purpose: traverses buckets and creates string representation
    :param ht: HashTable instance containing internal storage
    :return: list of strings
    """
    bucket_bodies = []
    for idx, bucket in enumerate(ht._buckets):
        body_str = f"Bucket {idx} → "
        curr_node = bucket._head
        while curr_node:
            body_str += f"({curr_node._key}, {curr_node._value}) → "
            curr_node = curr_node._next
        body_str += "None"
        bucket_bodies.append(body_str)
    return bucket_bodies

def _get_metadata_strings(ht) -> list:
    """
    Purpose: create metatdata strings from hash table metadata
    :param ht: HashTable instance containing internal storage
    :return:
    """
    meta_lines = [
        ("Hash Function", "hash(key) = (∑ ascii(chars)) % table size"),
        ("Num elements", f"{ht.get_num_elements()}"),
        ("Size of hash table", f"{ht.get_size()}"),
        ("Load Factor", f"{ht.get_load_factor():.2f}")
    ]
    return meta_lines

def _compute_max_width(bucket_bodies, meta_lines) -> int:
    max_meta_line_widths = max([len(left + right) + 3 for left, right in meta_lines])
    max_bucket_bodies_widths = max([len(body) for body in bucket_bodies])
    tab_width = 8
    width = max(max_bucket_bodies_widths, max_meta_line_widths) + tab_width
    return width

def print_hash_table(ht):
    """
    Purpose: Print the internal structure of the hash table for inspection
    :param ht: HashTable instance containing internal storage
    :return: Nothing
    """
    # -------------- preparing strings to be printed -----------------------
    bucket_bodies = _get_bucket_as_strings(ht)

    # -------------- meta lines for hash table metadata -----------------------
    meta_lines = _get_metadata_strings(ht)

    # --------------- calculate widths ----------------------------------------------
    max_left_widths = max([len(left) for left, _ in meta_lines])
    width = _compute_max_width(bucket_bodies, meta_lines)

    # --------------- header and footer lines ------------------------------------------
    title = "Hash Table"
    header = f"{title.center(width, '=')}"
    footer = "=" * width
    feed_row = "-" * width

    # --------------- print hash table ----------------------------------------------
    print(header)
    for body in bucket_bodies:
        print(body)

    print(feed_row)
    print("Hash Table Details:")
    for left, right in meta_lines:
        print(f"{left.ljust(max_left_widths)} → {right}")
    print(footer)

