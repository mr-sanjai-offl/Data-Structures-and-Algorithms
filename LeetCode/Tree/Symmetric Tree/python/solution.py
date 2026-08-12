# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def level_ord(root):
            if not root:
                return True
          
            q = deque([root])

            while q:
                lenq = len(q)
                level = []
                for _ in range(lenq):

                    cur = q.popleft()
                    if cur:
                        level.append(cur.val)
                      
                        q.append(cur.left)

                      
                        q.append(cur.right)
                    else:
                        level.append(None)

                    
                if level != level[::-1]:
                    return False
                if max(q) is None: 
                    break
            return True
        
        return level_ord(root)

        