from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # Do not return anything, modify head in-place instead.

        if not head:
            return None

        middle = self._find_middle(head)
        right_part = middle.next
        middle.next = None

        right_part = self._reverse_linked_list(right_part)
        self._merge_alternating(head, right_part)

    def _find_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow

    def _reverse_linked_list(
        self, part: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        while part:
            temp = part.next
            part.next = prev
            prev, part = part, temp

        return prev

    def _merge_alternating(
        self, first: Optional[ListNode], second: Optional[ListNode]
    ) -> None:
        while second:
            temp_first, temp_second = first.next, second.next
            first.next = second
            second.next = temp_first
            first, second = temp_first, temp_second

    def reorder_list_short_solve(self, head: Optional[ListNode]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head:
            return None

        # middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge alternating
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next


if __name__ == "__main__":
    pass
