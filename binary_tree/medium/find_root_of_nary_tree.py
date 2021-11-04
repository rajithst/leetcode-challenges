from typing import List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':

        seen = set()
        for node in tree:
            for nd in node.children:
                seen.add(nd.val)

        for ed in tree:
            if ed.val not in seen:
                return ed