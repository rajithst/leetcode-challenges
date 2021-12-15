# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = {}

        def dfs(node, distance, depth):
            if node is None:
                return

            if distance not in memo:
                memo[distance] = []
            memo[distance].append([node.val, depth])
            dfs(node.left, distance - 1, depth + 1)
            dfs(node.right, distance + 1, depth + 1)

        dfs(root, 0, 0)
        keys = sorted(memo.keys())
        result = []
        for k in keys:
            memo[k].sort(key=lambda x: x[1])
            result.append([f[0] for f in memo[k]])

        return result
