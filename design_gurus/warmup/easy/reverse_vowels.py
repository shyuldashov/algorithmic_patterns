from design_gurus.tests.test_foo import check_result


class Solution:
    _VOWELS: str = "aeiouAEIOU"

    @classmethod
    def get_vowels(cls) -> str:
        return cls._VOWELS

    def two_pointers(self, text: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param text:
        :return:
        """
        text: list[str] = list(text)
        vowels: str = self.get_vowels()

        left: int = 0
        right: int = len(text) - 1
        while left < right:
            if text[left] in vowels and text[right].lower() in vowels:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            elif text[left] in vowels:
                right -= 1
            else:
                left += 1

        return "".join(text)

    def two_pointers_with_nested_loops(self, text: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param text:
        :return:
        """
        text: list[str] = list(text)
        vowels: str = self.get_vowels()

        left: int = 0
        right: int = len(text) - 1
        while left < right:

            while left < right and text[left] not in vowels:
                left += 1

            while left < right and text[right] not in vowels:
                right -= 1

            text[left], text[right] = text[right], text[left]

            left += 1
            right -= 1

        return "".join(text)


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[str, str]] = [
        ("hello", "holle"),
        ("AEIOU", "UOIEA"),
        ("DesignGUrus", "DusUgnGires"),
        ("LeetCode", "LeotCede"),
        ("CodeRun", "CudeRon"),
    ]
    check_result(solve.two_pointers, test_case)
    check_result(solve.two_pointers_with_nested_loops, test_case)
