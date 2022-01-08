import heapq as heap
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # create frequency dictionary
        mem = {}
        for task in tasks:
            if task not in mem:
                mem[task] = 0
            mem[task] += 1

        # add frequency to maxheap
        maxheap = []
        for task, count in mem.items():
            heap.heappush(maxheap, (-count, task))

        units = 0
        while maxheap:
            # trying to do k+1 work till heap empty or do k+1 work
            # if we can do k+1 work,we don't need to wait cooling period
            # till we do k+1 work,we don't push used task,we keep it in waiting list
            k = n + 1
            waiting = []
            while k > 0 and maxheap:
                units += 1
                c, t = heap.heappop(maxheap)
                if -c > 1:
                    waiting.append((c + 1, t))
                k -= 1
            # add remaining to maxheap again
            for j in waiting:
                heap.heappush(maxheap, j)
            # if heap exhausted before doing k+1 work,we need to add remain work as cooling
            if maxheap:
                units += k
        return units