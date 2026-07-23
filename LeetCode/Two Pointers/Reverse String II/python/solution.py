class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        i = 0
        while i < len(arr):
            if i + k < len(arr):
                arr[i:i+k] = reversed(arr[i:i+k])
            else:
                arr[i:len(arr)] = reversed(arr[i:len(arr)])
            i += 2 * k
        return ''.join(arr)