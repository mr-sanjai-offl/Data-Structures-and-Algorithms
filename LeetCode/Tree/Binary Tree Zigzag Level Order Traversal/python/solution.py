from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cnt = 0
        if not root:
            return res
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if cnt%2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
            cnt+=1
        return res
            
                
            