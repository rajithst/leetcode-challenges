from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        count = 0
        if root is None:
            return root

        def dfs(node):
            nonlocal count
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            if node.val == left_sum + right_sum:
                count += 1
            return node.val + left_sum + right_sum

        dfs(root)
        return count
