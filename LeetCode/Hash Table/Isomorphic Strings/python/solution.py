class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #s,t = "badc","baba"
        m1 = []
        m2 = []

        # for a,b in zip(s,t):
        #     m1.append(s.index(a))
        #     m2.append(t.index(b))
        for a in s:
            m1.append(s.index(a))
        for a in t:
            m2.append(t.index(a))
        
        if m1 != m2:
            return False
        return True
        
