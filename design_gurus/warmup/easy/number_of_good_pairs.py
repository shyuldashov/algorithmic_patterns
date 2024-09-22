from collections import Counter

from design_gurus.tests.test_foo import check_result


class Solution:
    def brute_force(self, data: list[int]) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param data:
        :return:
        """
        length: int = len(data)

        good_pairs: int = 0
        for i in range(length):
            for j in range(i + 1, length):
                if data[i] == data[j]:
                    good_pairs += 1

        return good_pairs

    def use_dict(self, data: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param data:
        :return:
        """

        # frequency: dict[int, int] = {}
        # for num in data:
        #     frequency[num] = frequency.get(num, 0) + 1

        frequency: dict[int, int] = Counter(data)
        good_pairs: int = 0
        for num, freq in frequency.items():
            if freq >= 2:
                good_pairs += (freq * (freq - 1)) // 2

        return good_pairs


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list[int], int]] = [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
    ]

    check_result(solve.brute_force, test_case)
    check_result(solve.use_dict, test_case)
