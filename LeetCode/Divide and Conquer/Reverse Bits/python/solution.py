class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31,-1,-1):
            if n >> 31-i & 1 == 1:
                res += 2**i
        return res