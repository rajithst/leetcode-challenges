# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root
        que = deque()
        que.append(root)
        stack = deque()
        while que:
            ll = len(que)
            level = []
            for _ in range(ll):
                cn = que.popleft()
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
                level.append(cn.val)
            stack.appendleft(level)

        return stack
