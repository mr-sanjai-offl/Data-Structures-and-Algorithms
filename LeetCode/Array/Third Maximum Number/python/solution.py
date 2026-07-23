class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
        arr.sort(reverse=True)
        if len(arr) < 3:
            return arr[0]
        return arr[2]