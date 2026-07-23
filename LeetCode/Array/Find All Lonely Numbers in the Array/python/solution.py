class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        for i in nums:
            if freq[i] == 1 and (i+1 not in freq) and (i-1 not in freq) :
                res.append(i)
        return res