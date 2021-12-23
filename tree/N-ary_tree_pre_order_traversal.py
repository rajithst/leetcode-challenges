"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        result = []

        def dfs(node):
            if node is None:
                return
            result.append(node.val)
            for ch in node.children:
                dfs(ch)

        dfs(root)
        return result