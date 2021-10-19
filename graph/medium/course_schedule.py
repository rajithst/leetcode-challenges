from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = {}
        callstack = {}
        coursemap = {}

        for c in range(numCourses):
            visited[c] = False
            callstack[c] = False
            coursemap[c] = []

        for c, pr in prerequisites:
            coursemap[pr].append(c)

        def dfs(node, callstack):
            visited[node] = True
            callstack[node] = True

            for nei in coursemap[node]:
                if callstack[nei]:
                    return True
                elif not visited[nei]:
                    cycle_found = dfs(nei, callstack)
                    if cycle_found:
                        return True
            callstack[node] = False
            return False

        for v in range(numCourses):
            if not visited[v]:
                if dfs(v, callstack):
                    return False
        return True


from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        indegrees = {}
        for c in range(numCourses):
            indegrees[c] = 0
            adj_list[c] = []

        total_dependencies = 0
        for c, pr in prerequisites:
            indegrees[c] += 1
            adj_list[pr].append(c)
            total_dependencies += 1

        que = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                que.append(i)

        finished_dependencies = 0
        finished_courses = 0
        while que:
            cn = que.popleft()
            finished_courses += 1
            for nei in adj_list[cn]:
                indegrees[nei] -= 1
                finished_dependencies += 1

                if indegrees[nei] == 0:
                    que.append(nei)
        if finished_courses == numCourses:
            return True
        else:
            return False