from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def simple_approach(self, first: str, second: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param first:
        :param second:
        :return:
        """

        def apply_backspace(raw_text: str) -> str:
            if "#" not in raw_text:
                return raw_text

            backspaces: int = 0
            text: str = ""
            for i in range(len(raw_text) - 1, -1, -1):
                if raw_text[i] == "#":
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    text = raw_text[i] + text

            return text

        return apply_backspace(first) == apply_backspace(second)

    def two_pointers(self, first: str, second: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param first:
        :param second:
        :return:
        """

        def get_next_valid_char_index(raw_text: str, curr_length: int) -> int:
            backspaces: int = 0
            while curr_length >= 0:
                if raw_text[curr_length] == "#":
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    break
                curr_length -= 1
            return curr_length

        first_len: int = len(first) - 1
        second_len: int = len(second) - 1
        while first_len >= 0 or second_len >= 0:
            first_len = get_next_valid_char_index(first, first_len)
            second_len = get_next_valid_char_index(second, second_len)

            if (
                first_len >= 0
                and second_len >= 0
                and first[first_len] != second[second_len]
            ) or ((first_len >= 0) != (second_len >= 0)):
                return False

            first_len -= 1
            second_len -= 1

        return True


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[str, str, bool]] = [
        ("xy#z", "xzz#", True),
        ("xy#z", "xyz#", False),
        ("xp#", "xyz##", True),
        ("abcde#####", "ijklm#####", True),
        ("#", "#", True),
        ("#ba#", "#ab#", False),
        ("abcdefgdsfgdfg###", "xyz###", False),
    ]

    test_for_two_pointers(solve.simple_approach, test_case)
    test_for_two_pointers(solve.two_pointers, test_case)
