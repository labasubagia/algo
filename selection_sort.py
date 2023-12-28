import unittest
import random
from typing import List


class TestCase(unittest.TestCase):
    def test_sorted(self):
        actual = [x for x in range(10)]
        arr = actual.copy()
        random.shuffle(arr)

        self.assertEqual(actual, selection_sort1(arr.copy()))


def selection_sort1(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        lowest_index_number = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_index_number]:
                lowest_index_number = j
        if lowest_index_number != i:
            arr[i], arr[lowest_index_number] = arr[lowest_index_number], arr[i]
    return arr


if __name__ == "__main__":
    unittest.main()
