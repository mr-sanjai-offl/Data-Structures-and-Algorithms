class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left = [0]*26
        right = [0]*26
        for i in range(n):
            right[ord(s[i]) - ord('a')] += 1
        res = 0
        for i in range(n-1):
            left[ord(s[i]) - ord('a')] += 1
            right[ord(s[i]) - ord('a')] -= 1
            l = 0
            r = 0
            for j in range(0,26):
                if left[j] > 0 :
                    l += 1
                if right[j] > 0:
                    r += 1
            if l == r:
                res += 1
        return res 


