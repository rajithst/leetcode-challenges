from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_BST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return root
    return traverse(root, val)


def traverse(current_node, val):
    if current_node:
        if current_node.val == val:
            return current_node
        if val > current_node.val:
            return traverse(current_node.right, val)
        else:
            return traverse(current_node.left, val)
