from design_gurus.tests.test_foo import check_result


class Solution:
    def find_all_duplicate_nums(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        result: list[int] = []
        for i in range(len(nums)):

            curr: int = abs(nums[i]) - 1
            if nums[curr] < 0:
                result.append(curr + 1)

            nums[curr] *= -1

        return result


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list]] = [
        ([3, 4, 4, 5, 5], [4, 5]),
        ([5, 4, 7, 2, 3, 5, 3], [5, 3]),
        ([2, 4, 1, 4, 3, 3], [4, 3]),
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1], []),
    ]

    check_result(solve.find_all_duplicate_nums, test_case)
