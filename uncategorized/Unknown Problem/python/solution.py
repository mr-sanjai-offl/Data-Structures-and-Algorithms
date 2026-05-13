1class Solution:
2    def reverse(self, x: int) -> int:
3        y = int(str(abs(x))[::-1])
4        res = -y if x < 0 else y
5        return 0 if res < -(2**31) or res > 2**31 - 1 else res
6