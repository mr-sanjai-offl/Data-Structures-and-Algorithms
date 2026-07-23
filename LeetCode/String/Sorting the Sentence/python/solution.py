class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        res = ["" for _ in range(len(arr))]

        for word in arr:
            i = int(word[-1]) - 1
            res[i] = word[:-1]

        return " ".join(res)