from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def dfs_helper(node, path):
            if node == target:
                results.append(list(path))
                return

            neis = graph[node]
            for nei in neis:
                path.append(nei)
                dfs_helper(nei, path)
                path.pop()

        path = deque([0])
        dfs_helper(0, path)
        return results

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        target = len(graph) -1
        que = deque()
        que.append([source])
        result = []

        while que:
            cr = que.popleft()
            if cr[-1] == target:
                result.append(cr)
            else:
                for n in graph[cr[-1]]:
                    que.append(cr+[n])
        return result