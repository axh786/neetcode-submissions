# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareSubTree(root, subRoot): # checks if the root matches the subroot
            if root is None and subRoot is None:
                return True

            elif root is None or subRoot is None:
                return False
                
            if root.val != subRoot.val:
                return False
            
            return compareSubTree(root.left, subRoot.left) and compareSubTree(root.right, subRoot.right)

        if root is None:
            return False
        
        if root.val == subRoot.val:
            if compareSubTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    