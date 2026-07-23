class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)-2
        res = []
        for i in range(0,n):
            if num[i:i+3] == num[i]*3:
                res.append(num[i:i+3])

        res.sort(reverse=True)
        return "" if not res else res[0]
        
        