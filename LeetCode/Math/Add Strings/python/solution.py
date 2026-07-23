class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x = len(num1)
        y = len(num2)
        i = 0
        carry = 0
        result = []

        while i < x or i < y or carry:
            a = 0
            b = 0
            if i < x:
                a = int(num1[x - 1 - i])
            if i < y:
                b = int(num2[y - 1 - i])
            total = a + b + carry
            carry = total // 10
            result.append(str(total % 10))
            i += 1

        return ''.join(result[::-1])