import unittest
from collections import deque


class TestCase(unittest.TestCase):
    def test_print_doc(self):
        print_manager = PrintManager()
        print_manager.queue_print_job("Doc1")
        print_manager.queue_print_job("Doc2")
        print_manager.queue_print_job("Doc3")
        print_manager.run()


class PrintManager:
    def __init__(self):
        self.queue: deque[str] = deque()

    def queue_print_job(self, doc: str):
        self.queue.append(doc)

    def run(self):
        while len(self.queue):
            print(self.queue.popleft())


if __name__ == "__main__":
    unittest.main()
