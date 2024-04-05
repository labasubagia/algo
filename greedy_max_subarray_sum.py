import unittest


# use greedy
def max_sub_array_sum(nums: list[int]) -> int:
    ans = 0
    curr_sum = 0
    for n in nums:
        curr_sum += n
        if curr_sum < 0:
            curr_sum = 0
        ans = max(ans, curr_sum)
    return ans


class TestCase(unittest.TestCase):
    def test_correct(self):
        arr = [3, -4, 4, -3, 5, -9]
        self.assertEqual(6, max_sub_array_sum(arr))


if __name__ == "__main__":
    unittest.main()
