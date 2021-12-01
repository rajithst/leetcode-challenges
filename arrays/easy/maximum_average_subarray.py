from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p1 = 0
        p2 = k - 1
        n = len(nums)
        mv = cs = sum(nums[p1:p2 + 1])
        for i in range(p2 + 1, n):
            cs += nums[i]
            cs -= nums[i - k]
            mv = max(mv, cs)
        return mv / k

