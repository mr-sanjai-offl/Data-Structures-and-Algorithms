class Solution:
    def search(self, nums, target):
        x = 0
        y = len(nums) - 1

        while x <= y:
            i = (x + y) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                x = i + 1
            else:
                y = i - 1

        return -1