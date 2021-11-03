# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, current_path):
            if node is None:
                return

            current_path.append(node.val)
            path_count = len(current_path)
            path_sum = 0
            for i in range(path_count - 1, -1, -1):
                path_sum += current_path[i]
                if path_sum == targetSum:
                    self.count += 1
            dfs(node.left, current_path)
            dfs(node.right, current_path)
            del current_path[-1]

        dfs(root, [])
        return self.count
