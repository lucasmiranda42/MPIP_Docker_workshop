# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""

Auxiliary functions for manin.py

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

        return to_sort
    return to_sort


def binary_search(sorted_array, x, low=0, high=None):
    """Searches for an element in a sorted array in O(log(n)) time"""

    if high is None:
        high = len(sorted_array)

    # Check base case
    if high >= low:

        try:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if sorted_array[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif sorted_array[mid] > x:
                return binary_search(sorted_array, x, low, mid - 1)

            # Else the element can only be present in right subarray
            else:
                return binary_search(sorted_array, x, mid + 1, high)

        except IndexError:
            return -1

    else:
        # Element is not present in the array
        return -1


def retrieve_element():
    pass
