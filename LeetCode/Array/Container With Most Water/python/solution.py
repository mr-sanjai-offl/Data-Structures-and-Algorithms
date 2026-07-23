class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maximum = 0
        width = 0
        while(l < r):
            width = r - l
            area = min(height[l],height[r]) * width
            maximum = max(maximum, area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maximum

