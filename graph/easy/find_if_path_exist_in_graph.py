from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        if start == end:
            return True

        adj_list = {}
        for f, t in edges:
            if f not in adj_list:
                adj_list[f] = []
            if t not in adj_list:
                adj_list[t] = []
            adj_list[f].append(t)
            adj_list[t].append(f)

        visited = {}
        for k in adj_list.keys():
            visited[k] = False
        que = deque()
        que.append(start)
        visited[start] = True
        while que:
            current_node = que.popleft()
            for nei in adj_list[current_node]:
                if not visited[nei]:
                    visited[nei] = True
                    que.append(nei)
                    if nei == end:
                        return True

        return False