class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        res = False
        for i in range(0,20):
            if 4**i == n:
                res = True
                break
        return res
                
        