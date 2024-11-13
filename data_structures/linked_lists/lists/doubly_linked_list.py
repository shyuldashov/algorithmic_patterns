from typing import Any, Optional, Sequence

from data_structures.linked_lists.base import BaseLinkedList
from data_structures.linked_lists.nodes import DoublyLinkedListNode
from data_structures.linked_lists.utils import PrintLinkedList

__all__ = ["DoublyLinkedList"]


class DoublyLinkedList(BaseLinkedList):
    def __init__(self) -> None:
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None
        self.__length: int = 0

    @property
    def length(self) -> int:
        return self.__length

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self.__length:
            raise IndexError(f"Index {index} is out of bounds")

    def __insert_by(self, index: int, value: Any) -> None:
        new_node = DoublyLinkedListNode(value)

        current = self.head
        for _ in range(index):
            current = current.next

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

    def insert(self, index: int, value: Any) -> None:
        """Insert a new Node at the index-th Node of the Doubly Linked List.
        Time Complexity: O(n)
        :param index:
        :param value:
        :raises IndexError: If index is out of bounds.
        """
        self._check_index(index)

        if index == 0:
            self.prepend(value)
        elif index == self.__length:
            self.append(value)
        else:
            self.__insert_by(index, value)
            self.__length += 1

    def pop(self, index: int) -> None:
        """Delete the index-th Node of the Doubly Linked List.
        Time Complexity: O(n)
        :param index:
        :raises IndexError: If index is out of bounds.
        """
        self._check_index(index)

        if index == 0:
            value = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.__length - 1:
            value = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            value = current.data
            current.prev.next = current.next
            current.next.prev = current.prev

        self.__length -= 1

        return value

    def prepend(self, value: Any) -> None:
        """Insert a new Node at the beginning of the Doubly Linked List.
        Time Complexity: O(1)
        :param value:
        """
        new_node = DoublyLinkedListNode(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.__length += 1

    def append(self, value: Any) -> None:
        """Inserts a new Node at the end of the Doubly Linked List.
        Time Complexity: O(1)
        :param value:
        """
        new_node = DoublyLinkedListNode(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.__length += 1

    def remove(self, value: Any) -> None:
        """Remove by value Node of the Doubly Linked List.
        Time Complexity: O(n)
        :param value:
        :raises ValueError: If value not in list.
        """

        current = self.head
        while current is not None:
            if current.data == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.__length -= 1
                return

            current = current.next

        raise ValueError(f"{value} not in list")

    def get(self, index: int) -> Optional[Any]:
        """Get the value of index-th Node in the Doubly Linked List.
        Time Complexity: O(n)
        :param index:
        :raises IndexError: If index is out of bounds.
        """
        self._check_index(index)

        if self.head is None:
            return

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def append_many(self, values: Sequence) -> None:
        """
        Inserts multiple values into a Doubly Linked List.
        :param values:
        Time Complexity: O(n^2)
        """
        _ = [self.append(value) for value in values]


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append_many([1, 2, 3, 4, 5])
    print(linked_list.length)

    printer = PrintLinkedList(linked_list.head, separator="<->")
    printer.print()
