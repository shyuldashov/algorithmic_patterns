from design_gurus.tests.test_foo import check_result


class Solution:
    def find_all_missing_number(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param nums:
        :return:
        """
        length: int = len(nums)

        for i in range(length):
            curr: int = abs(nums[i]) - 1

            if nums[curr] > 0:
                nums[curr] *= -1

        return [i + 1 for i in range(length) if nums[i] > 0]


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list]] = [
        ([2, 3, 1, 8, 2, 3, 5, 1], [4, 6, 7]),
        ([2, 4, 1, 2], [3]),
        ([2, 3, 2, 1], [4]),
    ]

    check_result(solve.find_all_missing_number, test_case)
