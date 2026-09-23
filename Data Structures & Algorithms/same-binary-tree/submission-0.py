# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ST(p,q):
            if p is None and q is None:
                return True
            elif (p is None and q is not None) or (p is not None and q is None):
                return False
            elif p.val!=q.val:
                return False

            return ST(p.left,q.left) and ST(p.right,q.right)

        return ST(p,q)
