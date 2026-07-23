class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res=[0]*2
        for i,j in enumerate(bin(n)[2:][::-1]):
            if j == '1':
                if (i) % 2 == 0:
                    res[0] += 1
                else:
                    res[1] += 1

        return res