""" This is from recursive chapter """

import unittest
import math


class TestCase(unittest.TestCase):
    def test_factorial(self):
        n = 10
        self.assertEqual(math.factorial(n), factorial0(n))
        self.assertEqual(math.factorial(n), factorial1(n))


def factorial0(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial1(n: int) -> int:
    if n <= 2:
        return n
    return n * factorial1(n - 1)


if __name__ == "__main__":
    unittest.main()
