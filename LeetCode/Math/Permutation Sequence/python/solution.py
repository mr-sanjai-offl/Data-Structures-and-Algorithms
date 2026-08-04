from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        for i, j in enumerate(permutations([i for i in range(1,n+1)])):
            if i == k-1:
                return "".join(map(str,j))

        


