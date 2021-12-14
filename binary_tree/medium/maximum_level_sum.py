# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        que = deque()
        que.append(root)
        level = 1
        ans = 1
        current_max = float("-inf")
        while (que):
            ll = len(que)
            level_sum = 0
            for _ in range(ll):
                cn = que.popleft()
                level_sum += cn.val
                if cn.left:
                    que.append(cn.left)
                if cn.right:
                    que.append(cn.right)
            if level_sum > current_max:
                current_max = level_sum
                ans = level
            level += 1
        return ans
