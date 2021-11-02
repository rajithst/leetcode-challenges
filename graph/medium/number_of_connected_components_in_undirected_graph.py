from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = {}
        adj_list = {}
        for i in range(n):
            visited[i] = False
            adj_list[i] = []

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            visited[node] = True
            for cd in adj_list[node]:
                if not visited[cd]:
                    dfs(cd)

        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        return components