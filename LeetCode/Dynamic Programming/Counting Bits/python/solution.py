class Solution:
    def countBits(self, n: int) -> list:
        arr = [0] * (n + 1)
        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                count += x % 2
                x //= 2
            arr[i] = count
        return arr