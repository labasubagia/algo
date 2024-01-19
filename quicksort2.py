import unittest
import random


class TestCase(unittest.TestCase):
    def test_sort(self):
        arr1 = list(range(30))
        random.shuffle(arr1)

        self.assertEqual(list(range(30)), quicksort1(arr1))


def quicksort1(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left: list[int] = []
    right: list[int] = []
    middle: list[int] = []

    for item in arr:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            middle.append(item)

    return quicksort1(left) + middle + quicksort1(right)


if __name__ == "__main__":
    unittest.main()
