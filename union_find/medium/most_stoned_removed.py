from typing import List


class Solution:
    def __init__(self):
        self.count = 0

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        root = [-1] * n
        rank = [1] * n

        def find(node):
            if root[node] == -1:
                return node
            root[node] = find(root[node])
            return root[node]

        def union(u, v):
            ru = find(u)
            rv = find(v)
            if ru != rv:
                if rank[ru] > rank[rv]:
                    root[ru] = rv
                    rank[rv] += rank[ru]
                else:
                    root[rv] = ru
                    rank[ru] += rank[rv]
                self.count += 1

        for i in range(n):
            for j in range(i + 1, n):
                r, c = stones[i]
                rr, cc = stones[j]
                if r == rr or c == cc:
                    union(i, j)
        return self.count
