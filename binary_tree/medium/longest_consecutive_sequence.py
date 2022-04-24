# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, val):
        self.max_length = val


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def dfs(node, parent, current_length, treeInfo):
            if not node:
                return
            if parent is not None and parent.val + 1 == node.val:
                current_length += 1
            else:
                current_length = 1
            treeInfo.max_length = max(treeInfo.max_length, current_length)
            dfs(node.left, node, current_length, treeInfo)
            dfs(node.right, node, current_length, treeInfo)

        ti = TreeInfo(0)
        dfs(root, None, 0, ti)
        return ti.max_length
