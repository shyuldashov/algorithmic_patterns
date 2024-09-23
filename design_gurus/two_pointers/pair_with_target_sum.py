class Solution:
    def two_pointers(self, arr: list[int], target_sum: int) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param arr:
        :param target_sum:
        :return:
        """
        left: int = 0
        right: int = len(arr) - 1
        while left < right:
            temp_sum: int = arr[left] + arr[right]
            if temp_sum == target_sum:
                return [left, right]

            if temp_sum > target_sum:
                right -= 1
            else:
                left += 1

        return [-1, -1]

    def use_dict(self, arr: list[int], target_sum: int) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param arr:
        :param target_sum:
        :return:
        """
        data: dict[int, int] = {}

        for index, num in enumerate(arr):
            diff: int = target_sum - num
            if diff in data:
                return [data[diff], index]
            data[num] = index

        return [-1, -1]


if __name__ == "__main__":
    solve = Solution()

    def test(foo):
        test_case: list[tuple[list[int], int, list[int]]] = [
            ([1, 2, 3, 4, 6], 6, [1, 3]),
            ([2, 5, 9, 11], 11, [0, 2]),
            ([3, 6, 9], 7, [-1, -1]),
        ]

        for nums, target, expected in test_case:
            result: list[int] = foo(nums, target)
            assert (
                result == expected
            ), f"{nums}, {target} - got {result} expected {expected}"
        print("ok!")

    test(solve.two_pointers)
    test(solve.use_dict)
