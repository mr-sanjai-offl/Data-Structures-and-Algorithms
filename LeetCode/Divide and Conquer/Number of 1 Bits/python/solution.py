class Solution:
    def hammingWeight(self, n: int) -> int:
        #recursion
        # if n == 1:
        #     return 1
        # return n%2 + self.hammingWeight(n//2)

        #string
        # return bin(n)[2:].count('1')
        
        #USING RIGHT SHIFT
        w = 0
        for i in range(32):
            w += n >> i & 1
        return w

        



