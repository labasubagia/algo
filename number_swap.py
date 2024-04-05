import unittest

# swap a number in an array so both sum equal


def swap_naive(arr1: list[int], arr2: list[int]) -> tuple[int, int] | None:
    s1 = sum(arr1)
    s2 = sum(arr2)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if s1 - arr1[i] + arr2[j] == s2 - arr2[j] + arr1[i]:
                return i, j

    return None


def swap_hashmap(arr1: list[int], arr2: list[int]) -> tuple[int, int] | None:
    m: dict[int, int] = {}
    sum1 = 0
    sum2 = 0

    for i, n in enumerate(arr1):
        sum1 += n
        m[n] = i

    for i, n in enumerate(arr2):
        sum2 += n

    shift_amount = (sum1 - sum2) // 2
    for i, n in enumerate(arr2):
        if n + shift_amount in m:
            return m[n + shift_amount], i

    return None


class TestCase(unittest.TestCase):
    arr1 = [5, 3, 2, 9, 1]
    arr2 = [1, 12, 5]

    def test_naive(self):
        actual = swap_naive(self.arr1, self.arr2)
        self.assertEqual((2, 0), actual)

    def test_hashmap(self):
        actual = swap_hashmap(self.arr1, self.arr2)
        self.assertEqual((2, 0), actual)


if __name__ == "__main__":
    unittest.main()
