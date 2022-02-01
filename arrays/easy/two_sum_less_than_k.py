from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        maximum = -1
        while p1 < p2:
            s = nums[p1] + nums[p2]
            if s < k:
                maximum = max(maximum, s)
                p1 += 1
            else:
                p2 -= 1
        return maximum
