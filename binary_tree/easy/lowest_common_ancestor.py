# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parents = {}
        depth = {}

        def dfs(node, parent):
            if node:
                parents[node.val] = parent
                depth[node.val] = 0 if parent == None else depth[parent.val] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        def lca(u, v):
            if u == v:
                return u.val
            if depth[u.val] < depth[v.val]:
                u, v = v, u

            diff = depth[u.val] - depth[v.val]
            while diff != 0:
                u = parents[u.val]
                diff -= 1
            while u != v:
                u = parents[u.val]
                v = parents[v.val]
            return u

        return lca(p, q)
