import heapq as heap
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        pq = []
        for i in nums:
            heap.heappush(pq, i)

        return [heap.heappop(pq) for i in range(len(pq))]