import string

from design_gurus.tests.test_foo import check_result


class Solution:
    def use_set(self, sentence: str) -> bool:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param sentence:
        :return:
        """
        return set(string.ascii_lowercase).issubset(sentence.lower())

    def use_include(self, sentence: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param sentence:
        :return:
        """
        sentence = sentence.lower()
        return all(char in sentence for char in string.ascii_lowercase)


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[str, bool]] = [
        ("TheQuickBrownFoxJumpsOverTheLazyDog", True),
        ("This is not a pangram", False),
        ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
    ]
    check_result(solve.use_set, test_case)
    check_result(solve.use_include, test_case)
