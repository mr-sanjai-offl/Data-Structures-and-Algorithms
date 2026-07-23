class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        m = 0
        c = 0

        for i in range(len(s)):
            c += self.isvow(s[i])
            if(i>=k):
                c -= self.isvow(s[i-k])
            
            m=max(m,c)
        return m

    


    def isvow(self, c: chr) -> int:
        if c in "aeiou":
            return 1
        return 0

           
        
