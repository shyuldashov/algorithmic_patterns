from design_gurus.tests.test_foo import check_result


class Solution:
    def binary_search(self, num: int) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param num:
        :return:
        """
        if num in (0, 1):
            return num

        left: int = 0
        right: int = num
        while left <= right:
            middle: int = (left + right) // 2

            if (middle**2) == num:
                return middle

            if (middle**2) < num:
                left = middle + 1
            else:
                right = middle - 1

        return right


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[int, int]] = [
        (8, 2),
        (4, 2),
        (2, 1),
    ]

    check_result(solve.binary_search, test_case)
