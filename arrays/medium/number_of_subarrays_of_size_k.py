from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window_start = 0
        count = 0
        cs = 0
        for window_end in range(len(arr)):
            cs += arr[window_end]

            if window_end >= k:
                remove = arr[window_start]
                cs -= remove
                window_start += 1

            if (window_end - window_start + 1) == k and cs / k >= threshold:
                count += 1
        return count