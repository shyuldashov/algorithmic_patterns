from design_gurus.tests.test_foo import check_result


class Solution:
    def find_missing_number(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        length: int = len(nums)
        self._cyclic_sort(nums, length)

        for i in range(length):
            if nums[i] != i:
                return i

        return length

    def _cyclic_sort(self, nums: list[int], length: int) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        i: int = 0
        while i < length:

            temp: int = nums[i]
            if (temp < length) and (temp != i):
                nums[i], nums[temp] = nums[temp], nums[i]
                continue

            i += 1

    def xor(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        result: int = 0
        for i in range(0, len(nums) + 1):
            result ^= i

        for num in nums:
            result ^= num

        return result


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, int]] = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([1, 2, 0, 3, 5], 4),
    ]

    check_result(solve.xor, test_case)
    check_result(solve.find_missing_number, test_case)
