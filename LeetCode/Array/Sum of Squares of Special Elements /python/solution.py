class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        l = len(nums)
        for i,n in enumerate(nums):
            if l%(i+1)==0:
                sum+=n**2
        return sum