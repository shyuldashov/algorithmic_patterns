class Solution:
    def two_pointers_first(self, nums: list[int], target: int) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        nums.sort()  # O(n log n)

        length: int = len(nums)
        total_sum: int | float = float("inf")
        min_distance: int | float = float("inf")
        for curr in range(length):
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            left: int = curr + 1
            right: int = length - 1
            while left < right:
                temp_sum: int = nums[curr] + nums[left] + nums[right]
                if temp_sum == target:
                    return temp_sum

                temp_distance: int = abs(temp_sum - target)
                if temp_distance < min_distance:
                    min_distance = temp_distance
                    total_sum = temp_sum
                elif temp_distance == min_distance:
                    total_sum = min(total_sum, temp_sum)

                if temp_sum < target:
                    left += 1
                else:
                    right -= 1

        return total_sum

    def two_pointers_second(self, nums: list[int], target: int) -> int:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        nums.sort()  # O(n log n)

        length: int = len(nums)
        min_distance: int | float = float("inf")
        for curr in range(length - 2):
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            left: int = curr + 1
            right: int = length - 1
            while left < right:
                temp_distance: int = target - (
                    nums[curr] + nums[left] + nums[right]
                )

                if temp_distance == 0:
                    return target

                if abs(temp_distance) < abs(min_distance) or (
                    abs(temp_distance) == abs(min_distance)
                    and temp_distance > min_distance
                ):
                    min_distance = temp_distance

                if temp_distance > 0:
                    left += 1
                elif temp_distance <= 0:
                    right -= 1

        return target - min_distance


if __name__ == "__main__":
    solve = Solution()

    def test(foo) -> None:
        test_case: list[tuple[list[int], int, int]] = [
            ([-1, 0, 2, 3], 3, 2),
            ([-3, -1, 1, 2], 1, 0),
            ([1, 0, 1, 1], 100, 3),
            ([0, 0, 1, 1, 2, 6], 5, 4),
            ([0, 0, 0], 0, 0),
            ([1, 2, 3, 4, 5], 6, 6),
            ([39, -55, 11, 69, 4, -9, 6, 23], -72, -60),
        ]

        for data, target, expected in test_case:
            result = foo(data, target)

            assert (
                result == expected
            ), f"{data}, {target} - got {result}, expected {expected}"

        print("ok")

    test(solve.two_pointers_first)
    test(solve.two_pointers_second)
