class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':

        # if target node is not a leaf node
        if p.right is not None:
            temp = p.right
            while temp.left is not None:
                temp = temp.left
            return temp

        # if target node is a leaf node
        temp = root
        succ = None
        while temp is not None:
            if temp.val > p.val:
                succ = temp
                temp = temp.left
            elif temp.val < p.val:
                temp = temp.right
            else:
                break
        return succ
