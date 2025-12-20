"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------

This module serves as the execution and demonstration entry point for the
Hash Table implementation using separate chaining with linked lists.

It initializes a HashTable instance, performs a sequence of insert operations,
and prints the internal structure of the hash table along with its metadata.

This module is intended for:
- validating end-to-end hash table behavior
- verifying collision handling via chaining
- visually inspecting bucket distribution
- confirming metadata correctness (size, load factor)

No core data structure logic is implemented here. All behavior is delegated to
the schema and operations layers.

------------------------------------------------------------------------------------
Execution Flow
------------------------------------------------------------------------------------
1. Create an empty HashTable instance
2. Insert multiple key-value pairs
3. Print the internal bucket structure
4. Display hash table metadata

------------------------------------------------------------------------------------
Sample Output
------------------------------------------------------------------------------------

============================= Hash Table =============================
Bucket 0 → (2025-12-18, 95.75) → None
Bucket 1 → (2025-12-19, 180.5) → None
Bucket 2 → None
Bucket 3 → (2025-12-20, 260.0) → (2025-12-16, 310.25) → None
Bucket 4 → (2025-12-17, 420.0) → None
--------------------------------------------------------------------
Hash Table Details:
Hash Function      → hash(key) = (∑ ascii(chars)) % table size
Num elements       → 5
Size of hash table → 5
Load Factor        → 1.00
====================================================================

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- This module contains no business logic
- Intended for debugging and demonstration only
- Not designed for production use
- Acts as a thin execution wrapper around the hash table API

------------------------------------------------------------------------------------
"""

from hash_table.linked_list_hash_table.schemas import HashTable

def main():
    ht = HashTable()

    data = [
        ("2025-12-20", 260.0),
        ("2025-12-19", 180.5),
        ("2025-12-18", 95.75),
        ("2025-12-17", 420.0),
        ("2025-12-16", 310.25),
    ]

    for key, value in data:
        ht[key] = value

    ht.print_hash_table()

    print(ht['2025-12-16'])
    print(ht['2025-12-19'])

    ht['2025-12-10'] = 230.90
    ht.print_hash_table()

    del ht['2025-12-17']
    del ht['2025-12-20']
    ht.print_hash_table()

if __name__ == '__main__':
    """
    Purpose: Execute and demonstrate hash table operations end-to-end
    :return: Nothing
    """
    main()