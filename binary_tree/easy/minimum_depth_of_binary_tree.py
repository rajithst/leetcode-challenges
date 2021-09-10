from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#purpose is finding minimum depth
#it's not easy to keep track of left and right side depth if we traverse DFS
#if we traverse level wise,we can check if any node is a leaf node,it is the minimum depth
#use normal BFS and increase depth at each level

def min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    #normal queue based BFS
    que = deque()
    que.append(root)
    minimum_depth = 0

    while que:
        #increase depth at each level
        minimum_depth += 1
        level_size = len(que)
        #iterate over each node in level
        for _ in range(level_size):
            current_node = que.popleft()

            #core logic - check if node is a leaf node..if it is a leaf node return the minimum depth
            if current_node.left is None and current_node.right is None:
                return minimum_depth
            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
    return minimum_depth
