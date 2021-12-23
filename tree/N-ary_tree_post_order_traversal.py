from collections import deque
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            result.append(node.val)

        dfs(root)
        return result
