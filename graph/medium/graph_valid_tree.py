from typing import List


class Solution:
    def __init__(self):
        self.valid = True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = {i: [] for i in range(n)}
        visited = {i: 0 for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, parent):
            visited[node] = 1
            for cd in adj_list[node]:
                if not visited[cd]:
                    dfs(cd, node)
                elif cd != parent and visited[cd] == 1:
                    self.valid = False
            visited[node] = 2

        dfs(0, -1)
        for v in visited.keys():
            if not visited[v]:
                return False
        return self.valid
