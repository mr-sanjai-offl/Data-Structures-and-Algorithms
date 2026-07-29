class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispali(s):
            return s == s[::-1]
        n = len(s)
        if n == 1:
            return s
        maxlen = 0
        res = ""
        for i in range(0,n):
            for j in range(i+1,n+1):
                sub = s[i:j]
                if ispali(sub) and len(sub) > maxlen:
                    maxlen = len(sub)
                    res = sub
        return res