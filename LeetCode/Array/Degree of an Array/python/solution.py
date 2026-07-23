class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # size = len(nums)
        # freq = {}
        # first_ocr = {}
        # last_ocr = {}

        # for i in range(size):
        #     n = nums[i]
        #     freq[n] = freq.get(n,0) + 1
        #     if n not in first_ocr:
        #         first_ocr[n] = i
        #     last_ocr[n] = i
        
        # degree = max(freq.values())

        # res = float("inf")
        # for i in freq:
        #     if freq[i] == degree:
        #         length = (last_ocr[i] - first_ocr[i]) + 1
        #         res = min(res,length)
        # return res

    
        numsCounter = Counter(nums)
        maxCount = max(numsCounter.values())
        if maxCount == 1:
            return 1
        numsLen = len(nums)
        minLen = numsLen
        for num, count in numsCounter.items():
            if count == maxCount:
                left = nums.index(num)
                right = numsLen - nums[::-1].index(num) - 1

                minLen = min(minLen, right - left + 1)

        return minLen


   