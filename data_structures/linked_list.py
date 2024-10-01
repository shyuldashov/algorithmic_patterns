from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.value: Any = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def prepend(self, value: Any) -> None:
        """Insert a new Node at the beginning of the Linked List.
        Time Complexity: O(1)
        :param value:
        :return:
        """
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def append(self, value: Any) -> None:
        """Inserts a new Node at the end of the Linked List.
        Time Complexity: O(1)
        :param value:
        :return:
        """
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def get(self, index: int) -> Any | None:
        """Get the value of index-th Node in the Linked List.
        Time Complexity: O(n)
        :param index:
        :return:
        """
        if (index < 0) or (self.head is None) or (index >= self.size):
            return

        current = self.head
        for _ in range(index):
            current = current.next

        return current.value

    def insert(self, index: int, value: Any) -> None:
        """Insert a new Node at the index-th Node of the Linked List.
        Time Complexity: O(n)
        :param index:
        :param value:
        :return:
        """
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} is out of boundaries")

        if index == self.size:
            self.append(value)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            node = Node(value)
            node.next = current.next
            current.next = node

        self.size += 1

    def pop(self, index: int) -> None:
        """Delete the index-th Node of the Linked List.
        Time Complexity: O(n)
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} is out of boundaries")

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            if current.next.next is None:
                current.next = None
                self.tail = current
            else:
                current.next = current.next.next

        self.size -= 1


if __name__ == "__main__":
    from random import randint

    obj = LinkedList()
    nums = []
    for _ in range(10):
        num = randint(10, 50)
        obj.append(num)
        nums.append(num)

    print(nums)
    obj.pop(5)
    for i in range(9):
        print(obj.get(i))
