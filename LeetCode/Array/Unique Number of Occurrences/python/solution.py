class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        for x in arr:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        occurrences = []
        for y in count:
            occurrences.append(count[y])

        for i in range(len(occurrences)):
            for j in range(i + 1, len(occurrences)):
                if occurrences[i] == occurrences[j]:
                    return False
        return True