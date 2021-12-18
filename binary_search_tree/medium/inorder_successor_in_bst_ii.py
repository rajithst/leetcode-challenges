"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        if node.right is not None:
            temp = node.right
            while temp.left is not None:
                temp = temp.left

            return temp

        root = node
        while root.parent and root.parent.right is root:
            root = root.parent

        return root.parent
