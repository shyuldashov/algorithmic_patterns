from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome_brute_force(self, head: Optional[ListNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param head:
        :return:
        """
        data: list[Any] = []
        while head:
            data.append(head.val)
            head = head.next

        left: int = 0
        right: int = len(data) - 1
        while left < right:
            if data[left] != data[right]:
                return False

            left += 1
            right -= 1

        return True

    def fast_and_slow_pointers(self, head: Optional[ListNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        _, right_side = self._find_middle(head)
        right_side = self._reverse_linked_list(right_side)

        left, right = head, right_side
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def _find_middle(
        self, head: Optional[ListNode]
    ) -> tuple[ListNode, ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return fast, slow

    def _reverse_linked_list(
        self, part: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        while part:
            temp = part.next
            part.next = prev
            prev, part = part, temp

        return prev


if __name__ == "__main__":
    pass
