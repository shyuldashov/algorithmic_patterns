from design_gurus.tests.test_foo import check_result


class Solution:
    def count_duplicates(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        length: int = len(arr)

        duplicates: int = 0
        for i in range(length - 1):
            if arr[i] == arr[i + 1]:
                duplicates += 1

        return length - duplicates

    def two_pointers(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        count: int = 1
        for i in range(1, len(arr)):
            if arr[i - 1] != arr[i]:
                count += 1

        return count


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list[int], int]] = [
        ([2, 3, 3, 3, 6, 9, 9], 4),
        ([2, 2, 2, 11], 2),
    ]

    check_result(solve.count_duplicates, test_case)
    check_result(solve.two_pointers, test_case)
