import heapq as heap
from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(1, n + 1)}
        visited = set()
        for u, v, w in connections:
            adj_list[u].append([v, w])
            adj_list[v].append([u, w])
        # minimum spanning tree prims
        mst_weight = 0
        start = (0, connections[0][0])
        pq = []
        heap.heappush(pq, start)

        while pq:
            weight, node = heap.heappop(pq)
            if node in visited:
                continue
            mst_weight += weight
            visited.add(node)
            for ed in adj_list[node]:
                if ed[0] not in visited:
                    heap.heappush(pq, (ed[1], ed[0]))

        if len(visited) == n:
            return mst_weight
        else:
            return -1
