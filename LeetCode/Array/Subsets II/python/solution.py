class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # according to bit manupulation bit order 2**n eg: 2**3 = 8 subsets
        subset = 1 << n
        res = []
        for num in range(subset):
            temp = []
            for i in range(n):
                if num & (1 << i):
                    temp.append(nums[i])
            if sorted(temp) not in res:
                res.append(sorted(temp))
        return res
