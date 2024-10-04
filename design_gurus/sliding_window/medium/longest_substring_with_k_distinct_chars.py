from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def longest_substring(self, line: str, k) -> int:
        max_longest: int = 0
        length: int = len(line)

        for curr in range(length):
            left: int = curr
            sub_str_length = distinct_count = 0
            seen: set[str] = set()

            while left < length:
                if line[left] not in seen:
                    distinct_count += 1
                    seen.add(line[left])

                if distinct_count > k:
                    break

                sub_str_length = left - curr + 1
                left += 1

            max_longest = max(sub_str_length, max_longest)

        return max_longest


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[str, int, int]] = [
        ("araaci", 2, 4),
        ("araaci", 1, 2),
        ("cbbebi", 3, 5),
        ("", 0, 0),
        ("abcd", 4, 4),
    ]

    test_for_two_pointers(solve.longest_substring, test_case)
