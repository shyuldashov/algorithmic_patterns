from design_gurus.tests.test_foo import check_result


class Solution:
    def find_the_corrupt_pair(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        duplicate: int = -1

        for num in nums:
            curr = abs(num) - 1
            nums[curr] *= -1

            if nums[curr] > 0:
                duplicate = curr + 1

        for pos, num in enumerate(nums, start=1):
            if (num > 0) and (pos != duplicate):
                return [duplicate, pos]

        return [-1, -1]


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list]] = [
        ([3, 1, 2, 5, 2], [2, 4]),
        ([3, 1, 2, 3, 6, 4], [3, 5]),
        ([3, 2, 2], [2, 1]),
        ([1, 1], [1, 2]),
    ]

    check_result(solve.find_the_corrupt_pair, test_case)
