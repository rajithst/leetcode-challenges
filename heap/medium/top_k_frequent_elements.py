import heapq as heap
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        minheap = []
        for key, frq in freq.items():
            heap.heappush(minheap, (frq, key))
            if len(minheap) > k:
                heap.heappop(minheap)
        result = []
        for _ in range(k):
            cv = heap.heappop(minheap)
            result.append(cv[1])
        return result