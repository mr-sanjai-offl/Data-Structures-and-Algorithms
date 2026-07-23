class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split()
        result = ""
        for i in range(k):
            if i > 0:
                result += " "
            result += arr[i]
        return result