import unittest
import random
from collections import defaultdict


class TestCase(unittest.TestCase):
    def test_sum3(self):
        """max sum of 3 item in array"""
        arr = list(range(11))
        expected = 10 * 9 * 8
        self.assertEqual(expected, sum3_1(arr))
        self.assertEqual(expected, sum3_2(arr))

    def test_missing_number(self):
        """expected to find missing number from 0 to len array"""
        arr = [9, 3, 2, 5, 6, 7, 1, 0, 4]
        expected = 8
        self.assertEqual(expected, missing_number1(arr))
        self.assertEqual(expected, missing_number2(arr))
        self.assertEqual(expected, missing_number3(arr))

    def test_greatest_number(self):
        n = 10
        arr = list(range(n + 1))
        random.shuffle(arr)
        self.assertEqual(n, greatest_number1(arr))
        self.assertEqual(n, greatest_number2(arr))
        self.assertEqual(n, greatest_number3(arr))


# O(n^3)
def sum3_1(arr: list[int]) -> int:
    n = len(arr)
    if n < 3:
        return 0
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i:
                    curr = arr[i] * arr[j] * arr[k]
                    ans = max(ans, curr)

    return ans


# O(nlogn)
def sum3_2(arr: list[int]) -> int:
    if len(arr) < 3:
        return 0
    arr.sort()
    return arr[-1] * arr[-2] * arr[-3]


# O(n^2), `not in` is O(n)
def missing_number1(arr: list[int]) -> int | None:
    for i in range(len(arr)):
        if i not in arr:
            return i
    return None


# O(nlogn) + O(n) = O(nlogn)
def missing_number2(arr: list[int]) -> int | None:
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return None


# O(n)
def missing_number3(arr: list[int]) -> int | None:
    m: defaultdict[int, int] = defaultdict(int)
    for x in arr:
        m[x] += 1
    for i in range(len(arr)):
        if m[i] == 0:
            return i
    return None


# O(n^2)
def greatest_number1(arr: list[int]) -> int | None:
    n = len(arr)
    for i in range(n):
        is_greatest = True
        for j in range(n):
            if arr[j] > arr[i]:
                is_greatest = False

        if is_greatest:
            return arr[i]
    return None


# O(nlogn)
def greatest_number2(arr: list[int]) -> int | None:
    if len(arr) == 0:
        return None
    arr.sort()
    return arr[-1]


# O(n)
def greatest_number3(arr: list[int]) -> int | None:
    if len(arr) == 0:
        return None
    ans = arr[0]
    for x in arr:
        if ans < x:
            ans = x
    return ans


if __name__ == "__main__":
    unittest.main()
