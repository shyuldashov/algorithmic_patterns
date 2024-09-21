import re

from design_gurus.tests.test_foo import check_result


class Solution:
    def brute_force(self, sentence: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param sentence:
        :return:
        """
        sentence: str = "".join(
            char for char in sentence if char.isalpha() or char.isdigit()
        ).lower()
        return sentence == sentence[::-1]

    def regex_method(self, sentence: str):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param sentence:
        :return:
        """
        sentence: str = re.sub(
            r"[^a-z0-9]", "", sentence, flags=re.IGNORECASE
        ).lower()
        return sentence == sentence[::-1]

    def two_pointers(self, sentence: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param sentence:
        :return:
        """
        left: int = 0
        right: int = len(sentence) - 1
        while left < right:
            while (left < right) and not (
                sentence[left].isalpha() or sentence[left].isdigit()
            ):
                left += 1

            while (left < right) and not (
                sentence[right].isalpha() or sentence[right].isdigit()
            ):
                right -= 1

            if sentence[left].lower() != sentence[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[str, bool]] = [
        ("A man, a plan, a canal, Panama!", True),
        ("Was it a car or a cat I saw?", True),
        ("Some Text", False),
    ]
    check_result(solve.brute_force, test_case)
    check_result(solve.regex_method, test_case)
    check_result(solve.two_pointers, test_case)
