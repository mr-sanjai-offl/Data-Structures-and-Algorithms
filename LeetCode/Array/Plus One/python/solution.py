class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return [int(j) for j in str(int("".join([str(i) for i in digits])) + 1)]
        num = 0
        for i in digits:
            num = num*10 + i
        num+=1
        res = []
        
        while num != 0:
            res.append(num%10)
            num //= 10
        return res[::-1]
