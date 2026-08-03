class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ss = 1<<n
        res = []
        for num in range(0,ss):
            sublist = []
            for i in range(0,n):
                if num & (1 << i):
                    sublist.append(nums[i-1])
            res.append(sublist)
        return res