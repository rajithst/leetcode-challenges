"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return root

        que = deque()
        que.append(root)
        results = []
        while que:
            level_length = len(que)
            lv = []
            for c in range(level_length):
                cn = que.popleft()
                lv.append(cn.val)
                que.extend(cn.children)
            results.append(lv)
        return results