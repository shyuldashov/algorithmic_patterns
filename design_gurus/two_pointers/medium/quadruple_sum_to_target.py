import time
from random import choices

from design_gurus.tests.test_two_pointers import test_for_two_pointers


class Solution:
    def two_pointers_recursive(
        self, nums: list[int], target: int
    ) -> list[list]:
        """
        Time Complexity: O(n^3)
        Space Complexity: O(n^2)
        :param nums:
        :param target:
        :return:
        """

        def recursive_sum(k: int, curr_start: int, curr_target: int) -> None:
            if k == 2:
                left, right = curr_start, len(nums) - 1
                while left < right:
                    temp_sum: int = nums[left] + nums[right]
                    if temp_sum == curr_target:
                        quadruples.append(
                            temp_quadruple + [nums[left], nums[right]]
                        )
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                        while nums[right] == nums[right + 1] and left < right:
                            right -= 1
                    elif temp_sum < curr_target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(curr_start, len(nums) - k + 1):
                    if i > curr_start and nums[i] == nums[i - 1]:
                        continue
                    temp_quadruple.append(nums[i])
                    recursive_sum(k - 1, i + 1, curr_target - nums[i])
                    temp_quadruple.pop()

        nums.sort()
        quadruples, temp_quadruple = [], []
        recursive_sum(4, 0, target)
        return quadruples


if __name__ == "__main__":
    solve = Solution()
    times: list[float] = []
    for _ in range(1000):
        test_case: list[tuple[list, int, list]] = [
            ([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
            ([2, 0, -1, 1, -2, 2], 2, [[-2, 0, 2, 2], [-1, 0, 1, 2]]),
            (choices(range(int(-1e6), int(1e6)), k=200), int(1e9), []),
        ]
        start_time = time.time()
        test_for_two_pointers(solve.two_pointers_recursive, test_case)
        end_time = time.time()
        times.append(end_time - start_time)

    avg_time: float = sum(times) / len(times)
    print(f"Среднее время {avg_time:0.4f} сек. для 200 элементов")
    # TODO: Можно ли уменшить T до O(n^2) или O(n^2 * n log n)
