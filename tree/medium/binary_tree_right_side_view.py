from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return root

    que = deque()
    que.append(root)
    results = []
    while que:
        level_length = len(que)
        for i in range(level_length):
            current_node = que.popleft()

            if i == level_length - 1:
                results.append(current_node.val)

            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
    return results
