class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid[0])
        count = 0
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(grid[j][i])
            for k in range(size):
                if temp == grid[k]:
                    count+=1
            temp = []
        return count
            
