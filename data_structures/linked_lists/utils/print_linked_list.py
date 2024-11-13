__all__ = ["PrintLinkedList"]


class PrintLinkedList:
    def __init__(self, head, separator: str = "") -> None:
        self.head = head
        self.__sep = separator

    def __print_processor(self, sep: str = None) -> str:
        sep = sep or self.__sep
        result: str = ""

        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            result += f" {sep} " if temp else f" {sep} null"

        return result

    def print(self) -> None:
        print(self.__print_processor())

    def print_with_forward_arrow(self) -> None:
        print(self.__print_processor("→"))
