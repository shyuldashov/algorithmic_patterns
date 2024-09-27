from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def two_pointers(self, nums: list[int], target: int) -> list[list]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        :param nums:
        :param target:
        :return:
        """
        length: int = len(nums)
        if length == 1:
            return [nums] if nums[0] < target else []

        result: list[list[int]] = []
        left: int = 0
        prod: int = 1
        for right in range(length):

            prod *= nums[right]
            while (left <= right) and (prod >= target):
                prod //= nums[left]
                left += 1

            result.extend(
                [
                    [nums[i]] + nums[i + 1 : right + 1]
                    for i in range(right, left - 1, -1)
                ]
            )

        return result


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list, int, list]] = [
        (
            [2, 5, 3, 10],
            30,
            [[2], [5], [2, 5], [3], [5, 3], [10]],
        ),
        (
            [8, 2, 6, 5],
            50,
            [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]],
        ),
        (
            [1],
            2,
            [[1]],
        ),
        (
            [10],
            5,
            [],
        ),
        (
            [1, 2, 3, 4, 5],
            10,
            [[1], [2], [1, 2], [3], [2, 3], [1, 2, 3], [4], [5]],
        ),
        (
            [477, 338, 671, 745, 351, 3, 996, 532, 241],
            99,
            [[3]],
        ),
        (
            [1, 1, 1, 1],
            1000_000,
            [
                [1],
                [1],
                [1, 1],
                [1],
                [1, 1],
                [1, 1, 1],
                [1],
                [1, 1],
                [1, 1, 1],
                [1, 1, 1, 1],
            ],
        ),
    ]
    test_for_two_pointers(solve.two_pointers, test_case)

    # TODO: Можно ли оптимизировать решение?
