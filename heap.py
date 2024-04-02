import unittest
import random


class ArrayHeap:
    def __init__(self):
        self.data: list[int] = []

    def root_node(self):
        if not self.data:
            return None
        return self.data[0]

    def last_node(self):
        if not self.data:
            return None
        return self.data[-1]

    def left_child_index(self, index: int):
        return (index * 2) + 1

    def right_child_index(self, index: int):
        return (index * 2) + 2

    def parent_index(self, index: int):
        return (index - 1) // 2

    def insert(self, value: int):
        self.data.append(value)

        new_node_index = len(self.data) - 1
        while (
            new_node_index > 0
            and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]
        ):
            self.data[new_node_index], self.data[self.parent_index(new_node_index)] = (
                self.data[self.parent_index(new_node_index)],
                self.data[new_node_index],
            )
            new_node_index = self.parent_index(new_node_index)

    def delete(self):
        if not self.data:
            return
        if len(self.data) == 1:
            self.data.pop()
            return

        self.data[0] = self.data.pop()
        trickle_node_index = 0
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            self.data[trickle_node_index], self.data[larger_child_index] = (
                self.data[larger_child_index],
                self.data[trickle_node_index],
            )
            trickle_node_index = larger_child_index

    def has_greater_child(self, index: int):
        left_index = self.left_child_index(index)
        right_index = self.right_child_index(index)
        return (
            self.is_valid_index(left_index) and self.data[left_index] > self.data[index]
        ) or (
            self.is_valid_index(right_index)
            and self.data[right_index] > self.data[index]
        )

    def calculate_larger_child_index(self, index: int):
        left_index = self.left_child_index(index)
        right_index = self.right_child_index(index)

        if not self.is_valid_index(right_index):
            return left_index

        if self.data[right_index] > self.data[left_index]:
            return right_index
        return left_index

    def is_valid_index(self, index: int):
        if not self.data:
            return False
        return 0 <= index < len(self.data)


class TestCase(unittest.TestCase):

    def test_insert(self):
        nums = list(range(10))
        random.shuffle(nums)

        heap = ArrayHeap()
        curr: list[int] = []
        for num in nums:
            heap.insert(num)
            curr.append(num)
            self.assertEqual(heap.root_node(), max(curr))

    def test_delete(self):
        nums = list(range(10))
        random.shuffle(nums)

        heap = ArrayHeap()
        for num in nums:
            heap.insert(num)

        expected = sorted(nums, reverse=True)
        for num in expected:
            self.assertEqual(num, heap.root_node())
            heap.delete()


if __name__ == "__main__":
    unittest.main()
