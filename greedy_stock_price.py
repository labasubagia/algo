# detect 3 upward trend of stock price
import unittest


def has_3_uptrend_naive(arr: list[float]):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] <= arr[j] <= arr[k]:
                    return True
    return False


def has_3_uptrend_greedy(arr: list[float]):
    lowest_price = float("inf")
    middle_price = float("inf")
    for price in arr:
        if price <= lowest_price:
            lowest_price = price
        elif price <= middle_price:
            middle_price = price
        else:
            return True
    return False


class TestCase(unittest.TestCase):
    test_cases = [
        ([22, 25, 21, 18, 19.6, 17, 16, 20.5], True),
        ([5, 2, 8, 4, 3, 7.0], True),
        ([50, 51.25, 48.4, 49, 47.2, 48, 46.9], False),
    ]

    def test_naive(self):
        for arr, expected in self.test_cases:
            self.assertEqual(expected, has_3_uptrend_naive(arr))

    def test_greedy(self):
        for arr, expected in self.test_cases:
            self.assertEqual(expected, has_3_uptrend_greedy(arr))


if __name__ == "__main__":
    unittest.main()
