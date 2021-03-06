# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return root
        que = deque()
        que.append(root)
        result = []
        while que:
            l = len(que)
            lv = float("-inf")
            for _ in range(l):
                cn = que.popleft()
                lv = max(lv, cn.val)
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
            result.append(lv)
        return result


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        mem = {}

        def dfs(node, depth):
            if node is None:
                return
            if depth not in mem:
                mem[depth] = float("-inf")
            mem[depth] = max(mem[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return mem.values()