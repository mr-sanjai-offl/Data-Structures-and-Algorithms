class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastCount = 0
        d = s.strip().split(" ")
        return len(d[-1])
        # for i in s.strip()[::-1]:
        #     if i != " ":
        #         lastCount+=1
        #     else:
        #         break
        # return lastCount