class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        # step1 = 1
        # step2 = 2
        # i=3
        # while(i<=n):
        #     ways = step1 + step2
        #     step1 = step2
        #     step2 = ways
        #     i+=1
        # return ways
    
        step = [1]*n
        step[0] = 1
        step[1] = 2
        for i in range(2,n):
            step[i] = step[i-1]+step[i-2]
        return step[-1]

        
