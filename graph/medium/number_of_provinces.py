from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = {n: False for n in range(len(isConnected))}
        adj_list = {n: [] for n in range(len(isConnected))}

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        def dfs(node):
            visited[node] = True
            for c in adj_list[node]:
                if not visited[c]:
                    dfs(c)

        provinces = 0
        for i in visited.keys():
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces
