from design_gurus.tests.test_foo import check_result


class Solution:
    def two_pointers(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        length: int = len(nums)
        left: int = 0
        while (left < length - 1) and (nums[left] < nums[left + 1]):
            left += 1

        if left == length - 1:  # массив уже отсортирован
            return 0

        right: int = length - 1
        while (right > 0) and (nums[right] > nums[right - 1]):
            right -= 1

        min_value, max_value = self._get_max_and_min_values(
            left + 1, right, nums
        )
        while (left >= 0) and (nums[left] > min_value):
            left -= 1
        while (right < length) and (nums[right] < max_value):
            right += 1

        return right - left - 1

    def _get_max_and_min_values(
        self, start: int, end: int, arr: list[int]
    ) -> tuple[int, int]:
        mn_value: int | float = float("inf")
        mx_value: int | float = float("-inf")

        for i in range(start, end):
            mn_value = min(mn_value, arr[i])
            mx_value = max(mx_value, arr[i])

        return mn_value, mx_value


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, int]] = [
        ([1, 2, 5, 3, 7, 10, 9, 12], 5),
        ([1, 3, 2, 0, -1, 7, 10], 5),
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
        ([1, 2, 6, 3, 4, 8, 10, 7, 9], 7),
        ([7, 2, 3, 4, 5, 6, 1], 7),
    ]

    check_result(solve.two_pointers, test_case)
