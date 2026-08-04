# from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return [i for i in permutations(nums,len(nums))]
        used = [False] * len(nums)
        res = []

        def dfs(path):
            
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])

                dfs(path)

                path.pop()
                used[i] = False
        
        dfs([])
        return res

        