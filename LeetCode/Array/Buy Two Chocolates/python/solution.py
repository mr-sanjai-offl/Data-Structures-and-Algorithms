class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n=0
        c=0
        money1=money
        prices.sort()
        for i in prices[0:2]:
            if(i<=money1):
                money1-=i
                c+=i
                n+=1
        if n>=2:
            return money-c
        else:
            return money
            
        