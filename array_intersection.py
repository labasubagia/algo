import unittest
import random
from typing import List, Tuple
from collections import defaultdict


class TestCase(unittest.TestCase):
    def test_intersection(self):
        arr1 = list(range(1, 11))
        random.shuffle(arr1)

        arr2 = list(range(5, 16))
        random.shuffle(arr2)

        expected = sorted(list(set(arr1).intersection(arr2)))

        actual1, step1 = intersection1(arr1, arr2)
        self.assertEqual(expected, sorted(actual1))

        actual2, step2 = intersection2(arr1, arr2)
        self.assertEqual(expected, sorted(actual2))

        actual3, step3 = intersection3(arr1, arr2)
        self.assertEqual(expected, sorted(actual3))

        self.assertTrue(step1 >= step2 >= step3)
        print(step1, step2, step3)

    def test_no_intersection(self):
        arr1 = list(range(1, 11))
        random.shuffle(arr1)

        arr2 = list(range(11, 21))
        random.shuffle(arr2)

        expected = sorted(list(set(arr1).intersection(arr2)))

        actual1, step1 = intersection1(arr1, arr2)
        self.assertEqual(expected, sorted(actual1))

        actual2, step2 = intersection2(arr1, arr2)
        self.assertEqual(expected, sorted(actual2))

        actual3, step3 = intersection3(arr1, arr2)
        self.assertEqual(expected, sorted(actual3))

        self.assertTrue(step1 >= step2 >= step3)
        print(step1, step2, step3)


# O(n^2)
def intersection1(arr1: List[int], arr2: List[int]) -> Tuple[List[int], int]:
    result: List[int] = []
    step = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            step += 1
            if arr1[i] == arr2[j]:
                result.append(arr1[i])
    return result, step


# O(n^2) still better than `intersection1` on average/best case
# On worst case is same with `intersection1`
def intersection2(arr1: List[int], arr2: List[int]) -> Tuple[List[int], int]:
    result: List[int] = []
    step = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            step += 1
            if arr1[i] == arr2[j]:
                result.append(arr1[i])
                break
    return result, step


# O(n) or O(2n) time, O(n) space
def intersection3(arr1: List[int], arr2: List[int]) -> Tuple[List[int], int]:
    result: List[int] = []
    dict: defaultdict[int, int] = defaultdict(int)
    step = 0

    l1, l2 = len(arr1), len(arr2)
    for i in range(max(l1, l2)):
        step += 1
        if i < l1:
            dict[arr1[i]] += 1
        if i < l2:
            dict[arr2[i]] += 1

    for k, v in dict.items():
        step += 1
        if v >= 2:
            result.append(k)

    return result, step


if __name__ == "__main__":
    unittest.main()
