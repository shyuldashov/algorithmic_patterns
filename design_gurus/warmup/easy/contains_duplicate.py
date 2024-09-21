from design_gurus.tests.test_foo import check_result


class Solution:
    def brute_force(self, nums: list[int]) -> bool:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        length: int = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    return True
        return False

    def using_set(self, nums: list[int]) -> bool:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list[int], bool]] = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([1, 2, 1, 3, 3], True),
    ]
    check_result(solve.brute_force, test_case)
    check_result(solve.using_set, test_case)
