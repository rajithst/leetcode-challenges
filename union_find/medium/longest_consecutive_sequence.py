from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        root = [-1] * n
        rank = [1] * n

        def find(u):
            if root[u] == -1:
                return u
            root[u] = find(root[u])
            return root[u]

        def union(u, v):
            ru = find(u)
            rv = find(v)
            if ru != rv:
                if rank[ru] > rank[rv]:
                    root[rv] = ru
                    rank[ru] += rank[rv]
                else:
                    root[ru] = rv
                    rank[rv] += rank[ru]

        nodes = {}
        cnt = 0
        for num in nums:
            if num not in nodes:
                nodes[num] = cnt

                if num + 1 in nodes:
                    union(nodes[num], nodes[num + 1])
                if num - 1 in nodes:
                    union(nodes[num], nodes[num - 1])
            cnt += 1
        return max(rank)


