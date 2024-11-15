from abc import ABC, abstractmethod
from typing import Any


class AbstractLinkedList(ABC):

    @property
    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def insert(self, index: int, value: Any) -> None:
        pass

    @abstractmethod
    def pop(self, index: int) -> "AbstractLinkedList":
        pass

    @abstractmethod
    def prepend(self, value: Any) -> None:
        pass

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def get(self, index: int) -> "AbstractLinkedList":
        pass
