"""
DP chapters
avoid call recursive function more than once
it will drove to complexity of O(2^n)
"""

import unittest
import math


class TestCase(unittest.TestCase):
    def test_fib(self):
        n = 10
        expected = fib(n)

        actual1, step1 = fib1(n)
        self.assertEqual(expected, actual1)

        actual2, step2 = fib2(n)
        self.assertEqual(expected, actual2)

        actual3, step3 = fib3(n)
        self.assertEqual(expected, actual3)

        print(step1, step2, step3)


def fib(n: int) -> int | float:
    # Fn = {[(√5 + 1)/2] ^ n} / √5
    return round(((math.sqrt(5) + 1) / 2) ** n / math.sqrt(5))


def fib1(n: int, step: int = 0) -> tuple[int, int]:
    step += 1
    if n == 0 or n == 1:
        return n, step
    (f1, step) = fib1(n - 2, step)
    (f2, step) = fib1(n - 1, step)
    return f1 + f2, step


# using DP
def fib2(n: int, memo: dict[int, int] = {0: 0, 1: 1}, step: int = 0) -> tuple[int, int]:
    step += 1
    if n not in memo:
        f1, step = fib2(n - 2, memo, step)
        f2, step = fib2(n - 1, memo, step)
        memo[n] = f1 + f2
    return memo[n], step


# bottom-up DP
def fib3(n: int) -> tuple[int, int]:
    step: int = 1
    a = 0
    b = 1
    for _ in range(1, n):
        step += 1
        tmp = a
        a = b
        b = tmp + a
    return b, step


if __name__ == "__main__":
    unittest.main()
