class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        arr = [''] * len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        return ''.join(arr)