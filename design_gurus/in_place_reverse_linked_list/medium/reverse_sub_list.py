from typing import Optional

from data_structures.linked_lists import SinglyLinkedList
from data_structures.linked_lists.nodes import SinglyLinkedListNode
from data_structures.linked_lists.utils import PrintLinkedList


class Solution:
    def reverse_between(
        self,
        head: Optional[SinglyLinkedListNode],
        left: int,
        right: int,
    ) -> Optional[SinglyLinkedListNode]:
        if head is None or left == right:
            return head

        dummy = SinglyLinkedListNode(0)
        dummy.next = head

        left_prev, current = dummy, head
        for _ in range(left - 1):
            left_prev, current = current, current.next

        prev = None
        for _ in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev, current = current, temp

        left_prev.next.next = current
        left_prev.next = prev

        return dummy.next


if __name__ == "__main__":
    solve = Solution()
    data: list[tuple[tuple, int, int]] = [
        ((1, 2, 3, 4, 5), 2, 4),
        ((5,), 1, 1),
        ((10, 20, 30), 1, 3),
        ((6, 7, 8, 9), 3, 4),
    ]

    for values, i, j in data:
        linked_list = SinglyLinkedList()
        linked_list.append_many(values)
        printer = PrintLinkedList(linked_list.head)
        printer.print_with_forward_arrow()

        reversed_between = solve.reverse_between(linked_list.head, i, j)
        printer = PrintLinkedList(reversed_between)
        printer.print_with_forward_arrow()
        print()
