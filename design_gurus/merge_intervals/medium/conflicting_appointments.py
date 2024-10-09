from design_gurus.tests.test_foo import check_result


class Solution:
    def conflicting_appointments(self, intervals: list[list[int]]) -> bool:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda interval: interval[0])  # O(n log n)

        _, prev_end = intervals[0]  # unpack the first interval
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start <= prev_end:
                return False

            prev_end = min(curr_end, prev_end)

        return True


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, bool]] = [
        ([[1, 4], [2, 5], [7, 9]], False),
        ([[6, 7], [2, 4], [13, 14], [8, 12], [45, 47]], True),
        ([[4, 5], [2, 3], [3, 6]], False),
        ([[0, 1]], True),
    ]

    check_result(solve.conflicting_appointments, test_case)
