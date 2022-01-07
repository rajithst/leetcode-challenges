import heapq as heap


class Solution:
    def reorganizeString(self, s: str) -> str:
        mem = {}
        for i in s:
            if i not in mem:
                mem[i] = 0
            mem[i] += 1

        maxheap = []
        for k, v in mem.items():
            heap.heappush(maxheap, (-v, k))
        res = []
        prevK = None
        prevV = 0
        while maxheap:
            v, k = heap.heappop(maxheap)
            if prevK and -prevV > 0:
                heap.heappush(maxheap, (prevV, prevK))

            res.append(k)
            prevV = v + 1
            prevK = k
        return "".join(res) if len(res) == len(s) else ""
