from typing import Any, Optional, Sequence

from data_structures.linked_lists.base import AbstractLinkedList
from data_structures.linked_lists.nodes import SinglyLinkedListNode
from data_structures.linked_lists.utils import PrintLinkedList

__all__ = ["SinglyLinkedList"]


class SinglyLinkedList(AbstractLinkedList):
    def __init__(self) -> None:
        self.head: Optional[SinglyLinkedListNode] = None
        self.__length: int = 0

    @property
    def length(self) -> int:
        return self.__length

    def _check_index(self, index: int) -> None:
        if index < 0 or index > self.__length:
            raise IndexError(f"Index {index} is out of bounds")

    def __insert_by(self, index: int, value: Any) -> None:
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node = SinglyLinkedListNode(value)
        new_node.next = current.next
        current.next = new_node

    def insert(self, index: int, value: Any) -> None:
        """Inserts a new node at the index-th Node of the Singly Linked List.
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

    def pop(self, index: int) -> "SinglyLinkedListNode":
        """Removes the index-th Node of the Singly Linked List and returns it.
        Time Complexity: O(n)
        :param index:
        :raises IndexError: If index is out of bounds or the list is empty.
        """
        self._check_index(index)

        if self.head is None:
            raise IndexError("Pop from empty list")

        if index == 0:
            removed_node = self.head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            removed_node = current.next
            current.next = current.next.next

        self.__length -= 1
        return removed_node

    def prepend(self, value: Any) -> None:
        """Inserts a new Node at the beginning of the Singly Linked List.
        Time Complexity: O(1)
        :param value:
        """
        new_node = SinglyLinkedListNode(value)

        if self.head:
            new_node.next = self.head
        self.head = new_node

        self.__length += 1

    def append(self, value: Any) -> None:
        """Inserts a new Nodes at the end of the Singly Linked List.
        Time Complexity: O(n)
        :param value:
        """
        new_node = SinglyLinkedListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next

            last.next = new_node

        self.__length += 1

    def remove(self, value: Any) -> None:
        """Remove by value Node of the Singly Linked List.
        Time Complexity: O(n)
        :param value:
        :raises ValueError: If value not in list.
        """
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            self.__length -= 1
            return

        temp = self.head
        current = self.head.next
        while current:
            if current.data == value:
                temp.next = current.next
                self.__length -= 1
                return

            temp = current
            current = current.next

        raise ValueError(f"{value} not in list")

    def get(self, index: int) -> Optional["SinglyLinkedList"]:
        """Get the value of index-th Node in the Singly Linked List.
        Time Complexity: O(n)
        :param index:
        :raises IndexError: If index is out of bounds or the list is empty.
        """
        self._check_index(index)

        if self.head is None:
            raise IndexError("Get from empty list")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def append_many(self, values: Sequence) -> None:
        """
        Inserts multiple values into a Singly Linked List.
        :param values:
        Time Complexity: O(n^2)
        """
        _ = [self.append(value) for value in values]


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append_many([1, 2, 3, 4, 5])
    linked_list.insert(2, 10)

    printer = PrintLinkedList(linked_list.head)
    printer.print()
    printer.print_with_forward_arrow()
