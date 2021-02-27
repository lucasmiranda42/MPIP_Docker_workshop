# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""



"""

import numpy as np


def sort_array(to_sort: np.ndarray) -> np.ndarray:
    """Sorts to_sort using the merge sort algorithm"""

    if len(to_sort) > 1:
        mid = len(to_sort) // 2
        left = to_sort[:mid]
        right = to_sort[mid:]

        # Recursive call on each half
        sort_array(left)
        sort_array(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                to_sort[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                to_sort[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1


def binary_search():
    pass


def retrieve_element():
    pass
