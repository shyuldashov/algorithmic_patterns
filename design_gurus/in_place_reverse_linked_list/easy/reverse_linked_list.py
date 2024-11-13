class Solution:
    def in_place_reverse(self, head: "ListNode") -> "ListNode":
        if head is None:
            return head

        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev


if __name__ == "__main__":
    solve = Solution()
