class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while i <= 32:
            if 1 << i == n:
                return True
            i += 2
        return False 