class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(pattern) != len(arr):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(pattern)):
            x = pattern[i]
            y = arr[i]

            if x not in map1:
                map1[x] = y
            if y not in map2:
                map2[y] = x

            if map1[x] != y or map2[y] != x:
                return False

        return True