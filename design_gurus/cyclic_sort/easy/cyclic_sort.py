from design_gurus.tests.test_foo import check_result


class Solution:
    def cyclic_sort(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        length: int = len(nums)

        i: int = 0
        while i < length:

            temp = nums[i]
            if temp != i:
                nums[i], nums[temp - 1] = nums[temp - 1], nums[i]

            i += 1

        return nums


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list]] = [
        ([4, 2, 5, 6, 3, 1, 8, 7], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([3, 2, 1], [1, 2, 3]),
    ]

    check_result(solve.cyclic_sort, test_case)
