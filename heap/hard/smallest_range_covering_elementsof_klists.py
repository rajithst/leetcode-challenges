import heapq as heap
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        pq = []
        rangeStart, rangeEnd = float("-inf"), float("inf")
        max_number = float("-inf")
        for i in range(len(nums)):
            heap.heappush(pq, (nums[i][0], 0, nums[i]))
            max_number = max(max_number, nums[i][0])

        # lets take number of lists as 3
        # since we pop value from one list and insert value from same list
        # we make sure that everytime heap contains 3 values from each list
        # if we take minimum of 3 values as lower bound,it contains range of other lists

        while len(pq) == len(nums):

            val, listindex, cl = heap.heappop(pq)
            if max_number - val < rangeEnd - rangeStart:
                rangeStart = val
                rangeEnd = max_number

            if len(cl) > listindex + 1:
                heap.heappush(pq, (cl[listindex + 1], listindex + 1, cl))
                max_number = max(max_number, cl[listindex + 1])
        return [rangeStart, rangeEnd]