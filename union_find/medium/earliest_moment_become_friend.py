from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

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

        logs.sort(key=lambda x: x[0])
        for t, u, v in logs:
            union(u, v)
            if self.components == 1:
                return t
        return -1
