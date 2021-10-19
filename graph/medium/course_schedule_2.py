from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = {}
        adj_list = {}
        for i in range(numCourses):
            indegrees[i] = 0
            adj_list[i] = []

        for c, pr in prerequisites:
            adj_list[pr].append(c)
            indegrees[c] += 1

        que = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                que.append(i)

        results = []
        while que:
            cn = que.popleft()
            results.append(cn)
            for nei in adj_list[cn]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    que.append(nei)
        if len(results) == numCourses:
            return results
        else:
            return []


