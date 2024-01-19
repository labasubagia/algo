import unittest
import random


class TestCase(unittest.TestCase):
    def test_sort(self):
        arr = list(range(30))

        arr1 = arr.copy()
        random.shuffle(arr1)
        self.assertEqual(arr, quicksort1(arr1))

        arr2 = arr.copy()
        random.shuffle(arr2)
        quicksort2(arr2, 0, len(arr2) - 1)
        self.assertEqual(arr, arr2)


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


def quicksort2(arr: list[int], low: int, high: int):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort2(arr, low, pivot_index - 1)
        quicksort2(arr, pivot_index + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    unittest.main()
