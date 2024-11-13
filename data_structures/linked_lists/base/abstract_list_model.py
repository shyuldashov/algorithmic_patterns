from abc import ABC, abstractmethod
from typing import Any


class BaseLinkedList(ABC):

    @abstractmethod
    def insert(self, index: int, value: Any) -> None:
        pass

    @abstractmethod
    def pop(self, index: int) -> "BaseLinkedList":
        pass

    @abstractmethod
    def prepend(self, value: Any) -> None:
        pass

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def get(self, index: int) -> "BaseLinkedList":
        pass

    @property
    @abstractmethod
    def length(self) -> int:
        pass
