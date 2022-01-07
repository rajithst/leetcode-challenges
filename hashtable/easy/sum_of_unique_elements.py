from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = 0
        mem = {}
        for i in nums:
            if i not in mem:
                mem[i] = 0
            mem[i] += 1

        for k, v in mem.items():
            if v == 1:
                s += k
        return s