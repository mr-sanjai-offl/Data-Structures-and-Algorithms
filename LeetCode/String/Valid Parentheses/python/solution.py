class Solution:
    def isValid(self, s: str) -> bool:
        o=['(','{','[']
        b = {')':'(','}':'{',']':'['}
        t=[]

        for i in s:
            if i in o:
                t.append(i)
            elif len(t) != 0 and i in b and t[-1] == b[i]:
                t.pop()
            else:
                return False
        return t == []
     

        
        