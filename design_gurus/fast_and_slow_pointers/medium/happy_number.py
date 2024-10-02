from design_gurus.tests.test_foo import check_result


class Solution:
    def is_happy(self, n: int) -> bool:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param n:
        :return:
        """
        sums: set[int] = set()
        while n != 1:
            n = self._get_the_sum_squares_of_digits(n)

            if n in sums:
                return False
            sums.add(n)

        return True

    def _get_the_sum_squares_of_digits(self, num: int) -> int:
        total_sum: int = 0
        while num > 0:
            total_sum += (num % 10) ** 2
            num //= 10

        return total_sum


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[int, bool]] = [
        (82, True),
        (2, False),
        (1, True),
        (65536, False),
        (25, False),
        (1111, False),
    ]

    check_result(solve.is_happy, test_case)
