import heapq as heap
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []
        for i in range(k):
            diff = abs(x - arr[i])
            heap.heappush(maxheap, (-1 * diff, arr[i]))

        for i in range(k, len(arr)):
            diff = abs(x - arr[i])
            if maxheap[0][0] * -1 > diff:
                heap.heappop(maxheap)
                heap.heappush(maxheap, (-1 * diff, arr[i]))

        results = []
        while len(maxheap) > 0:
            _, v = heap.heappop(maxheap)
            results.append(v)
        return sorted(results)
