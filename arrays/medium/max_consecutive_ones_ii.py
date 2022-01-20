from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        window_start = 0
        one_count = 0
        max_len = 0
        max_freq = 0
        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                one_count += 1
            max_freq = max(max_freq, one_count)
            if window_end - window_start + 1 - max_freq > 1:
                remove = nums[window_start]
                if remove == 1:
                    one_count -= 1
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)
        return max_len
