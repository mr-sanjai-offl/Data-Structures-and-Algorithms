class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        res = []
        idx = 0
        res.append(nums[0])
        for i in range(1,n):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                for idx in range(len(res)):
                    if res[idx] >= nums[i]:
                        res[idx] = nums[i]
                        break
        return len(res)