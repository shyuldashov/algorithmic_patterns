from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        temp_sum: int = sum(nums[:k])

        max_sum: int = 0
        for i in range(k, len(nums)):
            temp_sum += nums[i] - nums[i - k]
            max_sum = max(temp_sum, max_sum)

        return max_sum


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, int, int]] = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([2, 3, 4, 1, 5], 2, 7),
        ([], 0, 0),
        ([3, 2, 5, 4, 1], 3, 11),
    ]

    test_for_two_pointers(solve.maximum_subarray_sum, test_case)
