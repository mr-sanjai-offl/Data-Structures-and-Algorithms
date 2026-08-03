class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        for i in range(32):
            if (start >> i & 1) ^ (goal >> i & 1):
                flips += 1
        return flips 