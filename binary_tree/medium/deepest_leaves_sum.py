from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        que = deque()
        que.append([root, 0])
        depth = 0
        deepest_sum = 0
        while que:
            node, curr_depth = que.popleft()

            if node.left is None and node.right is None:
                if curr_depth > depth:
                    deepest_sum = node.val
                    depth = curr_depth
                elif depth == curr_depth:
                    deepest_sum += node.val
            else:
                if node.left:
                    que.append([node.left, curr_depth + 1])
                if node.right:
                    que.append([node.right, curr_depth + 1])
        return deepest_sum
