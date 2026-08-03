class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            print(f"{res}= {res} ^ {i} => {res^i}")
            res ^= i
        for i in nums:
            print(f"{res}= {res} ^ {i} => {res^i}")
            res ^= i

        return res