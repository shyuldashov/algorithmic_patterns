from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def fast_and_slow_pointers(self, head: Optional[ListNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False

    def use_dict(self, head: Optional[ListNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return False

        visited: dict[ListNode, bool] = {}
        current = head
        while current:
            if current in visited:
                return True
            visited[current] = True
            current = current.next

        return False


if __name__ == "__main__":
    solve = Solution()
