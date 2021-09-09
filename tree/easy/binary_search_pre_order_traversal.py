from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        value_list = []

        def traversal(node):
            if node:
                value_list.append(node.val)
                traversal(node.left)
                traversal(node.right)
            return value_list

        return traversal(root)
