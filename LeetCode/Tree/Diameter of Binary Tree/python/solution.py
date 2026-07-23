# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dia = [0]
        def height(root,dia):
            if root == None:
                return 0
            left = height(root.left,dia)
            right = height(root.right,dia)

            dia[0] = max(dia[0],left+right)

            return 1 + max(left,right)
        height(root,dia)
        return dia[0]
        