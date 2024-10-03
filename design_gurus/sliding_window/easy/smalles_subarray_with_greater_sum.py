from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def two_pointers(self, nums: list[int], target) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        length: int = len(nums)
        min_length: int = length

        is_found: bool = False
        temp_sum: int = 0
        left = right = 0
        while right < length:
            temp_sum += nums[right]
            right += 1

            while temp_sum >= target:
                if (right - left) < min_length:
                    min_length = right - left
                    is_found = True

                temp_sum -= nums[left]
                left += 1

        return min_length if is_found else 0


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, int, int]] = [
        ([2, 1, 5, 2, 3, 2], 7, 2),
        ([2, 1, 5, 2, 8], 7, 1),
        ([3, 4, 1, 1, 6], 8, 3),
        ([1, 1, 1, 1], 99, 0),
        ([2, 2, 2, 2], 3, 2),
    ]

    test_for_two_pointers(solve.two_pointers, test_case)
