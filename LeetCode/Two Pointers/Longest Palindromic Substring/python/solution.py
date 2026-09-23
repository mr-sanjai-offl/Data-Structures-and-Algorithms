class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        max_len = 0
        for i in range(n):
            for j in range(i+1,n+1):
                st = s[i:j]
                if st == st[::-1] and len(st) > max_len:
                    max_len = len(st)
                    res = st
        return res