import unittest
from typing import List, Tuple, Any, Dict
import random


class TestCase(unittest.TestCase):
    def test_is_subset(self):
        arr1 = list(range(1000))
        random.shuffle(arr1)

        arr2 = list(range(2000))
        random.shuffle(arr2)

        expected = set(arr1).issubset(arr2)

        actual1, step1 = is_subset1(arr1, arr2)
        self.assertEqual(expected, actual1)

        actual2, step2 = is_subset2(arr1, arr2)
        self.assertEqual(expected, actual2)

        print(step1, step2)

    def test_is_not_subset(self):
        arr1 = list(range(1000))
        random.shuffle(arr1)

        arr2 = list(range(1001, 2000))
        random.shuffle(arr2)

        expected = set(arr1).issubset(arr2)

        actual1, step1 = is_subset1(arr1, arr2)
        self.assertEqual(expected, actual1)

        actual2, step2 = is_subset2(arr1, arr2)
        self.assertEqual(expected, actual2)

        print(step1, step2)


# O(m*n) -> O(n^2)
def is_subset1(arr1: List[Any], arr2: List[Any]) -> Tuple[bool, int]:
    larger = arr1
    smaller = arr2
    if len(arr2) > len(arr1):
        larger = arr2
        smaller = arr1

    step = 0
    for i in range(len(smaller)):
        found_match = False
        for j in range(len(larger)):
            step += 1
            if smaller[i] == larger[j]:
                found_match = True
                break
        if not found_match:
            return False, step

    return True, step


# O(n1+n2) -> O(n)
def is_subset2(arr1: List[Any], arr2: List[Any]) -> Tuple[bool, int]:
    larger = arr1
    smaller = arr2
    if len(arr2) > len(arr1):
        larger = arr2
        smaller = arr1
    step = 0

    larger_map: Dict[Any, bool] = {}
    for x in larger:
        step += 1
        larger_map[x] = True

    for x in smaller:
        step += 1
        if x not in larger_map:
            return False, step

    return True, step


if __name__ == "__main__":
    unittest.main()
