from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # if target is less than or equal to 1,result is 0
        # since array as positive values,we can't find any subarray less than 1
        if k <= 1:
            return 0

        # we need to find subarray,we can create a sliding window that satisfies target
        window_start = 0
        product = 1
        result = 0

        # move front of the window  and keep multiply the values
        for window_end in range(len(nums)):
            product *= nums[window_end]

            # at any point,product >= target and pointers are valid
            # shrink the window from the beginning till product < target
            # this way we can slide window forward
            while product >= k and window_start < len(nums):
                product /= nums[window_start]
                window_start += 1
            # while window movig forward,we need to add "count of new subarrays" that product < k
            # because when we add a new value to window,we have new set of subarrays including new value
            # in a given window,maximum product value is at window_end position
            # if window_end product is less than target,means all subarray products within window less than target
            # number of `new subarrays` in a window is, window_end - window_start +1
            # [10 , 5 , 2 , 6 ]
            #       ^       ^
            #       |       |
            #       ws      we
            # i 0    1   2   3
            # new subarrays = [6],[6,2],[6,2,5]
            # new subarrays = 3 - 1 + 1
            result += window_end - window_start + 1
        return result