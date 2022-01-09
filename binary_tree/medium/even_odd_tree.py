# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        que = deque()
        que.append(root)
        level = 0
        while que:
            ll = len(que)
            prev = None
            for _ in range(ll):
                cn = que.popleft()
                if level % 2 == 0:
                    if cn.val % 2 == 0 or (prev != None and prev >= cn.val):
                        return False
                else:
                    if cn.val % 2 == 1 or (prev != None and prev <= cn.val):
                        return False
                prev = cn.val
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)

            level += 1
        return True