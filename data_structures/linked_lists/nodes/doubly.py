from typing import Any, Optional

__all__ = ["DoublyLinkedListNode"]


class DoublyLinkedListNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional["DoublyLinkedListNode"] = None
        self.prev: Optional["DoublyLinkedListNode"] = None
