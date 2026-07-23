class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0

        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
            if s[i] == 'L':
                l += 1
                if l == 3:
                    return False
            else:
                l = 0

        return a < 2