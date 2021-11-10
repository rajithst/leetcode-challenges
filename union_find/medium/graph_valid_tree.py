from typing import List


class Solution:
    def __init__(self):
        self.valid = True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        self.root = [-1] * n
        self.rank = [1] * n

        def find(node):
            if self.root[node] == -1:
                return node
            self.root[node] = find(self.root[node])
            return self.root[node]

        def union(u, v):
            ru = find(u)
            rv = find(v)
            if ru != rv:
                if self.rank[ru] < self.rank[rv]:
                    self.root[ru] = rv
                    self.rank[rv] += self.rank[ru]

                else:
                    self.root[rv] = ru
                    self.rank[ru] += self.rank[rv]
                return True
            else:
                return False

        for x, y in edges:
            if not union(x, y):
                return False
        return True
