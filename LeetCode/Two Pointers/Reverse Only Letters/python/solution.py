class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        x = 0
        y = len(arr) - 1

        while x < y:
            if not arr[x].isalpha():
                x += 1
            elif not arr[y].isalpha():
                y -= 1
            else:
                arr[x], arr[y] = arr[y], arr[x]
                x += 1
                y -= 1

        return ''.join(arr)