# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ref = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(p, q, target):
            if p is None and q is None:
                return

            if target.val == p.val:
                self.ref = q

            dfs(p.left, q.left, target)
            dfs(p.right, q.right, target)

        dfs(original, cloned, target)
        return self.ref
