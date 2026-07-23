from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False
        # alps = [0]*26

        # for i in range(len(s)):
        #     alps[ord(s[i]) - ord('a')] += 1
        #     alps[ord(t[i]) - ord('a')] -= 1
        
        # for i in alps:
        #     if i != 0:
        #         return False
        # return True

        # return sorted(list(s)) == sorted(list(t))


        