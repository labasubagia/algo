import unittest


class TestCase(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual("fedcba", reverse_str_stack("abcdef"))


def reverse_str_stack(text: str) -> str:
    stack = list(text)
    result = ""
    while len(stack) > 0:
        result += stack.pop()
    return result


if __name__ == "__main__":
    unittest.main()
