class Solution:
    def compress(self, chars: List[str]) -> int:
        l = len(chars)
        count = 1
        string = ""
        for i in range(1,l):
            if chars[i] == chars[i-1]:
                count+=1
            else:
                
                if count == 1:
                    string += chars[i-1]
                else:
                    string += chars[i-1]+ str(count)
                count=1
        if count == 1:
            string += chars[l-1]
        else:
            string += chars[l-1]+ str(count)
        for i in range(0,len(string)):
            chars[i] = string[i]

        return len(string)