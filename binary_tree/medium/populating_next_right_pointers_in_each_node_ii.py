"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root is None:
            return root
        que = deque()
        que.append(root)
        while que:
            ln = len(que)
            prev = None
            for i in range(ln):
                cn = que.popleft()
                if prev is not None:
                    prev.next = cn
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
                prev = cn

        return root