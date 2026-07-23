class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        j = 1
        for _ in range(n):
            c = i+j
            i, j = j, c
  
        return j