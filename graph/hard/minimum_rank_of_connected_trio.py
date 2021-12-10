from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:

        adj_matrix = [[0] * (n + 1) for row in range(n + 1)]
        indegrees = {r: 0 for r in range(1, n + 1)}
        for i, j in edges:
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1
            indegrees[i] += 1
            indegrees[j] += 1

        min_degree = float("inf")
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if adj_matrix[i][j] and adj_matrix[j][k] and adj_matrix[k][i]:
                        current_degree = indegrees[i] + indegrees[j] + indegrees[k] - 6
                        min_degree = min(min_degree, current_degree)

        return -1 if min_degree == float("inf") else min_degree