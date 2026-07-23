class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = [0] * 26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        for j in t:
            arr[ord(j) - ord('a')] -= 1
        for k in range(26):
            if arr[k] < 0:
                return chr(k + ord('a'))