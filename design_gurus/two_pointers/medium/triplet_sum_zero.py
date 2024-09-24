from design_gurus.tests.test_foo import check_result


class Solution:
    def two_pointers(self, nums: list[int]) -> list[list]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        :param nums:
        :return:
        """
        nums.sort()  # O(n log n)

        length: int = len(nums)
        triplets: list[list[int]] = []
        for curr in range(length):
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            left: int = curr + 1
            right: int = length - 1
            while left < right:
                temp_sum: int = nums[curr] + nums[left] + nums[right]

                if temp_sum > 0:
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    triplets.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return triplets


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list, list]] = [
        (
            [-3, 0, 1, 2, -1, 1, -2],
            [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]],
        ),
        ([-5, 2, -1, -2, 3], [[-5, 2, 3], [-2, -1, 3]]),
        ([-5, -5, 0, 0, 5, 5], [[-5, 0, 5]]),
        ([1, 2, 3, 4, 5], []),
    ]

    check_result(solve.two_pointers, test_case)
