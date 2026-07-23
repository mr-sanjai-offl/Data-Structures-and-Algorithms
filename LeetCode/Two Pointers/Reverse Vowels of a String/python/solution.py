class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        arr = list(s)
        x = 0
        y = len(arr) - 1

        while x < y:
            if arr[x] not in vowels:
                x += 1
            elif arr[y] not in vowels:
                y -= 1
            else:
                arr[x], arr[y] = arr[y], arr[x]
                x += 1
                y -= 1

        return ''.join(arr)