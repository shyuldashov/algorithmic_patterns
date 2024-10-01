from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                current = head
                while current is not slow:
                    current = current.next
                    slow = slow.next
                return slow

        return None

    def use_set(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param head:
        :return:
        """
        visited: set[ListNode] = set()
        while head:
            if head in visited:
                return head

            visited.add(head)
            head = head.next

        return None


if __name__ == "__main__":
    pass
