class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        return True if str(x)==y[::-1] else False
        