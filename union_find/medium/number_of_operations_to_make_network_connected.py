from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        root = [-1] * n
        rank = [1] * n
        extra = 0

        def find(node):
            if root[node] == -1:
                return node
            root[node] = find(root[node])
            return root[node]

        def union(u, v):
            nonlocal extra
            ru = find(u)
            rv = find(v)
            if ru != rv:
                if rank[ru] > rank[rv]:
                    root[rv] = ru
                    rank[ru] += rank[rv]
                    return ru
                else:
                    root[ru] = rv
                    rank[rv] += rank[ru]
                    return rv

            else:
                extra += 1
                return None

        group = set()
        for u, v in connections:
            grp = union(u, v)
            group.add(u)
            group.add(v)

        first = list(group)[0]
        used = 0
        for i in range(n):
            if i not in group:
                if extra > 0:
                    union(i, first)
                    extra -= 1
                    used += 1
                    group.add(i)
                else:
                    return -1

            elif find(i) != find(first):
                if extra > 0:
                    union(i, first)
                    extra -= 1
                    used += 1
                else:
                    return -1
        return used
