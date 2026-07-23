class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for i in magazine:
            arr[ord(i) - ord('a')] += 1
        for i in ransomNote:
            arr[ord(i) - ord('a')] -= 1
            if arr[ord(i) - ord('a')] < 0:
                return False
        return True