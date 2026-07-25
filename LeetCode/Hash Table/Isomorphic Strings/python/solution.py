class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = [0]*256
        b = [0]*256

        for i in range(len(s)):
            sch = ord(s[i])
            tch = ord(t[i])
            if a[sch] != 0 and a[sch] != tch:
                return False
            else:
                a[sch] = tch

            if b[tch] != 0 and b[tch] != sch:
                return False
            else:
                b[tch] = sch
        return True