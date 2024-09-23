from design_gurus.tests.test_foo import check_result


class Solution:
    def two_pointers(self, arr: list[int]) -> list[int]:
        length: int = len(arr)

        left: int = 0
        right = pos = length - 1
        result: list[int] = [0] * length
        while pos >= 0:
            square_left: int = arr[left] ** 2
            square_right: int = arr[right] ** 2

            if square_left > square_right:
                result[pos] = square_left
                left += 1
            else:
                result[pos] = square_right
                right -= 1
            pos -= 1

        return result


if __name__ == "__main__":
    solve = Solution()

    test_case: list[tuple[list[int], list[int]]] = [
        ([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
        ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9]),
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-1, -2, -3, -4], [1, 4, 9, 16]),
    ]

    check_result(solve.two_pointers, test_case)
