import heapq as heap


class Solution:
    def frequencySort(self, s: str) -> str:

        memo = {}
        for i in s:
            if i not in memo:
                memo[i] = 0
            memo[i] += 1

        pq = []
        for k, v in memo.items():
            heap.heappush(pq, (-1 * v, k))
        string = ""
        for i in range(len(pq)):
            t, v = heap.heappop(pq)
            string += v * (-1 * t)
        return string