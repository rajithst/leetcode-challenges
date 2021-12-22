from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return root

        q = deque()
        q.append([root, 0])
        val = None
        depth = 0
        while q:
            l = len(q)
            for i in range(l):
                node, branch = q.popleft()
                if i == 0:
                    val = node.val
                if node.left:
                    q.append([node.left, 1])
                if node.right:
                    q.append([node.right, 2])
            depth += 1
        return val
