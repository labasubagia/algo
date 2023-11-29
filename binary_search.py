"""
This is learn for binary and linear search
using sorted array
return index when found otherwise None
"""

import unittest
from typing import List


class TestSearch(unittest.TestCase):
    def test_found(self):
        arr = [x for x in range(1, 101)]
        find, idx = 78, 77
        self.assertEqual(linear_search(arr, find), idx)
        self.assertEqual(binary_search(arr, find), idx)

    def test_not_found(self):
        arr = [x for x in range(1, 10)]
        find, idx = 78, None
        self.assertEqual(linear_search(arr, find), idx)
        self.assertEqual(binary_search(arr, find), idx)


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
