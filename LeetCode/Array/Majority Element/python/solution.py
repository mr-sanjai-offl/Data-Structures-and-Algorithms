class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = {}
        n = len(nums)
        b =  set(nums)
        for i in b:
            r[i]=0
        for j in nums:
            r[j]+=1
            if r[j] > n//2:
                return j
        return -1

