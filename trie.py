import unittest


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode | None] = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word: str):
        current_node = self.root
        for char in word:
            if current_node and current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def insert(self, word: str):
        if not word:
            return

        current_node = self.root
        for char in word:

            # none node only when key *
            if not current_node:
                break

            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node

        if current_node:
            current_node.children["*"] = None

    def collectAllWords(
        self, node: TrieNode | None = None, word: str = "", words: list[str] = []
    ):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(child_node, word + key, words)
        return words

    def autocomplete(self, prefix: str) -> list[str]:
        current_node = self.search(prefix)
        if not current_node:
            return []
        return self.collectAllWords(current_node)


class TestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_trie(self):
        words = ["act", "cat", "bat", "batter", "bad", "catnip", "catnap"]
        trie = Trie()
        for word in words:
            trie.insert(word)
        words = trie.collectAllWords()
        self.assertEqual(sorted(words), sorted(words))

    def test_autocomplete(self):
        words = sorted(["act", "cat", "bat", "batter", "bad", "catnip", "catnap"])
        trie = Trie()
        for word in words:
            trie.insert(word)
        prefix = "cat"
        autocomplete = trie.autocomplete(prefix)

        expected = sorted([word for word in words if word.startswith(prefix)])
        actual = sorted([prefix + suffix for suffix in autocomplete])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
