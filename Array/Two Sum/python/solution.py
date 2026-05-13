class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if(nums[i]+nums[j]==target):
        #             return [i,j]

        #Hash Table O(n)
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return[numMap[complement], i]
            numMap[num] = i

        # numMap={}

        # for i in range(0,len(nums)):
        #     temp = target - nums[i]
        #     if temp in numMap:
        #         return [numMap[temp], i]
        #     numMap[nums[i]] = i
            

        