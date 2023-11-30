"""
This is learn for binary and linear search
using sorted array
return index when found otherwise None
"""

import unittest
from typing import List
from random import choice


class TestSearch(unittest.TestCase):
    def test_found(self):
        arr = list(range(100))
        x = choice(arr)
        x_idx = arr.index(x)

        self.assertEqual(linear_search(arr, x), x_idx)
        self.assertEqual(binary_search(arr, x), x_idx)

    def test_not_found(self):
        arr = list(range(10))
        x, x_idx = 78, None
        self.assertEqual(linear_search(arr, x), x_idx)
        self.assertEqual(binary_search(arr, x), x_idx)


def binary_search(items: List[int], find: int):
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if find > items[mid]:
            left = mid + 1
        elif find < items[mid]:
            right = mid - 1
        else:
            return mid
    return None


def linear_search(items: List[int], find: int):
    for idx, item in enumerate(items):
        if item == find:
            return idx
    return None


if __name__ == "__main__":
    unittest.main()
