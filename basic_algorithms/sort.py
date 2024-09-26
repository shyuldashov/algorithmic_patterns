from typing import Any, Callable


class Sort:
    def quicksort(self, arr: list[Any]) -> list[Any]:
        """
        Time Complexity: O(n^2) -> ~O(n log n)
        Space Complexity: O(n)
        :param arr:
        :return:
        """
        length: int = len(arr)

        if length <= 1:
            return arr

        left: list = []
        middle: list = []
        right: list = []
        pivot: Any = arr[length // 2]
        for value in arr:
            if value < pivot:
                left.append(value)
            elif value > pivot:
                right.append(value)
            else:
                middle.append(value)

        return self.quicksort(left) + middle + self.quicksort(right)

    def bubble_sort(self, arr: list[Any]) -> list[Any]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        length: int = len(arr)

        for i in range(length):
            for j in range(length - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def merge_sort(self, arr: list[Any]) -> list[Any]:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :param arr:
        :return:
        """
        length: int = len(arr)

        if length <= 1:
            return arr
        middle: int = length // 2
        left: list[Any] = self.merge_sort(arr[:middle])
        right: list[Any] = self.merge_sort(arr[middle:])

        return self._merge(left, right)

    def _merge(self, left: list[Any], right: list[Any]) -> list[Any]:
        result: list[Any] = []
        l_length, r_length = len(left), len(right)
        i = j = 0
        while (i < l_length) and (j < r_length):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def insertion_sort(self, arr: list[Any]) -> list[Any]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        for i in range(1, len(arr)):
            j: int = i
            while (j > 0) and (arr[j] > arr[i]):
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = arr[i]

        return arr

    def selection_sort(self, arr: list[Any]) -> list[Any]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        length: int = len(arr)
        for i in range(length - 1):
            curr_min_index: int = i

            for j in range(i + 1, length):
                if arr[j] < arr[curr_min_index]:
                    curr_min_index = j

            if curr_min_index != i:
                arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]

        return arr

    @staticmethod
    def test(foo: Callable, data: list[list | tuple]) -> None:
        for value, expected in data:
            result = foo(value)
            assert (
                result == expected
            ), f"{value} - got {result}, expected {expected}"
        print("ok!")


if __name__ == "__main__":
    sort = Sort()
    test_case: list[tuple[list, list]] = [
        (
            [9, 0, 5, 7, 1, 8, 2, 6, 4, 3],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        ),
        (
            [-1, 0, -9, -3, 0, 2],
            [-9, -3, -1, 0, 0, 2],
        ),
        (
            [-2, -3, -7, -8, -3, -4, -6, -1, -5, -7],
            [-8, -7, -7, -6, -5, -4, -3, -3, -2, -1],
        ),
        (
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ),
        (
            [85, 14, 68, -54, -41, 66, 9, 36, -93, 47, -87, 93],
            [-93, -87, -54, -41, 9, 14, 36, 47, 66, 68, 85, 93],
        ),
    ]

    Sort.test(sort.quicksort, test_case)
    Sort.test(sort.bubble_sort, test_case)
    Sort.test(sort.merge_sort, test_case)
    Sort.test(sort.insertion_sort, test_case)
    Sort.test(sort.selection_sort, test_case)
