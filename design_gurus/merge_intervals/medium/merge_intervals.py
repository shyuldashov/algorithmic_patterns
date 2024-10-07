from design_gurus.tests.test_foo import check_result


class Solution:
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :param intervals:
        :return:
        """
        if not intervals:
            return []

        # sort by starting intervals
        intervals.sort(key=lambda items: items[0])  # O(n log n)

        result: list[list[int]] = []
        start, end = intervals[0]  # unpack the first interval
        for curr_start, curr_end in intervals:

            if curr_start <= end:
                end = max(curr_end, end)
            else:
                result.append([start, end])
                start, end = curr_start, curr_end

        result.append([start, end])

        return result

    def merge_intervals_in_place(
        self, intervals: list[list[int]]
    ) -> list[list[int]]:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        :param intervals:
        :return:
        """
        if not intervals:
            return []

        # sort by starting intervals
        intervals.sort(key=lambda items: items[0])  # O(n log n)

        length: int = len(intervals)
        left: int = 0
        curr: int = 1
        while curr < length:

            if intervals[curr][0] <= intervals[left][1]:
                intervals[left][1] = max(
                    intervals[left][1],
                    intervals[curr][1],
                )
            else:
                left += 1
                intervals[left] = intervals[curr]

            curr += 1

        return intervals[: left + 1]


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list]] = [
        ([[1, 4], [2, 5], [7, 9]], [[1, 5], [7, 9]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[6, 7], [2, 4], [5, 9]], [[2, 4], [5, 9]]),
        ([[1, 4], [2, 6], [3, 5]], [[1, 6]]),
        ([[2, 3], [1, 2], [2, 7], [2, 4]], [[1, 7]]),
        ([[8, 9], [8, 9], [8, 9], [8, 9]], [[8, 9]]),
    ]

    check_result(solve.merge_intervals_in_place, test_case)
    check_result(solve.merge_intervals, test_case)
