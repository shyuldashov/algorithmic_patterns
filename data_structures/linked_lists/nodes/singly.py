from typing import Any, Optional

__all__ = ["SinglyLinkedListNode"]


class SinglyLinkedListNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional["SinglyLinkedListNode"] = None
