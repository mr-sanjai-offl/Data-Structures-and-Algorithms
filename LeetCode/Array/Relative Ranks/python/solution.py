class Solution:
    def findRelativeRanks(self, score):
        arr = sorted(score, reverse=True)
        answer = []
        for i in range(len(score)):
            x = arr.index(score[i]) + 1
            if x == 1:
                answer.append("Gold Medal")
            elif x == 2:
                answer.append("Silver Medal")
            elif x == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(x))
        return answer