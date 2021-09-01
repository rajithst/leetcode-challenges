from typing import Optional, List


# inorder traversal -- > left->data->right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.value_list = []

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        self.traversal(root)
        return self.value_list

    def traversal(self, node):
        if node.left:
            self.traversal(node.left)
        if node.val:
            self.value_list.append(node.val)
        if node.right:
            self.traversal(node.right)
