from typing import List


class Solution:
    def __init__(self):
        self.ans = True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(1, n + 1)}
        for u, v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = {i: 0 for i in range(1, n + 1)}

        def dfs(node, parent, color):
            visited[node] = color
            for cd in adj_list[node]:
                if visited[cd] == 0:
                    dfs(cd, node, 3 - color)
                elif cd != parent and visited[cd] == color:
                    self.ans = False

        for i in range(1, n + 1):
            if visited[i] == 0:
                dfs(i, -1, 1)
        return self.ans
