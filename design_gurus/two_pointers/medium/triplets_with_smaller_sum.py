from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def two_pointers(self, nums: list[int], target: int) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0

        nums.sort()  # O(n log n)

        length: int = len(nums)
        count: int = 0
        for curr in range(length - 2):
            left: int = curr + 1
            right: int = length - 1

            while left < right:
                temp_sum: int = nums[curr] + nums[left] + nums[right]
                if temp_sum < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list, int, int]] = [
        ([-1, 0, 2, 3], 3, 2),
        ([-1, 4, 2, 1, 3], 5, 4),
        ([-1, 1, -1, 1], 0, 2),
        ([-1, -2, -3], 0, 1),
        ([-1, -1, -1, -1], 3, 4),
        ([1, 1, 1, 1], 1, 0),
    ]
    test_for_two_pointers(solve.two_pointers, test_case)

    # Почему count += (right - left)?
    # Это значит, все комбинации от right до
    # текущего left (включительно) тоже будут меньше target
