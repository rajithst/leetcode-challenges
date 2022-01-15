from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ws = 0
        n = len(nums)
        subarray_sum = 0
        minlength = float("inf")
        for we in range(n):
            subarray_sum += nums[we]

            while subarray_sum >= target:
                minlength = min(minlength, we - ws + 1)
                subarray_sum -= nums[ws]
                ws += 1
        return minlength if minlength != float("inf") else 0