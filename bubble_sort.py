import unittest
import random
from typing import List

class TestCase(unittest.TestCase):
    def test_sorted(self):
        actual = [x for x in range(10)] 
        arr = actual.copy()
        random.shuffle(arr)

        expected1 = bubble_sort1(arr)
        self.assertEqual(actual, expected1)


def bubble_sort1(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    unittest.main()
