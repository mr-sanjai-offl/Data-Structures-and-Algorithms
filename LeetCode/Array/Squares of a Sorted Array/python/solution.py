class Solution:
    def sortedSquares(self, nums):
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] * nums[i])
        arr.sort()
        return arr