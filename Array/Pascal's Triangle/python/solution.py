
        for i in range(0,numRows):
            for j in range(0,i+1):
                if j==0 or j==i:
                    crow.append(1)
                else:
                    temp = prow[j-1] + prow[j]
                    crow.append(temp)
            res.append(crow)
            prow=crow
            crow=[]

        return res
