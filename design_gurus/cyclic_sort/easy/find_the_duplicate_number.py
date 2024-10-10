from design_gurus.tests.test_foo import check_result


class Solution:
    def find_the_duplicate_number(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        slow: int = nums[0]
        fast: int = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, int]] = [
        ([1, 4, 4, 3, 2], 4),
        ([2, 1, 3, 3, 5, 4], 3),
        ([2, 4, 1, 4, 4], 4),
        ([1, 1], 1),
        ([7, 7, 7, 7, 7, 7, 7, 7], 7),
    ]

    check_result(solve.find_the_duplicate_number, test_case)
