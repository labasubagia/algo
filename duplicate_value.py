import unittest
from typing import List
from collections import defaultdict

class TestCase(unittest.TestCase):
    def test_has_duplicate(self):
        arr = [1,2,3,4,1,5,6]
        # expected = len(list(set(arr))) < len(arr)

        self.assertTrue(has_duplicate_value1(arr))
        self.assertTrue(has_duplicate_value2(arr))

    def test_dont_have_duplicate(self):
        arr = [x for x in range(5)]
        self.assertFalse(has_duplicate_value1(arr))
        self.assertFalse(has_duplicate_value2(arr))


# Time: O(n^2), Space: O(1)
def has_duplicate_value1(arr: List[int]) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and arr[i] == arr[j]:
                return True
    return False

# Time: O(n), Space: O(n)
def has_duplicate_value2(arr: List[int]) -> bool:
    m : defaultdict[int, int] = defaultdict(int)
    for x in arr:
        m[x] += 1
        if m[x] > 1:
            return True

    return False

if __name__ == '__main__':
    unittest.main()
