class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(st):
            if st == len(nums):
                res.append(nums[:])
            for i in range(st, len(nums)):
                nums[st], nums[i] = nums[i], nums[st]
                backtrack(st+1)
                nums[st], nums[i] = nums[i], nums[st]

        backtrack(0)
        return res
        