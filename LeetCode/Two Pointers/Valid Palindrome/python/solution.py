class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = [i.lower() for i in s if i.isalnum()]
        return "".join(txt) == "".join(txt[::-1])