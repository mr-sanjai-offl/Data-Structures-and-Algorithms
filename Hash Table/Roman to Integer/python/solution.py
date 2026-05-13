class Solution:
    def romanToInt(self, s: str) -> int:
        n2={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans=0
        for i in range(len(s)):
            if(i+1 < len(s) and n2[s[i]] < n2[s[i+1]]):
                ans-=n2[s[i]]
            else:
                ans+=n2[s[i]]
        return ans