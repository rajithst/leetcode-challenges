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
            length = len(que)
            for i in range(length):
                cn = que.popleft()
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
                if i < length - 1:
                    cn.next = que[0]
        return root
