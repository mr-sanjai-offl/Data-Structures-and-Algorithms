class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        return [i for i in freq if freq[i] == 1]