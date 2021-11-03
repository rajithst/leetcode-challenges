# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.results = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, current_path):
            if node is None:
                return

            current_path.append(node.val)
            if node.left is None and node.right is None:
                if sum(current_path) == targetSum:
                    self.results.append(current_path.copy())
            dfs(node.left, current_path)
            dfs(node.right, current_path)

            del current_path[-1]

        dfs(root, [])
        return self.results
