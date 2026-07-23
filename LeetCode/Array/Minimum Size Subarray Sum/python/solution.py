class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minsum = 0
        length = float('inf')
        n = len(nums)
        while(r < n):
            minsum += nums[r]
            while(minsum >= target):
                length = min(length,r-l+1)
                minsum -= nums[l]
                l+=1
            r+=1
        return 0 if length == float('inf') else length
