from typing import List
import unittest


class TestGreatest(unittest.TestCase):
    def test_greatest(self):
        arr = list(range(10))
        self.assertEqual(max(arr), greatest_number1(arr))
        self.assertEqual(max(arr), greatest_number2(arr))


# O(n^2), question
def greatest_number1(array: List[int]):
    for i in array:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True
        for j in array:
            # If we find another value that is greater than i,
            # i is not the greatest:
            if j > i:
                isIValTheGreatest = False
            # If, by the time we checked all the other numbers, i
            # is still the greatest, it means that i is the greatest number:
        if isIValTheGreatest:
            return i


# O(n), answer
def greatest_number2(array: List[int]):
    curr = float("-inf")
    for x in array:
        if x > curr:
            curr = x
    return curr


if __name__ == "__main__":
    unittest.main()
