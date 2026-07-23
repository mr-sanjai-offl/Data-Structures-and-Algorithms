class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        first = {0: -1}
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                print(f"nums{i} = {nums[i]}")
                prefix -= 1
            else:
                print(f"nums{i} = {nums[i]}")
                prefix += 1

            if prefix in first:
                ans = max(ans, i - first[prefix])
                print(f"ans = {ans}")
            else:
                first[prefix] = i
                print(f"anselse = {first[prefix]}")
        print(first)
        return ans