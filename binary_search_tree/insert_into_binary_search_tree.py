from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_BST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        root = TreeNode(val)
        return root

    def traverse(current_node, val):
        if current_node:
            if val > current_node.val:
                if current_node.right:
                    traverse(current_node.right, val)
                else:
                    current_node.right = TreeNode(val)
            else:
                if current_node.left:
                    traverse(current_node.left, val)
                else:
                    current_node.left = TreeNode(val)

    traverse(root, val)
