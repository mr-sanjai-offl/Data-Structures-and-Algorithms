class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1

        maxlen = 0

        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                maxlen = max(maxlen,left[i] + right[i] + 1)

        return maxlen