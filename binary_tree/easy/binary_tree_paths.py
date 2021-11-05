# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, path):
            if node is None:
                return

            path.append(str(node.val))
            dfs(node.left, path)
            dfs(node.right, path)

            if node.left is None and node.right is None:
                self.res.append("->".join(path))

            del path[-1]

        dfs(root, [])
        return self.res
