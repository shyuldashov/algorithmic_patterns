class Solution:
    def brute_force(self, words: list[str], first: str, second: str) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param words:
        :param first:
        :param second:
        :return:
        """
        length: int = len(words)
        min_distance: int = length

        for i in range(length):
            if words[i] == first:
                for j in range(length):
                    if words[j] == second:
                        min_distance = min(min_distance, abs(i - j))

        return min_distance

    def simple_iter(self, words: list[str], first: str, second: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param words:
        :param first:
        :param second:
        :return:
        """
        left = right = -1
        length: int = len(words)
        min_distance: int = length

        for i in range(length):
            if words[i] == first:
                left = i
            elif words[i] == second:
                right = i

            if left != -1 and right != -1:
                min_distance = min(min_distance, abs(left - right))
        return min_distance


if __name__ == "__main__":
    solve = Solution()

    def test(foo) -> None:
        test_case: list[tuple[list[str], str, str, int]] = [
            (
                [
                    "the",
                    "quick",
                    "brown",
                    "fox",
                    "jumps",
                    "over",
                    "the",
                    "lazy",
                    "dog",
                ],
                "fox",
                "dog",
                5,
            ),
            (
                ["a", "c", "d", "b", "a"],
                "a",
                "b",
                1,
            ),
        ]

        for data, val_1, val_2, expected in test_case:
            result = foo(data, val_1, val_2)

            assert (
                result == expected
            ), f"{data}\n{val_1}, {val_2}- got {result} expected {expected}"
        print("ok!")

    test(solve.brute_force)
    test(solve.simple_iter)
