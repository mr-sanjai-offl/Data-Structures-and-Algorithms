class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1
        # for i in range(0,m):
        #     for j in range(0,n):
        #         if(matrix[i][j]!=matrix[i+1][j+1]):
        #             return False
        # return True
        
        #pythonic way by majority trick

        return all(matrix[i][j] == matrix[i+1][j+1] for i in range(0,m) for j in range(0,n))

