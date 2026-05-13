1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        
4        ans = {}
5        for i in range(len(nums)):
6            remain = target - nums[i]
7            if remain in ans:
8                return ans[remain], i
9            ans[nums[i]] = i