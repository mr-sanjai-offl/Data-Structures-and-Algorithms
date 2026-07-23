class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        curmax = curmin = nums[0]
        maxval = minval = nums[0]
        for i in range(1,n):
            curmax = max(nums[i], curmax + nums[i])
            curmin = min(nums[i], curmin + nums[i])
            maxval = max(maxval,curmax)
            minval = min(minval,curmin)
        print(minval,maxval)
        return max(abs(minval),abs(maxval))