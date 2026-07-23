class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = 0
        for i in s:
            if s.count(i) == 1:
                return idx
            idx+=1
        return -1