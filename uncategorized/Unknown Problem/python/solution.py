1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3
4        res = []
5        prow = []
6        crow = []
7
8        for i in range(0,numRows):
9            for j in range(0,i+1):
10                if j==0 or j==i:
11                    crow.append(1)
12                else:
13                    temp = prow[j-1] + prow[j]
14                    crow.append(temp)
15            res.append(crow)
16            prow=crow
17            crow=[]
18
19        return res