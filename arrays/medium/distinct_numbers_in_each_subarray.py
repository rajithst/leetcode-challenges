from typing import List


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        ws = 0
        mem = {}
        res = []
        for we in range(n):
            cn = nums[we]
            if cn not in mem:
                mem[cn] = 0
            mem[cn] += 1

            if we >= k - 1:
                res.append(len(mem))
                rn = nums[ws]
                mem[rn] -= 1
                if mem[rn] == 0:
                    del mem[rn]
                ws += 1
        return res