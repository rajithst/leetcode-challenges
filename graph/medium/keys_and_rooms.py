from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        adj_list = {key: [] for key in range(len(rooms))}
        visited = {key: False for key in range(len(rooms))}

        for i in range(len(rooms)):
            for key in rooms[i]:
                adj_list[i].append(key)

        def dfs(node):
            visited[node] = True
            for cd in adj_list[node]:
                if not visited[cd]:
                    dfs(cd)

        dfs(0)
        for k in visited.keys():
            if visited[k] == False:
                return False
        return True
