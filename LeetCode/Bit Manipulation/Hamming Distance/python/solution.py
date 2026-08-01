class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #String function
        # return bin(x^y)[2:].count('1')
        #logic
        cnt = 0
        for i in range(32):
            cnt += x >> i & 1 ^ y >> i & 1
        return cnt