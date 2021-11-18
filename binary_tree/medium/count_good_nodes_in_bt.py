# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, cm):
            if node:
                cm.append(node.val)
                if max(cm) <= node.val:
                    self.count += 1

                dfs(node.left, cm)

                dfs(node.right, cm)
                del cm[-1]

        dfs(root, [])
        return self.count
