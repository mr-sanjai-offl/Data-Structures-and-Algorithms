class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a = m
        b = n
        for op in ops:
            if op[0] < a:
                a = op[0]
            if op[1] < b:
                b = op[1]
        return a * b