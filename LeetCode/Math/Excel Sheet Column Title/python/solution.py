class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber > 0:
            x = (columnNumber - 1) % 26
            arr.append(chr(x + 65))
            columnNumber = (columnNumber - 1) // 26
        arr.reverse()
        return ''.join(arr)