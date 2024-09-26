from typing import Any, Callable


class Search:
    def binary_search_classic(self, arr: list[Any], target: Any) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param arr:
        :param target:
        :return:
        """
        left: int = 0
        right: int = len(arr) - 1
        while left <= right:

            middle: int = (left + right) // 2
            if arr[middle] == target:
                return middle
            elif arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    def binary_search_first_occurrence(
        self, arr: list[Any], target: Any
    ) -> int:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param arr:
        :param target:
        :return:
        """
        left: int = 0
        right: int = len(arr) - 1
        find_index: int = -1
        while left <= right:

            middle: int = (left + right) // 2
            if arr[middle] == target:
                find_index = middle
                right = middle - 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return find_index

    def linear_search(self, arr: list[Any], target: Any) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param arr:
        :param target:
        :return:
        """
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1

    @staticmethod
    def test(foo: Callable, data: list[list | tuple]) -> None:
        for data, target, expected in data:
            result = foo(data, target)
            assert (
                result == expected
            ), f"{data}, {target} - got {result}, expected {expected}"
        print("ok!")


if __name__ == "__main__":
    search = Search()

    test_case: list[tuple[list, int, int]] = [
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7),
        ([-9, -3, -1, 0, 0, 2], 0, 3),
        ([-8, -7, -7, -6, -5, -4, -3, -3, -2, -1], -7, 1),
        ([0, 0, 0, 0, 0], 0, 0),
        ([0, 0, 0, 0, 0], 5, -1),
        ([-93, -87, -54, -41, 9, 14, 36, 47, 66, 68, 85, 93], 93, 11),
    ]

    Search.test(search.binary_search_first_occurrence, test_case)
    Search.test(search.linear_search, test_case)
