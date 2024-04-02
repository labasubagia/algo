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

    def auto_complete(self, prefix: str) -> list[str]:
        current_node = self.search(prefix)
        if not current_node:
            return []
        return self.collectAllWords(current_node, word="", words=[])

    def auto_correct(self, prefix: str) -> list[str]:
        current_node = self.root
        longestSameChar = ""
        for char in prefix:
            if current_node and current_node.children.get(char):
                longestSameChar += char
                current_node = current_node.children[char]
            else:
                break
        result = self.collectAllWords(current_node, word="", words=[])
        return [longestSameChar + suffix for suffix in result]

    def traverse(self, node: TrieNode | None = None):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            print(key, end="")
            if key != "*":
                self.traverse(child_node)


class TestCase(unittest.TestCase):

    def gen(self):
        words = sorted(["act", "cat", "bat", "batter", "bad", "catnip", "catnap"])
        trie = Trie()
        for word in words:
            trie.insert(word)
        return (trie, words.copy())

    def test_trie(self):
        trie, words = self.gen()
        actual = trie.collectAllWords(words=[])
        self.assertEqual(words, actual)

    def test_auto_complete(self):
        trie, words = self.gen()

        prefix = "cat"
        autocomplete = trie.auto_complete(prefix)

        expected = sorted([word for word in words if word.startswith(prefix)])
        actual = sorted([prefix + suffix for suffix in autocomplete])
        self.assertEqual(expected, actual)

    def test_traverse(self):
        trie, _ = self.gen()
        trie.traverse()

    def test_auto_correct(self):
        trie, words = self.gen()
        prefix = "car"
        expected = [word for word in words if word.startswith("ca")]
        actual = trie.auto_correct(prefix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
