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

        result: list[list[int]] = []
        new_start, new_end = new_interval
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]

            if new_end < curr_start:
                result.append([new_start, new_end])
                return result + intervals[i:]

            if new_start > curr_end:
                result.append(intervals[i])
            else:
                new_start = min(curr_start, new_start)
                new_end = max(curr_end, new_end)

        result.append([new_start, new_end])

        return result


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
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[5, 7]], [1, 7], [[1, 7]]),
        ([], [5, 7], [[5, 7]]),
    ]

    test_for_two_pointers(solve.insert_interval, test_case)
