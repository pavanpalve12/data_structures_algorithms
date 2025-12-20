"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------

This module serves as the executable entry point for demonstrating and testing
the HashTable implementation.

It performs the following responsibilities:
- Instantiates a HashTable object
- Inserts a predefined set of key-value pairs
- Demonstrates hash table insertion behavior
- Displays the internal structure of the hash table
- Performs lookup operations using dictionary-style access

This module is intentionally kept minimal and imperative in nature, acting as
a driver script rather than containing any business logic.

------------------------------------------------------------------------------------
Execution Flow
------------------------------------------------------------------------------------
1. Create an empty HashTable instance
2. Define sample input data (date-based keys with float values)
3. Insert all key-value pairs into the hash table
4. Print the internal hash table structure
5. Perform lookup operations to verify correctness

------------------------------------------------------------------------------------
Sample Output (Hash Table Size = 3)
------------------------------------------------------------------------------------

====================== Hash Table ======================
--------------------------------------------------------
|  index  |        (key-value)                         |
--------------------------------------------------------
|    0    | [('2025-12-19', 180.5), ('2025-12-16', 310.25)] |
|    1    | [('2025-12-20', 260.0), ('2025-12-17', 420.0)]  |
|    2    | [('2025-12-18', 95.75)]                          |
--------------------------------------------------------
========================================================
Hash Table Details:
    1. Hash Function -> hash(key) = (∑ ascii(chars)) % size
    2. Num elements  -> 5
    3. Size of hash  -> 3
    4. Load Factor   -> 1.67
========================================================

260.0
180.5

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- This module contains no hash table logic
- All data structure behavior is delegated to the HashTable class
- Serves as a manual test harness and usage example
- Demonstrates collision handling via chaining
- Intended for learning, debugging, and demonstration purposes

------------------------------------------------------------------------------------
"""


from hash_table.list_hash_table.schemas import HashTable

def main():
    """
    Purpose: Run a simple demonstration of the HashTable implementation

    - Creates a HashTable instance
    - Inserts sample key-value pairs
    - Prints the internal hash table structure
    - Performs basic lookup operations

    :return: Nothing
    """
    ht = HashTable()
    data = [
        ("2025-12-20", 260.0),
        ("2025-12-19", 180.5),
        ("2025-12-18", 95.75),
        ("2025-12-17", 420.0),
        ("2025-12-16", 310.25)
    ]

    for key, value in data:
        ht[key] = value

    ht.print_hash_table()

if __name__ == '__main__':
    main()