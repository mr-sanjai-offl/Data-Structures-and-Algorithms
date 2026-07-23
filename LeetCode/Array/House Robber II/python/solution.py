class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        

        def costcalc(res):
            s = len(res)
            res[1] = max(res[0],res[1])
            for i in range(2,s):
                res[i] = max(res[i-1], res[i-2]+res[i])
            return res[-1]
      
        res1 = nums[0:n-1]
        res2 = nums[1:n]

        return max(costcalc(res1),costcalc(res2))
        

