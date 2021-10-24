from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.results = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                self.results.append(node.val)

        dfs(root)
        return self.results
