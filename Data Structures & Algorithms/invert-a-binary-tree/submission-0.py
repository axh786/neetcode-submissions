# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # DFS preorder traversal solution solution
        if root is None: # Base Case
            return root
        
        root.left, root.right = root.right, root.left # Swap nodes
        self.invertTree(root.left) # run it on each child
        self.invertTree(root.right)

        return root # make sure to return
