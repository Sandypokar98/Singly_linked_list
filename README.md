# Singly Linked List Implementation in Python

## Overview

This project provides a Python implementation of a Singly Linked List (SLL). A singly linked list is a linear data structure where each element (node) contains data and a pointer to the next node in the sequence. This implementation includes fundamental operations such as insertion, deletion, traversal, searching, reversal, sorting, and concatenation.

## Class Structure

The implementation consists of two classes:-

* **`Node`:** Represents an individual node within the linked list.
* **`SLL`:** Represents the Singly Linked List itself, containing a reference to the first node and methods to manipulate the list.

## `Node` Class

### Description

The `Node` class is a building block for the `SLL`. Each `Node` object holds a piece of data (`item`) and a reference (`next`) to the subsequent node in the list.

### Attributes

* `item`: Stores the data associated with the node. Can be of any data type. Defaults to `None`.
* `next`: A reference to the next `Node` object in the linked list. If it's the last node, `next` will be `None`. Defaults to `None`.

### Methods

* `__init__(self, item=None, next=None)`:
    * Initializes a new `Node` object.
    * **Parameters:**
        * `item` (optional): The data to be stored in the node.
        * `next` (optional): The next node in the linked list.

## `SLL` Class

### Description

The `SLL` class manages a collection of `Node` objects, forming a singly linked list. It provides methods to perform various operations on the list.

### Attributes

* `start`: A reference to the first `Node` in the linked list (the head). If the list is empty, `start` is `None`. Initialized to `None` by default.

### Methods

* `__init__(self, start=None)`:
    * Initializes an empty `SLL` object, optionally with a starting node.
    * **Parameters:**
        * `start` (optional): The initial starting `Node` for the list.

* `is_empty(self)`:
    * Checks if the linked list contains any nodes.
    * **Returns:** `True` if the list is empty (`self.start` is `None`), `False` otherwise.

* `insert_at_start(self, data)`:
    * Adds a new node with the given `data` at the beginning of the list.
    * **Parameters:**
        * `data`: The data to be stored in the new node.

* `insert_at_last(self, data)`:
    * Adds a new node with the given `data` at the end of the list.
    * **Parameters:**
        * `data`: The data to be stored in the new node.

* `traverse(self, data)`:
    * Searches for the first node containing the specified `data`.
    * **Parameters:**
        * `data`: The data to search for.
    * **Returns:** The first `Node` object containing the `data` if found, otherwise `None`.
    * **Note:** While named `traverse`, this method primarily serves as a search utility.

* `insert_after(self, data1, data2)`:
    * Inserts a new node with `data2` after the first node containing `data1`.
    * **Parameters:**
        * `data1`: The data of the node after which the insertion will occur.
        * `data2`: The data to be stored in the new node.

* `print_list(self)`:
    * Prints the data (`item`) of each node in the list sequentially, separated by spaces. If the list is empty, it prints "Empty".

* `del_last(self)`:
    * Removes the last node from the list.
    * **Error Handling:** Prints an error message if the list is empty.

* `del_first(self)`:
    * Removes the first node from the list.
    * **Error Handling:** Prints a message if the list is already empty.

* `del_item(self, data)`:
    * Removes the first node containing the specified `data`.
    * **Parameters:**
        * `data`: The data of the node to be deleted.
    * **Error Handling:** Prints an error message if the list is empty. For lists with more than one node, it doesn't explicitly state if the item is not found.

* `del_all(self)`:
    * Removes all nodes from the list, making it empty.

* `length(self)`:
    * Calculates and returns the number of nodes in the linked list.
    * **Returns:** An integer representing the length of the list.

* `search(self, data)`:
    * Searches for the first occurrence of the given `data` and returns its index (0-based).
    * **Parameters:**
        * `data`: The data to search for.
    * **Returns:** The index of the first node containing the `data` if found, otherwise -1. Prints a message if the data is not present or if the list is empty.

* `reverse(self)`:
    * Reverses the order of the nodes in the linked list in-place.
    * **Error Handling:** Prints a message if the list is empty.

* `sort(self)`:
    * Sorts the linked list in ascending order based on the `item` attribute using the bubble sort algorithm.
    * **Efficiency:** Bubble sort is not the most efficient sorting algorithm for linked lists, especially for large lists. Consider more efficient algorithms like merge sort for better performance in such cases.
    * **Message:** Prints a message if the list has 0 or 1 element.

* `concat(self, l_list)`:
    * Appends all nodes from another `SLL` (`l_list`) to the end of the current list.
    * **Parameters:**
        * `l_list`: The `SLL` object to be concatenated.
    * **Message:** Prints a message if the provided list is empty.
