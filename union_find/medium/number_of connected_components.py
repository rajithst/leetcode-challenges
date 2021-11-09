from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.root = [-1] * n
        self.rank = [1] * n
        self.components = n

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
                self.components -= 1

        for u, v in edges:
            union(u, v)
        return self.components
