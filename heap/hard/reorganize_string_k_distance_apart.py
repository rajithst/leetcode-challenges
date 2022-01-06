import heapq as heap
from collections import deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        mem = {}
        for i in s:
            if i not in mem:
                mem[i] = 0
            mem[i] += 1

        maxheap = []
        for key, v in mem.items():
            heap.heappush(maxheap, (-v, key))
        res = []
        que = deque()
        while maxheap:
            v, key = heap.heappop(maxheap)
            res.append(key)
            que.append((v + 1, key))
            if len(que) == k:
                pv, pk = que.popleft()
                if -pv > 0:
                    heap.heappush(maxheap, (pv, pk))
        return "".join(res) if len(res) == len(s) else ""
