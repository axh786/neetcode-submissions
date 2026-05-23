# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_help(p, q):
            if (not p and not q): # Can be rewritten with bools
                return 0
            elif not p:
                return 1
            elif not q:
                return 1
            elif p.val != q.val:
                return 1
            
            return dfs_help(p.left, q.left) + dfs_help(p.right, q.right)
        
        num = dfs_help(p, q)

        if num:
            return False
        
        return True
        