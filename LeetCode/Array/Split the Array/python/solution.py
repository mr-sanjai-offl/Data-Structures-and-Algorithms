from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        for key in frequency:
            if frequency[key] > 2:
                return False
        return True