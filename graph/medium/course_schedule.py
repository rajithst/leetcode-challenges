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