from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def insert_interval(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param intervals:
        :param new_interval:
        :return:
        """
        if not intervals:
            return [new_interval]

        if not new_interval:
            return intervals

        start, end = new_interval
        curr: int = 0
        length: int = len(intervals)
        while curr < length and intervals[curr][1] < start:
            curr += 1

        intervals.insert(curr, new_interval)

        return self._merge_intervals_in_place(intervals)

    def _merge_intervals_in_place(
        self, intervals: list[list[int]]
    ) -> list[list[int]]:
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

    def insert_interval_in_place(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param intervals:
        :param new_interval:
        :return:
        """
        if not intervals:
            return [new_interval]

        if not new_interval:
            return intervals

        start, end = new_interval
        curr: int = 0
        length: int = len(intervals)
        while curr < length and intervals[curr][1] < start:
            curr += 1

        if not curr:
            intervals.insert(0, new_interval)
            return intervals

        if curr == length:
            intervals.append(new_interval)
            return intervals

        left: int = curr
        while curr < length and intervals[curr][0] <= end:
            start = min(start, intervals[curr][0])
            end = max(end, intervals[curr][1])
            curr += 1

        intervals[left] = [start, end]
        left += 1

        while curr < length:
            intervals[left] = intervals[curr]
            left += 1
            curr += 1

        return intervals[:left]


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list, list]] = [
        ([[1, 3], [5, 7], [8, 12]], [4, 6], [[1, 3], [4, 7], [8, 12]]),
        ([[1, 3], [5, 7], [8, 12]], [4, 10], [[1, 3], [4, 12]]),
        (
            [[1, 6], [8, 10], [15, 18]],
            [20, 25],
            [[1, 6], [8, 10], [15, 18], [20, 25]],
        ),
        (
            [[4, 6], [8, 10], [15, 18]],
            [1, 3],
            [[1, 3], [4, 6], [8, 10], [15, 18]],
        ),
    ]

    test_for_two_pointers(solve.insert_interval_in_place, test_case)
    test_for_two_pointers(solve.insert_interval, test_case)
