# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def findRoot(root,subRoot):
            if root is None:
                return False
            elif root.val==subRoot.val:
                res = match(root,subRoot)
                if res:
                    return res
            
            return findRoot(root.left,subRoot) or findRoot(root.right,subRoot)

        def match(root,subRoot):
            if not root and not subRoot:
                return True
            elif (not subRoot and root) or (not root and subRoot):
                return False
            elif root.val!=subRoot.val:
                return False

            return match(root.left,subRoot.left) and match(root.right,subRoot.right)

        return findRoot(root,subRoot)