import unittest


class TestCase(unittest.TestCase):
    def test_linter_ok(self):
        linter = Linter()
        self.assertTrue(linter.lint(r"([]{{()}})"))

    def test_linter_failed(self):
        linter = Linter()
        self.assertRaises(Exception, linter.lint, "([")
        self.assertRaises(Exception, linter.lint, ")")
        self.assertRaises(Exception, linter.lint, "{)")


class Linter:
    def __init__(self) -> None:
        self.braces = {"(": ")", "{": "}", "[": "]"}
        self.stack: list[str] = []

    def lint(self, text: str) -> bool:
        for char in text:
            if self.is_opening_brace(char):
                self.stack.append(char)

            elif self.is_closing_brace(char):
                if len(self.stack) == 0:
                    raise Exception(f"{char} does not have opening brace")
                popped_opening_brace = self.stack.pop()
                if not self.is_match(popped_opening_brace, char):
                    raise Exception(f"{char} does not match opening brace")

        if len(self.stack) > 0:
            raise Exception(f"{self.stack[-1]} does not have closing brace")

        return True

    def is_opening_brace(self, char: str):
        return char in self.braces

    def is_closing_brace(self, char: str):
        return char in self.braces.values()

    def is_match(self, opening: str, closing: str):
        return self.braces[opening] == closing


if __name__ == "__main__":
    unittest.main()
