import unittest
import random
from typing import List

class TestCase(unittest.TestCase):
    def test_sorted(self):
        actual = [x for x in range(10)] 
        arr = actual.copy()
        random.shuffle(arr)

        self.assertEqual(actual, bubble_sort1(arr.copy()))
        self.assertEqual(actual, bubble_sort2(arr.copy()))


def bubble_sort1(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 
    return arr

def bubble_sort2(arr: List[int]) -> List[int]:
    unsorted_until_index = len(arr)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        unsorted_until_index -= 1
    return arr

if __name__ == '__main__':
    unittest.main()
