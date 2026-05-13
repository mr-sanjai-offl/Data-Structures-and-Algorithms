class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {} #dictionary hash table
        for i in range(len(nums)):
            remain = target - nums[i] #find the remainder
            if remain in res:
                return res[remain], i #return the result if in the map
            res[nums[i]] = i #add to map