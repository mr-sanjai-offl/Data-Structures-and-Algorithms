class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in ans:
                return ans[remain], i
            ans[nums[i]] = i