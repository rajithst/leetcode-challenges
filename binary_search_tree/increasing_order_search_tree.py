# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.results = []

    def increasingBST(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if node:
                dfs(node.left)
                self.results.append(node.val)
                dfs(node.right)

        dfs(root)

        root = TreeNode(self.results[0])
        new_head = root
        for nd in self.results[1:]:
            cn = TreeNode(nd)
            root.right = cn
            root = cn

        return new_head
