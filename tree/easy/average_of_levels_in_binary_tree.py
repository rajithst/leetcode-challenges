from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(self, root: Optional[TreeNode]) -> List[float]:
    if root is None:
        return 0

    que = deque()
    que.append(root)

    results = []

    while que:
        current_length = len(que)
        level_tot = 0
        for _ in range(current_length):
            current_node = que.popleft()
            level_tot += current_node.val

            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
        results.append(level_tot / current_length)
    return results
