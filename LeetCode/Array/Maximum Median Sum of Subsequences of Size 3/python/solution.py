class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        sum = 0
        for i in range(n//3, n, 2):
            sum += nums[i]
        return sum
    
       