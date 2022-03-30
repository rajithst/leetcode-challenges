# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        # inorder traversal
        def dfs(node, info):
            if not node:
                return

            dfs(node.left, info)

            if node.val == info.prev:
                info.count += 1
            else:
                info.count = 1

            if info.count > info.max_count:
                info.max_count = info.count
                info.results.clear()
                info.results.append(node.val)
            elif info.count == info.max_count:
                info.results.append(node.val)

            info.prev = node.val
            dfs(node.right, info)

        class treeinfo:
            def __init__(self):
                self.results = []
                self.prev = None
                self.max_count = 0
                self.count = 0

        info = treeinfo()
        info.prev = root.val
        dfs(root, info)
        return info.results
