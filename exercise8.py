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

        arr3 = list(range(15, 21))
        random.shuffle(arr3)

        expected = sorted(list(set(arr1).intersection(arr2).intersection(arr3)))

        actual, _ = intersection(arr1, arr2, arr3)
        self.assertEqual(expected, sorted(actual))

    def test_duplicate(self):
        arr = ["a", "b", "c", "d", "d", "e"]
        self.assertEqual("d", first_duplicate(arr))

        arr = ["a", "b", "c"]
        self.assertEqual(None, first_duplicate(arr))

    def test_missing_letter(self):
        text = "the quick brown box jumps over a lazy dog"
        self.assertEqual("f", missing_letter(text))

    def test_first_no_duplicate(self):
        text = "minimum"
        self.assertEqual("n", first_non_duplicate(text))


# O(n)
# just want to learn to use 3 arr
def intersection(
    arr1: List[int], arr2: List[int], arr3: List[int]
) -> Tuple[List[int], int]:
    result: List[int] = []
    steps = 0
    map: defaultdict[int, int] = defaultdict(int)

    l1, l2, l3 = len(arr1), len(arr2), len(arr3)
    for i in range(max(l1, l2, l3)):
        steps += 1
        if i < l1:
            map[arr1[i]] += 1
        if i < l2:
            map[arr2[i]] += 1
        if i < l3:
            map[arr3[i]] += 1

    for k, v in map.items():
        steps += 1
        if v >= 3:
            result.append(k)

    return result, steps


# O(n)
def first_duplicate(arr: List[str]) -> str | None:
    map: defaultdict[str, int] = defaultdict(int)
    for x in arr:
        if map[x] == 1:
            return x
        map[x] += 1
    return None


# O(n)
def missing_letter(text: str) -> str | None:
    map: defaultdict[str, int] = defaultdict(int)

    for x in text:
        map[x] += 1

    for x in "abcdefghijklmnopqrstuvwxyz":
        if x not in map:
            return x

    return None


# O(n)
def first_non_duplicate(text: str) -> str | None:
    map: defaultdict[str, int] = defaultdict(int)
    for x in text:
        map[x] += 1

    for x in text:
        if map[x] == 1:
            return x
    return None


if __name__ == "__main__":
    unittest.main()
