class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
                maxlen = max(maxlen,cnt)
            else:
                cnt = 0
        return maxlen

