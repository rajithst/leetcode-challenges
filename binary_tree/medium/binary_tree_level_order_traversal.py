from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# should populate same level values in a same list
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return root

    # since this is level order traversal we need a queue to traverse as normal BFS
    queue = deque()

    #start from appending root node
    queue.append(root)
    results = []

    #while queue is not empty iterate
    while queue:
        #since we need to store same level values in a same list,we need to iterate over same level nodes while iterating over levels
        #get length of the queue
        current_length = len(queue)
        level_results = []

        #iterate over queue
        for _ in range(current_length):
            #each time pop the node from queue and get the value,same time insert node's children to the queue
            current_node = queue.popleft()
            level_results.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        results.append(level_results)
    return results
