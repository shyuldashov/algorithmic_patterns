from design_gurus.tests.test_foo import check_result


class Solution:
    def sliding_window(self, fruits: list[str]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param fruits:
        :return:
        """
        basket: dict[str, int] = {}
        left = max_fruits = 0
        for curr in range(len(fruits)):
            basket[fruits[curr]] = basket.get(fruits[curr], 0) + 1

            while len(basket) > 2:
                temp_count: int = basket.get(fruits[left])

                if temp_count == 1:
                    basket.pop(fruits[left])
                else:
                    basket[fruits[left]] -= 1
                left += 1

            max_fruits = max(curr - left + 1, max_fruits)

        return max_fruits


if __name__ == "__main__":
    solve = Solution()
    test_case: list[tuple[list, int]] = [
        (["a", "b", "a", "a", "c", "d", "b", "b", "b", "b", "d"], 6),
        (["a", "b", "a"], 3),
        (["a", "b", "c", "d"], 2),
        (["a", "a", "a", "c", "b", "b", "c", "c", "a", "a"], 5),
    ]

    check_result(solve.sliding_window, test_case)
