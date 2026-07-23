import math
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = 0
        nums.sort()  # Group duplicates together
        n = len(nums)
        visited = [False] * n

        def isPerfectsqr(num):
            root = int(math.sqrt(num))
            return root * root == num

        def backtrack(temp):
            nonlocal count
            # Base case: valid squareful permutation found
            if len(temp) == n:
                count += 1
                return

            for i in range(n):
                # Skip if already used in current path
                if visited[i]:
                    continue
                
                # Bug Fix 2: Skip duplicates at the same tree depth
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                # Bug Fix 3: Safely check adjacent sum rule if path is not empty
                if len(temp) > 0:
                    adj_sum = temp[-1] + nums[i]
                    if not isPerfectsqr(adj_sum):
                        continue

                # Choose
                visited[i] = True
                temp.append(nums[i])

                # Explore
                backtrack(temp)

                # Bug Fix 1: Unchoose properly using pop()
                temp.pop()
                visited[i] = False

        backtrack([])
        return count
