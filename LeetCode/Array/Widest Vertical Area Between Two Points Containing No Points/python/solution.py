class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted([x for x, _ in points])
        re=[]
        for i in range(len(xs)-1,0,-1):
            if(i<len(xs)):
                r=xs[i]-xs[i-1]
                re.append(r)

        return max(re)
        