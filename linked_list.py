from __future__ import annotations


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def prepend(self, node: Node):
        if self.head is None:
            self.head = node
            return

        tmp = self.head
        self.head = node
        node.next = tmp

    def append(self, node: Node):
        if not self.head:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def insert_at_index(self, index: int, node: Node):
        if index == 0:
            node.next = self.head
            self.head = node
            return

        curr = self.head
        curr_index = 0
        while curr and curr_index < (index - 1):
            curr = curr.next
            curr_index += 1

        if curr:
            node.next = curr.next
            curr.next = node

    def delete_at_index(self, index: int):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        curr_index = 0
        while curr and curr_index < (index - 1):
            curr = curr.next
            curr_index += 1

        if curr and curr.next:
            node_after_deleted_node = curr.next.next
            curr.next = node_after_deleted_node

    def read(self, index: int):
        curr = self.head
        curr_index = 0
        while curr:
            if curr_index == index:
                return curr
            curr = curr.next
            curr_index += 1
        return None

    def index_of(self, val: int):
        curr = self.head
        index = 0
        while curr:
            if curr.val == val:
                return index
            index += 1
            curr = curr.next
        return None

    def traverse(self):
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

    def reverse(self):
        curr = self.head
        prev: Node | None = None
        next: Node | None = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


class Node:
    def __init__(self, val: int, next: Node | None = None) -> None:
        self.val = val
        self.next = next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    ll.append(Node(4))
    ll.append(Node(5))

    ll.reverse()
    ll.traverse()
