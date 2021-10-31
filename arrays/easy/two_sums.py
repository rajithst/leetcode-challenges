from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [seen[remaining], idx]
            else:
                seen[value] = idx