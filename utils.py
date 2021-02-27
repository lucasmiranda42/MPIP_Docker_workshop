# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""

Auxiliary functions for manin.py

"""


def sort_array(to_sort: list) -> list:
    """Sorts to_sort using the bubble sort algorithm"""

    sorted = to_sort.copy()

    for i in range(len(sorted)):

        for j in range(len(sorted) - 1):

            if sorted[j] > sorted[j + 1]:

                sorted[j], sorted[j + 1] = sorted[j + 1], sorted[j]

    return sorted


def binary_search(sorted_array: list, x: int, low: int = 0, high: int = None) -> int:
    """Searches for an element in a sorted array in O(log(n)) time"""

    if high is None:
        high = len(sorted_array)

    if high >= low:

        try:

            mid = (high + low) // 2

            if sorted_array[mid] == x:
                return mid

            elif sorted_array[mid] > x:
                return binary_search(sorted_array, x, low, mid - 1)

            else:
                return binary_search(sorted_array, x, mid + 1, high)

        except IndexError:
            return -1

    else:
        return -1
