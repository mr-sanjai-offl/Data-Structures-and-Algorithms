class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        d = -1
        idx = 0

        res = [""]*numRows

        for i in s:
            res[idx] += i

            if idx == 0 or idx == numRows - 1:
                d *= -1
            
            idx += d
        
        return "".join(res)
