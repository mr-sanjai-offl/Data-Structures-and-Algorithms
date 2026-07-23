class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sort=[]
        sort=sorted(list(nums))
        result=(sort[-1]*sort[-2])-(sort[0]*sort[1])
        return result
