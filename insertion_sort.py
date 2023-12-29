import unittest
import random
from typing import List


class TestCase(unittest.TestCase):
    def test_sorted(self):
        actual = list(range(10))
        arr = actual.copy()
        random.shuffle(arr)

        self.assertEqual(actual, insertion_sort1(arr.copy()))


def insertion_sort1(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        tmp_value = arr[i]
        position = i - 1

        while position >= 0:
            if arr[position] > tmp_value:
                arr[position + 1] = arr[position]
                position -= 1
            else:
                break
        arr[position + 1] = tmp_value
    return arr


if __name__ == "__main__":
    unittest.main()
