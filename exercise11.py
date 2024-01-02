"""Recursion"""

import unittest


class TestCase(unittest.TestCase):
    def test_total_chars(self):
        arr = ["ab", "c", "def", "ghij"]
        expected = len("".join(arr))
        self.assertEqual(expected, total_chars(arr))

    def test_even_numbers(self):
        arr = list(range(11))
        expected = [x for x in arr if x % 2 == 0]
        self.assertEqual(expected, even_numbers(arr))

    def test_triangular_number(self):
        arr: list[int] = []
        for i in range(10):
            if len(arr) == 0:
                arr.append(i)
            else:
                arr.append(i + arr[i - 1])
        for i, expected in enumerate(arr):
            self.assertEqual(expected, triangular_number(i))

    def test_x_index(self):
        string = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(string.index("x"), x_index(string))

    def test_unique_paths(self):
        self.assertEqual(28, unique_paths(3, 7))


def total_chars(arr_chars: list[str]) -> int:
    if len(arr_chars) == 0:
        return 0
    return len(arr_chars[0]) + total_chars(arr_chars[1 : len(arr_chars)])


def even_numbers(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return []
    curr: list[int] = []
    if arr[0] % 2 == 0:
        curr.append(arr[0])
    return curr + even_numbers(arr[1 : len(arr)])


def triangular_number(n: int) -> int:
    if n == 0:
        return 0
    return n + triangular_number(n - 1)


def x_index(string: str, index: int = 0) -> int | None:
    if len(string) == 0:
        return None
    if string[0] == "x":
        return index
    return x_index(string[1:], index + 1)


def unique_paths(rows: int, columns: int) -> int:
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


if __name__ == "__main__":
    unittest.main()
