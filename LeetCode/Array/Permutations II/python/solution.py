class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(st):
            if st == len(nums) and nums not in res:
                res.append(nums[:])
                return
            for i in range(st,len(nums)):
                nums[st], nums[i] = nums[i], nums[st]
                dfs(st+1)
                nums[st], nums[i] = nums[i], nums[st]
        dfs(0)
        return res
            

