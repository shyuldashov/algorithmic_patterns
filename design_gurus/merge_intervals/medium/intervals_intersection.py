from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def intervals_intersection(
        self, nums_1: list[list[int]], nums_2: list[list[int]]
    ) -> list[list[int]]:
        """
        Time Complexity: O(m + n)
        Space Complexity: O(n)
        :param nums_1:
        :param nums_2:
        :return:
        """
        length_1: int = len(nums_1)
        length_2: int = len(nums_2)

        result: list[list[int]] = []
        left = right = 0
        while (left < length_1) and (right < length_2):
            start = max(nums_1[left][0], nums_2[right][0])
            end = min(nums_1[left][1], nums_2[right][1])

            if start <= end:
                result.append([start, end])

            if nums_1[left][1] < nums_2[right][1]:
                left += 1
            else:
                right += 1

        return result


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, list, list]] = [
        ([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]], [[2, 3], [5, 6], [7, 7]]),
        ([[1, 3], [5, 7], [9, 12]], [[5, 10]], [[5, 7], [9, 10]]),
        (
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        ([[1, 3], [5, 9]], [], []),
        ([], [[1, 3], [5, 9]], []),
    ]

    test_for_two_pointers(solve.intervals_intersection, test_case)
