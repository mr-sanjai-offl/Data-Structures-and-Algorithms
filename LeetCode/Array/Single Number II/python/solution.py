class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        s = [i for i in c if c[i] == 1]
        return max(s)