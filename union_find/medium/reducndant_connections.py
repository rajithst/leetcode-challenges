from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        self.root = [-1] * 1001
        self.rank = [1] * 1001

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

        backedges = []
        for u, v in edges:
            if not union(u, v):
                backedges.append([u, v])
        return backedges[-1]
