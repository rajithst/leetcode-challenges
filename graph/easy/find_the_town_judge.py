from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n
        judge_out = {}
        judge_in = {}
        for p, j in trust:
            if j not in judge_out:
                judge_out[j] = 0
            if p not in judge_in:
                judge_in[p] = 0
            judge_out[j] += 1
            judge_in[p] += 1

        for j in judge_out.keys():
            if judge_out[j] == n - 1 and (j not in judge_in):
                return j
        return -1