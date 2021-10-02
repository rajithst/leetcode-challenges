from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        if len(graph) == 0:
            return

        visited = {}
        for i in range(len(graph)):
            visited[i] = 0

        def dfs_helper(current_node, parent_node, color, visited):
            visited[current_node] = color
            adj_list = graph[current_node]

            for nei in adj_list:
                if visited[nei] == 0:
                    sub_result = dfs_helper(nei, current_node, 3 - color, visited)
                    if not sub_result:
                        return False

                elif (nei != parent_node) and (color == visited[nei]):
                    return False
            return True

        res = dfs_helper(0, 1, -1, visited)
        if not res:
            return False

        for i in visited:
            if visited[i] == 0:
                res_new = dfs_helper(i, 1, -1, visited)
                if not res_new:
                    return False
        return True
