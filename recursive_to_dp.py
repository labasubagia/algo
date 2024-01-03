"""
DP chapters
avoid call recursive function more than once
it will drove to complexity of O(2^n)
"""

import unittest
import random


class TestCase(unittest.TestCase):
    def test_max_increase(self):
        arr = list(range(10))
        expected = max(arr)

        actual1, step1 = max1(arr)
        self.assertEqual(expected, actual1)

        actual2, step2 = max2(arr)
        self.assertEqual(expected, actual2)

        print("increase", step1, step2)

    def test_max_decrease(self):
        arr = list(range(10))
        arr.reverse()
        expected = max(arr)

        actual1, step1 = max1(arr)
        self.assertEqual(expected, actual1)

        actual2, step2 = max2(arr)
        self.assertEqual(expected, actual2)

        print("decrease", step1, step2)

    def test_max_shuffled(self):
        arr = list(range(10))
        random.shuffle(arr)
        expected = max(arr)

        actual1, step1 = max1(arr)
        self.assertEqual(expected, actual1)

        actual2, step2 = max2(arr)
        self.assertEqual(expected, actual2)

        print("shuffled", step1, step2)


# O(2^n) on decrease array
def max1(arr: list[int], step: int = 0) -> tuple[int, int]:
    step += 1
    if len(arr) == 1:
        return arr[0], step
    (next, step) = max1(arr[1 : len(arr)], step)
    if arr[0] > next:
        return arr[0], step
    return max1(arr[1 : len(arr)], step)


# little fix
def max2(arr: list[int], step: int = 0) -> tuple[int, int]:
    step += 1
    if len(arr) == 1:
        return arr[0], step
    (next, step) = max2(arr[1 : len(arr)], step)
    if arr[0] > next:
        return arr[0], step
    return next, step


if __name__ == "__main__":
    unittest.main()
