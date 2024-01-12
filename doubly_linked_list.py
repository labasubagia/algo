from __future__ import annotations


class Queue:
    def __init__(self) -> None:
        self.data = DoublyLinkedList()

    def enqueue(self, val: int):
        self.data.insert_at_end(val)

    def dequeue(self):
        removed = self.data.remove_front()
        if removed:
            return removed.val


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail = self.head

    def insert_at_end(self, val: int):
        node = Node(val)

        if not self.head:
            self.head = node
            self.tail = self.head
            return

        if self.head and self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove_front(self):
        if self.head:
            removed = self.head
            self.head = self.head.next
            if not self.head:
                self.tail = self.head
            return removed

    def traverse_backward(self):
        curr = self.tail
        while curr:
            print(curr.val)
            curr = curr.prev

    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


class Node:
    def __init__(
        self, val: int, prev: Node | None = None, next: Node | None = None
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


if __name__ == "__main__":
    # q = Queue()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)

    # print(q.dequeue())
    # print(q.data.__dict__)

    ll = DoublyLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)

    ll.traverse_backward()
    ll.traverse_forward()
