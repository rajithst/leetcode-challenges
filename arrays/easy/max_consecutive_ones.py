from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        con = 0
        max_con = 0
        for i in nums:
            if i == 1:
                con += 1
                max_con = max(max_con, con)
            else:

                con = 0
        return max_con
