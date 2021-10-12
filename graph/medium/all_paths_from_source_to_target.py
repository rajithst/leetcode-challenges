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
