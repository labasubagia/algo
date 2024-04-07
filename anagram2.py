# check wether 2 string anagram

import unittest


def are_anagram_naive(s1: str, s2: str) -> bool:
    arr2: list[str] = list(s2)
    for c1 in s1:
        if not arr2:
            return False
        for i in range(len(arr2)):
            if c1 == arr2[i]:
                del arr2[i]
                break
    return len(arr2) == 0


def are_anagram_double_map(s1: str, s2: str) -> bool:
    m1: dict[str, int] = {}
    m2: dict[str, int] = {}
    for c in s1:
        if c not in m1:
            m1[c] = 0
        m1[c] += 1
    for c in s2:
        if c not in m2:
            m2[c] = 0
        m2[c] += 1
    return m1 == m2


def are_anagram_single_map(s1: str, s2: str) -> bool:
    m1: dict[str, int] = {}
    for c in s1:
        if c not in m1:
            m1[c] = 0
        m1[c] += 1

    for c in s2:
        if c not in m1:
            return False
        m1[c] -= 1
        if m1[c] == 0:
            del m1[c]

    return len(m1) == 0


class TestCase(unittest.TestCase):
    test_cases = [
        ("makar", "kamar", True),
        ("silent", "listen", True),
        ("ab", "aba", False),
    ]

    def test_naive(self):
        for s1, s2, expected in self.test_cases:
            self.assertEqual(expected, are_anagram_naive(s1, s2))

    def test_double_map(self):
        for s1, s2, expected in self.test_cases:
            self.assertEqual(expected, are_anagram_double_map(s1, s2))

    def test_single_map(self):
        for s1, s2, expected in self.test_cases:
            self.assertEqual(expected, are_anagram_single_map(s1, s2))


if __name__ == "__main__":
    unittest.main()
