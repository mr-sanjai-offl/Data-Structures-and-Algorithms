class Solution:
    def maximum69Number (self, num: int) -> int:
        res = []
        s = str(num)
        n = len(s)
        i = 0
        res.append(int(s))
        temp = [i for i in s]

        while i < n:
            if s[i] == '6' or s[i] == '9':
                if s[i] == '6':
                    temp[i] = '9'
                    res.append(int(''.join(temp)))
                else:
                    temp[i] = '6'
                    res.append(int(''.join(temp)))
            temp = [i for i in s]
            i+=1
        return max(res)
            
        