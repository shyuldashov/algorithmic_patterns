from data_structures.linked_list import PrintLinkedListWithForwardArrow, LinkedList


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

    def main():

        data = (
            [1, 3, 5, 7, 9, 11],
            [2, 4, 6, 8, 10, 12],
            [3, 2, 1],
            [100],
            [1, 2],
        )

        for index, values in enumerate(data, start=1):
            linked_list = LinkedList()
            linked_list.create(values)

            print(index, ".\tInput linked list: ", sep="", end="")
            PrintLinkedListWithForwardArrow(linked_list.head)

            print("\n\tReversed linked list: ", end="")
            PrintLinkedListWithForwardArrow(
                solve.in_place_reverse(linked_list.head)
            )
            print("\n", "-" * 10)

    main()
