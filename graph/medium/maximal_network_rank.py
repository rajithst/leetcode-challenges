from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        for i, j in roads:
            adj_list[i].append(j)
            adj_list[j].append(i)

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                current_rank = len(adj_list[i]) + len(adj_list[j])
                if i in adj_list[j]:
                    current_rank -= 1
                max_rank = max(max_rank, current_rank)

        return max_rank