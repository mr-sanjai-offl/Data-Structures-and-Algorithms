class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        fw = [0]*n
        bw = [0]*n
        f = 1
        b = 1
        fw[0]=f
        bw[n-1]=b
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                f = f+1
            else:
                f=1
            fw[i]=f
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                b = b+1
            else:
                b=1  
            bw[i]=b
        count=0
        for i,j in zip(fw,bw):
            count+=max(i,j)
        return count

        