class Solution:
    def countAndSay(self, n: int) -> str:
    #     res = "1"
    #     if n == 1:
    #         return '1'
    #     for i in range(1,n):
    #         res = self.count(res)
    #     return res
    # def count(self, res: str) -> str:
    #     temp = ""
    #     count = 1
    #     for i in range(1,len(res)):
    #         if res[i] == res[i-1]:
    #             count+=1
    #         else:
    #             temp+=str(count)+res[i-1]
    #             count=1
    #     temp+=str(count)+res[-1]
    #     return temp

        s = "1"
        if n == 1:
            return '1'
        for i in range(n-1):

            temp = ""
            count = 1
            for i in range(1,len(s)):

                if s[i] == s[i-1]:
                    count+=1
                else:
                    temp+=str(count)+s[i-1]
                    count=1
            temp+=str(count)+s[i]
            s=temp
        return s
        
            

        
