from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        middle: int = (self._get_size(head) // 2) + 1
        return self._get(head, middle)

    def _get_size(self, head: Optional[ListNode]) -> int:
        size: int = 0
        current = head
        while current:
            size += 1
            current = current.next

        return size

    def _get(self, head: Optional[ListNode], index: int) -> Optional[ListNode]:
        current = head
        for _ in range(index):
            current = current.next

        return current

    def fast_and_slow_pointers(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    pass
