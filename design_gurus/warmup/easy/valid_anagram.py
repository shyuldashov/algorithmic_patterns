from collections import Counter


class Solution:
    def sort_values(self, first: str, second: str) -> bool:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :param first:
        :param second:
        :return:
        """
        if len(first) != len(second):
            return False

        return sorted(first.lower()) == sorted(second.lower())

    def use_dict(self, first: str, second: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param first:
        :param second:
        :return:
        """
        if len(first) != len(second):
            return False

        return Counter(first) == Counter(second)


if __name__ == "__main__":
    solve = Solution()

    def test(foo) -> None:
        test_case: list[tuple[str, str, bool]] = [
            ("listen", "silent", True),
            ("rat", "car", False),
            ("hello", "world", False),
            ("meat", "team", True),
        ]

        for val_1, val_2, expected in test_case:
            result = foo(val_1, val_2)

            assert (
                result == expected
            ), f"{val_1}, {val_2} - got {result} expected {expected}"
        print("ok!")

    test(solve.sort_values)
    test(solve.use_dict)
