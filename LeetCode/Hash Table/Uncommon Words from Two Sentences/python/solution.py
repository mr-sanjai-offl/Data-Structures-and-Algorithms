class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list:
        arr1 = s1.split()
        arr2 = s2.split()
        count = {}

        for word in arr1:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        for word in arr2:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        result = []
        for word in count:
            if count[word] == 1:
                result.append(word)

        return result