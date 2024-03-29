import unittest
import random


class TestCase(unittest.TestCase):
    def test_sorted(self):
        arr = list(range(20))
        random.shuffle(arr)

        sortable_arr = SortableArray(arr)
        sortable_arr.quicksort(0, len(sortable_arr.array) - 1)

        self.assertEqual(sorted(arr), sortable_arr.array)

    def test_select(self):
        arr = [0, 50, 20, 5, 10, 60, 30]
        sortable_arr = SortableArray(arr)

        # find 2nd lowest
        th = 1
        actual = sortable_arr.quick_select(th, 0, len(sortable_arr.array) - 1)
        self.assertEqual(sorted(arr)[th], actual)

        # find 5th lowest value
        th = 4
        actual = sortable_arr.quick_select(th, 0, len(sortable_arr.array) - 1)
        self.assertEqual(sorted(arr)[th], actual)


class SortableArray:
    def __init__(self, array: list[int]):
        self.array = array

    def partition(self, left_pointer: int, right_pointer: int) -> int:
        # select right-most element as pivot
        pivot_index = right_pointer

        # pivot value
        pivot = self.array[pivot_index]

        # move right pointer one step to left,
        # after right-most element used as pivot
        right_pointer -= 1
        while True:
            # move left pointer to right as long as its value less than pivot
            while self.array[left_pointer] < pivot:
                left_pointer += 1

            # move right pointer to left as long as its value larger than pivot
            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            # now both pointer stopped
            # if left pointer reached/beyond right pointer
            # then break the loop to swap the pivot later
            if left_pointer >= right_pointer:
                break

            # when left-pointer still on the left side of the right-pointer
            # swap value of both pointer
            else:
                self.array[left_pointer], self.array[right_pointer] = (
                    self.array[right_pointer],
                    self.array[left_pointer],
                )
                left_pointer += 1

        # swap pivot and left pointer
        self.array[left_pointer], self.array[pivot_index] = (
            self.array[pivot_index],
            self.array[left_pointer],
        )

        # return left pointer
        return left_pointer

    def quicksort(self, left_index: int, right_index: int):
        if right_index - left_index <= 0:
            return

        # partition array
        pivot_index = self.partition(left_index, right_index)

        # recursive left side
        self.quicksort(left_index, pivot_index - 1)

        # recursive right side
        self.quicksort(pivot_index + 1, right_index)

    def quick_select(
        self, kth_lowest_value: int, left_index: int, right_index: int
    ) -> int:
        # one cell sub array as base case
        if right_index - left_index <= 0:
            return self.array[left_index]

        # partition index
        pivot_index = self.partition(left_index, right_index)

        # k th lowest, e.g 2nd lowest
        if kth_lowest_value < pivot_index:
            return self.quick_select(kth_lowest_value, left_index, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            return self.quick_select(kth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.array[pivot_index]


if __name__ == "__main__":
    unittest.main()
