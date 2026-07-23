import math
class Solution:
    def countPrimes(self, n: int) -> int:
        # if n<=2:
        #     return 0
        # count = 0
        # for i in range(2,n):
        #     isPrime = 1
        #     for j in range(2,i):
        #         if i%j==0:
        #             isPrime = 0
        #             break
        #     count+=isPrime if isPrime == 1 else 0
        # return count

        if n<=2:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.sqrt(n))+1):
            if isPrime[i]:
                for j in range(i*i,n,i):
                    isPrime[j] = False
        return sum(isPrime)
