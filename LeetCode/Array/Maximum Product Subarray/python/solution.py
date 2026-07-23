from math import prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currmax = currmin = nums[0]
        maxpro = nums[0]

        for i in range(1,n):
            if nums[i] < 0:
                currmax, currmin = currmin, currmax
            currmax = max(nums[i], currmax * nums[i])
            currmin = min(nums[i], currmin * nums[i])
            maxpro = max(maxpro,currmax)
        return maxpro
                