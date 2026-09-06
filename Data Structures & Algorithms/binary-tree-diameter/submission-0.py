# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        def height(a):
            if a==None:
                return 0
            self.d=max(self.d,height(a.left)+height(a.right))
            return 1+max(height(a.left),height(a.right))
        height(root)
        return self.d
        