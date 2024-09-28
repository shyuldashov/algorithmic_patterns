from design_gurus.tests.test_foo import check_result


class Solution:
    def two_pointers(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        curr = left = 0
        right: int = len(nums) - 1
        while left <= right:

            match nums[left]:
                case 0:
                    nums[left], nums[curr] = nums[curr], nums[left]
                    curr += 1
                    left += 1
                case 1:
                    left += 1
                case _:  # default
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1

        return nums


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list]] = [
        ([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
        ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2]),
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 2]),
    ]

    check_result(solve.two_pointers, test_case)
