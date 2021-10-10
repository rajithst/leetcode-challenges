import heapq as heap
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}
        for u, v, w in times:
            if u not in adj_list:
                adj_list[u] = []
            adj_list[u].append((v, w))

        distance = {node: float("inf") for node in range(1, n + 1)}
        distance[k] = 0
        pq = []
        heap.heappush(pq, (0, k))
        while pq:
            weight_for_parent, parent_node = heap.heappop(pq)
            if parent_node not in adj_list:
                continue
            for nei_edge in adj_list[parent_node]:
                node, weight = nei_edge
                if weight_for_parent + weight < distance[node]:
                    distance[node] = weight_for_parent + weight
                    heap.heappush(pq, [distance[node], node])

        max_d = max(distance.values())
        if max_d == float("inf"):
            return -1
        return max_d