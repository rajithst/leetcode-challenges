from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_range = 0
        mem = {}
        for i in nums:
            mem[i] = True

        for i in nums:
            if not mem[i]:
                continue
            mem[i] = False
            current_length = 1
            next_val = i + 1
            prev_val = i - 1
            while prev_val in mem:
                mem[prev_val] = False
                current_length += 1
                prev_val -= 1
            while next_val in mem:
                mem[next_val] = False
                current_length += 1
                next_val += 1
            longest_range = max(longest_range, current_length)
        return longest_range
