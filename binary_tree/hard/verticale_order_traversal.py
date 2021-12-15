# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = {}

        def dfs(node, distance, depth):
            if node is None:
                return

            if distance not in memo:
                memo[distance] = []
            memo[distance].append([depth, node.val])
            dfs(node.left, distance - 1, depth + 1)
            dfs(node.right, distance + 1, depth + 1)

        dfs(root, 0, 0)
        keys = sorted(memo.keys())
        result = []
        for k in keys:
            tmp = sorted(memo[k])
            result.append([f[1] for f in tmp])

        return result
