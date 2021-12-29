import heapq as heap
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for i in range(min(k, len(matrix))):
            heap.heappush(pq, (matrix[i][0], 0, matrix[i]))

        count = 0
        val = None
        while pq:
            val, index, row = heap.heappop(pq)
            count += 1
            if count == k:
                break
            if len(row) > index + 1:
                heap.heappush(pq, (row[index + 1], index + 1, row))

        return val