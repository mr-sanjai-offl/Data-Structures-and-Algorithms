class Solution:
    def shortestToChar(self, s: str, c: str):
        arr = []
        n = len(s)

        for i in range(n):
            min_distance = n
            for j in range(n):
                if s[j] == c:
                    distance = abs(i - j)
                    if distance < min_distance:
                        min_distance = distance
            arr.append(min_distance)

        return arr