class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal): return False
        for i in range(1,n+1):
            if(goal == s[i:n] + s[0:i]): return True
        return False